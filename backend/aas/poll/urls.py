from django.urls import path

from . import views

app_name = 'poll'
urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.OrgInputStart, name='org_input_start'),
    path('search/', views.OrgSearch, name='org_search'),
    path('edit/', views.OrgEdit, name='org_edit'),
    path('edit/<int:org_id>/', views.OrgEdit, name='org_edit'),
    path('api/', views.OrganizationViewSet.as_view({'get': 'list'}), name='api'),
]
