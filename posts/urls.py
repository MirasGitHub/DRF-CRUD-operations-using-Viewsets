from django.urls import path

from posts.views import LoginView, LogoutView, PostList, PostDetail, RegisterView

urlpatterns = [
    path("user/register/", RegisterView.as_view(), name='register'),
    path("user/login/", LoginView.as_view(), name='login'),
    path("user/logout/", LogoutView.as_view(), name='logout'),
    path("posts/", PostList.as_view(), name='posts'),
    path("posts/<int:pk>/", PostDetail.as_view(), name='post detail'),
]
