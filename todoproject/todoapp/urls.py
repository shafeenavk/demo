from django.conf.urls.static import static
from django.urls import path

from todoproject import settings
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/',views.update,name='update'),
    path('lv/',views.TaskListView.as_view(),name='lv'),
    path('dv/<int:pk>/',views.TaskDetailView.as_view(),name='dv'),
    path('upv/<int:pk>/',views.TaskUpdateView.as_view(),name='upv'),
    path('delv/<int:pk>',views.TaskDeleteView.as_view(),name='delv')
]