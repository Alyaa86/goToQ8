"""goToQ8_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from goToQ8 import views
# (
#     HotAndTrendAPIView,
#     FavouriteCreateView,
#     UserRegisterView,
#     LoginUserView,
#     EventListAPIView,
#     EventDetailAPIView,
#     EventCreateAPIView,
#     EventUpdateAPIView,
#     EventDeleteAPIView,
#     PlanListAPIView,
#     PlanDetailAPIView,
#     PlanCreateAPIView,
#     PlanUpdateAPIView,
#     PlanDeleteAPIView,
#     ProfileListAPIView,
#     ProfileDetailAPIView,
#     ProfileCreateAPIView,
#     ProfileUpdateAPIView,
#     ProfileDeleteAPIView,
#     FriendListAPIView,
#     FriendDetailAPIView,
#     FriendCreateAPIView,
#     FriendUpdateAPIView,
#     FriendDeleteAPIView,
#     )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hot_and_trend', views.HotAndTrendAPIView.as_view(), name='hot_and_trend'),
    path('favourite', views.FavouriteCreateView.as_view(), name='favourite'),
    path('favourites', views.FavouriteListView.as_view(), name='favourites'),
    path('register', views.UserRegisterView.as_view(), name='register'),
    path('login', views.LoginUserView.as_view(), name='login'),

    path('event_list', views.EventListAPIView.as_view(), name='event_list'),
    path('event_detail/<int:event_id>/', views.EventDetailAPIView.as_view(), name='event_detail'),
    path('event_create', views.EventCreateAPIView.as_view(), name='event_create'),
    path('event_update/<int:event_id>/', views.EventUpdateAPIView.as_view(), name='event_update'),
    path('event_delete/<int:event_id>/', views.EventDeleteAPIView.as_view(), name='event_delete'),

    path('plan_list', views.PlanListAPIView.as_view(), name='plan_list'),
    path('plan_detail/<int:plan_id>/', views.PlanDetailAPIView.as_view(), name='plan_detail'),
    path('plan_create', views.PlanCreateAPIView.as_view(), name='plan_create'),
    path('plan_update/<int:plan_id>/', views.PlanUpdateAPIView.as_view(), name='plan_update'),
    path('plan_delete/<int:plan_id>/', views.PlanDeleteAPIView, name='plan_delete'),

    path('profile_list', views.ProfileListAPIView.as_view(), name='profile_list'),
    path('profile_detail/<int:profile_id>/', views.ProfileDetailAPIView.as_view(), name='profile_detail'),
    path('profile_create', views.ProfileCreateAPIView.as_view(), name='profile_create'),
    path('profile_update/<int:profile_id>/', views.ProfileUpdateAPIView.as_view(), name='profile_update'),
    path('profile_delete/<int:profile_id>/', views.ProfileDeleteAPIView.as_view(), name='profile_delete'),

    path('friend_list', views.FriendListAPIView.as_view(), name='friend_list'),
    path('friend_detail/<int:friend_id>/', views.FriendDetailAPIView.as_view(), name='friend_detail'),
    path('friend_create', views.FriendCreateAPIView.as_view(), name='friend_create'),
    path('friend_update/<int:friend_id>/', views.FriendUpdateAPIView.as_view(), name='friend_update'),
    path('friend_delete/<int:friend_id>/', views.FriendDeleteAPIView.as_view(), name='friend_delete'),




]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)