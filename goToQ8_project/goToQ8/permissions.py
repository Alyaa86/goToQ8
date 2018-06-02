from rest_framework import permissions


class IsStaff(permissions.BasePermission):
    message = 'You can contact us to be able to add events .. thank you 😄 !!'

    def has_object_permission(self, request, view, obj):
    	if request.user.is_staff:
    		return True
    	else:
    		return False
