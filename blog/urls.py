from django.urls import path, include
from blog import views

app_name = 'blog'

urlpatterns = [

    # path('', include('blog.urls')),
    # path('', views.index),
    # path('about', views.about),
    # path('contact', views.contact),
    path('', views.post_list, name='post_list')
]