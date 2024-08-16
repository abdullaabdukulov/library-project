from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_view

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path(
        "password_change/", auth_view.PasswordChangeView.as_view(
            success_url=reverse_lazy("accounts:password_change_done")
        ), name="password_change"
    ),
    path(
        "password_change/done/",
        auth_view.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", auth_view.PasswordResetView.as_view(
        success_url=reverse_lazy("accounts:password_reset_done")
    ), name="password_reset"),
    path(
        "password_reset/done/",
        auth_view.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_view.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy("accounts:password_reset_complete")
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_view.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
