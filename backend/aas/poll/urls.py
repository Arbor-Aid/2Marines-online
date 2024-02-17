from django.urls import path

from . import views

app_name = 'poll'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:org_id>/', views.OrgView, name='org_view'),
]
