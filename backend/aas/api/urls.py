from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('org/', views.OrganizationViewSet.as_view({'get': 'list'}), name='orgs'),
    path('org/create/', views.OrganizationViewSet.as_view({'post': 'create'}), name='org_create'),
    path('org/by-id/<uuid:org_id>/', views.OrganizationByIdViewSet.as_view(), name='org_by_id'),
    path('org/update/<uuid:org_id>/', views.OrganizationUpdateByIdViewSet.as_view(), name='org_update'),
    path('org/delete/<uuid:org_id>/', views.OrganizationDeleteByIdViewSet.as_view(), name='org_delete'),
]

# county
# Services
