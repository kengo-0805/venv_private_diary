from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'index.html' # テンプレートファイルの指定（templatesディレクトリから探してくる）