from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views
router  = DefaultRouter()
router.register('list',views.GuestViewSet)
router.register('user',views.UserViewSet)
router.register('edit_profile',views.EditProfileViewSet,basename='edit_profile')
urlpatterns = [
    path('',include(router.urls)),
    path("register/",views.RegistrationApiView.as_view(),name="register"),
    # path("edit_profile/",views.EditProfileViewSet.as_view(),name="edit_profile"),
    path("change_password/<int:pk>/",views.PasswordChangeViewSet.as_view(),name="change_password"),
    path("active/<uid64>/<token>/",views.activate,name="activate"),
    path("login/",views.UserLoginApiView.as_view(),name="login"),
    path("logout/",views.UserLogoutApiView.as_view(),name="logout"),
    path("admin_request/",views.AdminRequestViewSet.as_view(),name="admin_request"),
    path("admin_list/",views.AdminListViewSet.as_view(),name="admin_list"),
    path("user_list/",views.UserListViewSet.as_view(),name="user_list"),
    path("api/auth/google/login/",views.GoogleLogin.as_view(),name="google_login"),
]
