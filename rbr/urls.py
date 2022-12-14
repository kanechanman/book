from django.urls import path
from rbr import views

app_name = 'rbr'
urlpatterns = [
    # 書籍
    path('book/', views.book_list, name='book_list'),   # 一覧
    path('book/add/', views.book_edit, name='book_add'),  # 登録
    path('book/mod/<int:book_id>/', views.book_edit, name='book_mod'),  # 修正
    path('book/del/<int:book_id>/', views.book_del, name='book_del'),# 削除
    path('impression/<int:book_id>/', views.ImpressionList.as_view(), name='impression_list'),  # 一覧
    path('impression/add/<int:book_id>/', views.impression_edit, name='impression_add'),        # 登録
    path('impression/mod/<int:book_id>/<int:impression_id>/', views.impression_edit, name='impression_mod'),  # 修正
    path('impression/del/<int:book_id>/<int:impression_id>/', views.impression_del, name='impression_del'),   # 削除
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
]
