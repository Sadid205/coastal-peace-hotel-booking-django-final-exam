from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views
router  = DefaultRouter()
router.register('list',views.GuestViewSet)
router.register('user',views.UserViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path("register/",views.RegistrationApiView.as_view(),name="register"),
    path("edit_profile/",views.EditProfileViewSet.as_view(),name="edit_profile"),
    path("change_password/<int:pk>/",views.PasswordChangeViewSet.as_view(),name="change_password"),
    path("active/<uid64>/<token>/",views.activate,name="activate"),
    path("login/",views.UserLoginApiView.as_view(),name="login"),
    path("logout/",views.UserLogoutApiView.as_view(),name="logout"),
    # path("user/",views.UserViewSet.as_view(),name="user"),
]
