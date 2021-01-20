from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.urls import path

app_name = 'rewardsapp'
urlpatterns = [
        
    path('employee_list/', views.employee_list, name = 'employee_list'),
    path('employee_new/', views.employee_new, name = 'employee_new'),
    path('employee/<int:client_id>/edit/', views.employee_edit, name='employee_edit'),
    path('employee/<int:client_id>/delete/', views.employee_delete, name='employee_delete'),

    path('reward_list/', views.reward_list, name = 'reward_list'),
    path('reward_new/', views.reward_new, name = 'reward_new'),
    path('reward/<int:reward_id>/edit/', views.reward_edit, name='reward_edit'),
    path('reward/<int:reward_id>/delete/', views.reward_delete, name='reward_delete'),

    path('employee_reward_list/', views.employee_reward_list, name = 'employee_reward_list'),
    path('employee_reward_new/', views.employee_reward_new, name = 'employee_reward_new'),
    path('employee_reward/<int:employee_reward_id>/delete/', views.employee_reward_delete, name='employee_reward_delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
