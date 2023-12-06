from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

def home(request):
    return render(request,'home.html')

# --API views --
class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [IsAdminUser]

class ExecutiveViewSet(viewsets.ModelViewSet):
    queryset = Executive.objects.all()
    serializer_class = ExecutiveSerializer
    permission_classes = [IsAdminUser]

#-- view for users to have the function to view their permissions --

# @login_required
# def view_user_permissions(request,id):
#     user = User.objects.get(id=id)
#     # to check whether the user is manager or executive
#     if user.is_manager:
#         permissions = user.get_all_permissions()
#         context = {
#             'permissions':permissions
#         }
#         return render(request,'view_user_permissions.html',context)        
#     elif user.is_executive:
#         permissions = user.get_all_permissions()
#         context = {
#             'permissions': permissions
#         }
#         return render(request,'view_user_permissions.html',context)        


