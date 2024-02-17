from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('org/', views.OrganizationViewSet.as_view({'get': 'list'}), name='orgs'),
    path('org/create/', views.OrganizationViewSet.as_view({'post': 'create'}), name='org_create'),
    path('org/by-id/<uuid:org_id>/', views.OrganizationByIdViewSet.as_view(), name='org_by_id'),
    path('org/update/<uuid:org_id>/', views.OrganizationUpdateByIdViewSet.as_view(), name='org_update'),
    path('org/delete/<uuid:org_id>/', views.OrganizationDeleteByIdViewSet.as_view(), name='org_delete'),
    path('hours/', views.HoursViewSet.as_view({'get': 'list'}), name='hours'),
    path('hours/create/', views.HoursViewSet.as_view({'post': 'create'}), name='hours_create'),
    path('hours/by-org-id/<uuid:org_id>/', views.HoursByOrgIdViewSet.as_view(), name='hours_by_org_id'),
    path('hours/by-id/<uuid:hour_id>/', views.HoursByIdViewSet.as_view(), name='hours_by_id'),
    path('hours/update/<uuid:hour_id>/', views.HoursUpdateByIdViewSet.as_view(), name='hours_update'),
    path('hours/delete/<uuid:hour_id>/', views.HoursDeleteByIdViewSet.as_view(), name='hours_delete'),
]

# county
# Services
