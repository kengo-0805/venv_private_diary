import logging

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import InquiryForm
from .models import Diary
from .forms import InquiryForm, DiaryCreateForm

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries
    
class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'
    # slug_field = "title" # モデルのフィールドの名前
    # slug_url_kwarg = "title" # urls.pyのキーワードの名前

class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    # モデルとテンプレートを設定
    # モデルを設定
    model = Diary
    # テンプレートを設定
    template_name = 'diary_create.html'
    # フォームを設定
    form_class = DiaryCreateForm
    # 成功時のリダイレクト先を設定
    success_url = reverse_lazy('diary:diary_list')

    # ビジネスロジックを実装
    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '日記の作成に失敗しました。')
        return super().form_invalid(form)