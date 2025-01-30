from . import views
from django.urls import path

urlpatterns = [
    path("", views.main, name="landing"),
    path("<int:product_id>", views.detail, name="detail"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout_user, name="logout"),
    path("login", views.login_user, name="login"),
]