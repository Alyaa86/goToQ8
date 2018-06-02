from django.shortcuts import render
from rest_framework.generics import (
	RetrieveAPIView, 
	DestroyAPIView, 
	CreateAPIView, 
	RetrieveUpdateAPIView, 
	ListAPIView,
	)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsStaff
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import (
	UserRegisterSerializer,
	LoginUserSerializer,
	FavouriteListSerializer,
	FavouriteCreateSerializer,
	EventListSerializer,
	EventDetailSerializer,
	EventCreateSerializer,
	EventUpdateSerializer,
	PlanListSerializer,
	PlanDetailSerializer,
	PlanCreateSerielizer,
	PlanUpdateSerielizer,
	ProfileListSerializer,
	ProfileDetailSerializer,
	ProfileCreateSerielizer,
	ProfileUpdateSerielizer,
	FrindListSerielizer,
	FrindDetailSerielizer,
	FrindCreateSerielizer,
	FriendUpdateSerielizer
	)
from .models import (
	Event,
	Plan,
	Favourite,
	Friends,
	Profile
	)

# Create your views here

class HotAndTrendAPIView(ListAPIView):
	queryset = Event.objects.filter(hot_and_trend=True)
	serializer_class = EventListSerializer
	permission_classes = [AllowAny,]

	# def get_queryset(self):
		# user = self.request.user
      
		# return Event.objects.filter(hot_and_trend=True)

		# queryset = Event.objects.all()
		# queryset = queryset.filter(hot_and_trend=True)
		# return queryset


class FavouriteCreateView(CreateAPIView):
	queryset= Favourite.objects.all()
	serializer_class = FavouriteCreateSerializer
	permission_classes = [AllowAny,]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class FavouriteListView(ListAPIView):
	queryset= Favourite.objects.all()
	serializer_class = FavouriteListSerializer
	permission_classes = [AllowAny,]


class UserRegisterView(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserRegisterSerializer
	permission_classes = [AllowAny,]

class LoginUserView(APIView):
	serializer_class = LoginUserSerializer
	permission_classes = [AllowAny,]
	def post(self, request, format=None):
		my_data = request.data
		serializer = LoginUserSerializer(data=my_data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response (new_data, status=HTTP_200_OK)
		return Response (serializer.errors, status=HTTP_400_BAD_REQUEST)




class EventListAPIView(ListAPIView):
	queryset= Event.objects.all()
	serializer_class = EventListSerializer
	permission_classes = [AllowAny,]
	filter_backends = [SearchFilter, OrderingFilter,]
	searchFields = ['title', 'event_date', 'color', 'category']


class EventDetailAPIView(RetrieveAPIView):
	queryset= Event.objects.all()
	serializer_class = EventDetailSerializer
	lookup_fiel = 'id'
	lookup_url_kwarg = 'event_id'
	permission_classes = [AllowAny,]


class EventCreateAPIView(CreateAPIView):
	queryset= Event.objects.all()
	serializer_class = EventCreateSerializer
	permission_classes = [IsAdminUser, IsStaff,]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class EventUpdateAPIView(RetrieveUpdateAPIView):
	queryset= Event.objects.all()
	serializer_class = EventUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'event_id'
	permission_classes = [IsAdminUser, IsStaff,]

class EventDeleteAPIView(DestroyAPIView):
	queryset= Event.objects.all()
	serializer_class = EventDetailSerializer
	lookup_fiel = 'id'
	lookup_url_kwarg = 'event_id'
	permission_classes = [IsAdminUser, IsStaff,]





class PlanListAPIView(ListAPIView):
	model = Plan
	serializer_class = PlanListSerializer
	permission_classes = [IsAuthenticated,]
	
	def get_queryset(self):
		return Plan.objects.filter(planner=self.request.user)
	

class PlanDetailAPIView(RetrieveAPIView):
	queryset= Plan.objects.all()
	serializer_class = PlanDetailSerializer
	lookup_fiel = 'id'
	lookup_url_kwarg = 'plan_id'
	permission_classes = [IsAuthenticated,]


class PlanCreateAPIView(CreateAPIView):
	queryset= Plan.objects.all()
	serializer_class = PlanCreateSerielizer
	permission_classes = [IsAuthenticated,]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class PlanUpdateAPIView(RetrieveUpdateAPIView):
	queryset= Plan.objects.all()
	serializer_class = PlanUpdateSerielizer
	lookup_field = 'id'
	lookup_url_kwarg = 'plan_id'
	permission_classes = [IsAuthenticated,]

class PlanDeleteAPIView(DestroyAPIView):
	queryset= Plan.objects.all()
	serializer_class = PlanDetailSerializer
	lookup_fiel = 'id'
	lookup_url_kwarg = 'plan_id'
	permission_classes = [IsAuthenticated,]




class ProfileListAPIView(ListAPIView):
	queryset = Profile
	serializer_class = ProfileListSerializer
	permission_classes = [AllowAny,]

	def get_queryset(self):
		return Profile.objects.filter(user=self.request.user)

class ProfileDetailAPIView(RetrieveAPIView):
	queryset= Profile.objects.all()
	serializer_class = ProfileDetailSerializer
	lookup_fiel = 'id'
	lookup_url_kwarg = 'profile_id'
	permission_classes = [IsAuthenticated,]


class ProfileCreateAPIView(CreateAPIView):
	queryset= Profile.objects.all()
	serializer_class = ProfileCreateSerielizer
	permission_classes = [AllowAny,]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class ProfileUpdateAPIView(RetrieveUpdateAPIView):
	queryset= Profile.objects.all()
	serializer_class = ProfileUpdateSerielizer
	lookup_field = 'id'
	lookup_url_kwarg = 'profile_id'
	permission_classes = [IsAuthenticated,]

class ProfileDeleteAPIView(DestroyAPIView):
	queryset= Profile.objects.all()
	serializer_class = ProfileDetailSerializer
	lookup_fiel = 'id'
	lookup_url_kwarg = 'profile_id'
	permission_classes = [IsAuthenticated,]




class FriendListAPIView(ListAPIView):
	queryset= Friends.objects.all()
	serializer_class = FrindListSerielizer
	permission_classes = [AllowAny,]
	

class FriendDetailAPIView(RetrieveAPIView):
	queryset= Friends.objects.all()
	serializer_class = FrindDetailSerielizer
	lookup_fiel = 'id'
	lookup_url_kwarg = 'friend_id'
	permission_classes = [AllowAny,]


class FriendCreateAPIView(CreateAPIView):
	queryset= Friends.objects.all()
	serializer_class = FrindCreateSerielizer
	permission_classes = [IsAdminUser,]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class FriendUpdateAPIView(RetrieveUpdateAPIView):
	queryset= Friends.objects.all()
	serializer_class = FriendUpdateSerielizer
	lookup_field = 'id'
	lookup_url_kwarg = 'friend_id'
	permission_classes = [IsAdminUser,]

class FriendDeleteAPIView(DestroyAPIView):
	queryset= Friends.objects.all()
	serializer_class = FrindDetailSerielizer
	lookup_fiel = 'id'
	lookup_url_kwarg = 'friend_id'
	permission_classes = [IsAdminUser,]





















