from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import user_list, user_edit, user_new, user_delete

urlpatterns = [
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html')),

    # reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('user_list/', user_list, name='user_list'),
    path('<int:pk>/edit/', user_edit, name='user_edit'),
    path('user_create/', user_new, name='user_new'),
    path('<int:pk>/delete/', user_delete, name='user_delete'),
]