
from django.urls import path
from . import views


urlpatterns = [
        # path('', views.home, name='home'),
        path('home/', views.home, name='home'),
        path('book_detail/', views.book_detail, name='book_detail'),
        path(
            'book/<int:book_id>/',
            views.book_detail,name='book_detail'
        ),
]
