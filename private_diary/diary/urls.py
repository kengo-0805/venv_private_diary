from django.urls import path
from . import views

app_name = 'diary' # アプリケーションのルーティングに名前を設定（diaryアプリケーションのルーティングと明示）
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # インデックスビューに処理を渡す　nameはルーティング処理の引き継ぎ識別名
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'), # お問い合わせビューに処理を渡す
]