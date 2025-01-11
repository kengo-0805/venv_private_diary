from django.views import generic
from .forms import InquiryForm
import logging
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = 'index.html' # テンプレートファイルの指定（templatesディレクトリから探してくる）

class InquiryView(generic.FormView):
    template_name = 'inquiry.html' # テンプレートファイルの指定（templatesディレクトリから探してくる）
    form_class = InquiryForm # フォームクラスの指定
    success_url = reverse_lazy('diary:inquiry') # 送信完了後のリダイレクト先のURL

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)