from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework.validators import UniqueValidator
from .models import (
	Event,
	Plan,
	Favourite,
	Friends,
	Profile
	)
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name']

class UserRegisterSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(
			required=True,
			validators=[UniqueValidator(queryset=User.objects.all())]
			)
	username = serializers.CharField(
			required=True,
			validators=[UniqueValidator(queryset=User.objects.all())]
			)
	password = serializers.CharField(min_length=6, style={'input_type':'password'}, write_only=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']
		
		def create(self, validated_data):
			new_user=User(**validated_data)
			new_user.set_password(validated_data['password'])
			new_user.save()
			return validated_data

class LoginUserSerializer(serializers.Serializer):
	username= serializers.CharField()
	password= serializers.CharField(style={'input_type':'password'}, write_only=True)
	token = serializers.CharField(allow_blank=True, read_only=True)
	
	def validate(self, data):
		username = data.get('username')
		password = data.get('password')


		if username == '':
			raise serializers.ValidationError("A username is required to login")

		try:
			user_obj= User.objects.get(username=username)
		except:
			raise serializers.ValidationError("this username does not exsit")
		if not user_obj.check_password(password):
			raise serializers.ValidationError("check your password and try again")

		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

		payload = jwt_payload_handler(user_obj)
		token = jwt_encode_handler(payload)

		data["token"] = token 

		return data

class FavouriteListSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = Favourite
		fields = ['user']

class FavouriteCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Favourite 
		fields = ['event']


class EventListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name='event_detail', # n76 el esm mal el url mal el detail eli e7na msamena bl urls
		lookup_field='id',
		lookup_url_kwarg ='event_id',
		)
	owner = UserSerializer()
	class Meta:
		model = Event
		fields = ['title', 'image', 'event_date', 'owner', 'detail']


class EventDetailSerializer(serializers.ModelSerializer):
	delete = serializers.HyperlinkedIdentityField(
		view_name='event_delete', 
		lookup_field='id',
		lookup_url_kwarg ='event_id',
		)
	update = serializers.HyperlinkedIdentityField(
		view_name='event_update', 
		lookup_field='id',
		lookup_url_kwarg ='event_id',
		)

	owner = UserSerializer()
	# Favourite = serializers.SerializerMethodField()

	class Meta:
		model = Event
		fields = '__all__'

		def get_Favourite(self, obj):
			favourites = obj.favourite_set.all()
			jsaon_favourite = FavouriteListSerializer(favourites, many=True).data
			return jsaon_favourite

class EventCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model= Event
		fields =['title' , 'description', 'image', 'event_date', 'color', 'category', 'hot_and_trend']

class EventUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model= Event
		fields =['title' , 'description', 'image', 'event_date', 'color', 'category', 'hot_and_trend']

class PlanListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name='plan_detail', 
		lookup_field='id',
		lookup_url_kwarg ='plan_id',
    	)
	owner = UserSerializer()
	class Meta:
		model = Plan
		fields = ['weekend_date', 'owner', 'detail']


class PlanDetailSerializer(serializers.ModelSerializer):
	delete = serializers.HyperlinkedIdentityField(
		view_name='plan_delete', 
		lookup_field='id',
		lookup_url_kwarg ='plan_id',
		)
	update = serializers.HyperlinkedIdentityField(
		view_name='plan_update', 
		lookup_field='id',
		lookup_url_kwarg ='plan_id',
		)

	owner = UserSerializer()

	class Meta:
		model = Plan
		fields = ['weekend_date', 'plans', 'owner', 'delete', 'update']

class PlanCreateSerielizer(serializers.ModelSerializer):
	class Meta:
		model = Plan 
		fields = ['weekend_date', 'plans']

class PlanUpdateSerielizer(serializers.ModelSerializer):
	class Meta:
		model = Plan 
		fields = ['weekend_date', 'plans']

class ProfileListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name='profile_detail', 
		lookup_field='id',
		lookup_url_kwarg ='profile_id',
		)
	owner = UserSerializer()
	class Meta:
		model = Profile
		fields = '__all__'

class ProfileDetailSerializer(serializers.ModelSerializer):
	update = serializers.HyperlinkedIdentityField(
		view_name='profile_update', 
		lookup_field='id',
		lookup_url_kwarg ='profile_id',
    	)
	owner = UserSerializer()
	class Meta:
		model = Profile
		fields = '__all__'


class ProfileCreateSerielizer(serializers.ModelSerializer):
	class Meta:
		model = Profile  
		fields = ['events', 'plans', 'dob', 'image']

class ProfileUpdateSerielizer(serializers.ModelSerializer):
	class Meta:
		model = Profile 
		fields = ['events', 'plans', 'image']


class FrindListSerielizer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
        view_name='friend_detail', 
        lookup_field='id',
        lookup_url_kwarg ='friend_id',
    	)
	class Meta:
		model = Friends
		fields = ['name', 'logo', 'detail']

class FrindDetailSerielizer(serializers.ModelSerializer):
	delete = serializers.HyperlinkedIdentityField(
        view_name='friend_delete', 
        lookup_field='id',
        lookup_url_kwarg ='friend_id',
    	)
	update = serializers.HyperlinkedIdentityField(
        view_name='friend_update', 
        lookup_field='id',
        lookup_url_kwarg ='friend_id',
    	)
	class Meta:
		model = Friends
		fields = '__all__'

class FrindCreateSerielizer(serializers.ModelSerializer):
	class Meta:
		model = Friends 
		fields = '__all__'

class FriendUpdateSerielizer(serializers.ModelSerializer):
	class Meta:
		model = Friends
		fields = '__all__'























