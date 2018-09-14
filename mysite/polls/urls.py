from django.urls import path
from . import views

app_name = 'polls'
# urlpatterns = [
#     path('', views.index, name='index'),
#     # /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/result/', views.result, name='result'),
#     path('<int:question_id>/vote/', views.vote, name='vote')
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsViews.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]