from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [

    path('', views.index, name='index'),
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    path('new_blog/', views.new_blog, name='new_blog'),
    # path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]