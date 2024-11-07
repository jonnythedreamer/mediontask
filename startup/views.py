from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, Profession
from django.core.exceptions import PermissionDenied
from django.utils.dateparse import parse_date

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomUserSerializer
from .serializers import ProfessionSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all() #.order_by('-created_at')
    serializer_class = CustomUserSerializer
    
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def permission_list(request):
   permissions = {'delete': False, 'view': False, 'change': False}
   if request.user.has_perm('startup.view_customuser'): permissions['view'] = True
   if request.user.has_perm('startup.change_customuser'): permissions['change'] = True
   if request.user.has_perm('startup.delete_customuser'): permissions['delete'] = True
   print(request.user, permissions)
   return JsonResponse(permissions, safe=False)


def profession_list(request):
   professions = Profession.objects.all()
   profession_serializer = ProfessionSerializer(professions, many=True)
   return JsonResponse(profession_serializer.data, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
#@permission_classes([IsAuthenticated])
def customuser_list(request):
    if request.method == 'GET':
        print(request.user)
        #if not request.user.has_perm('startup.view_customuser'):  raise PermissionDenied()
        customusers = CustomUser.objects.all()
        
        fired = request.query_params.get('fired', '0')
        not_fired = request.query_params.get('not_fired', '0')
        full_name = request.query_params.get('name', '')
        profession = request.query_params.get('profession', '')
        fired_date = request.query_params.get('fired_date', '')
        
        if fired == '1' and not_fired == '0':
            customusers = customusers.filter(fired=True)
        if not_fired == '1' and fired == '0':
            customusers = customusers.filter(fired=False)
        if not full_name == '':
            customusers = customusers.filter(full_name__icontains=full_name)
        if not profession == '':
            customusers = customusers.filter(profession=profession)
        if not fired_date == '':
            d = parse_date(fired_date)
            customusers = customusers.filter(fired_date__year=d.year)
        
        customuser_serializer = CustomUserSerializer(customusers, many=True)
        return JsonResponse(customuser_serializer.data, safe=False)
        
    elif request.method == 'POST':
        customuser_data = JSONParser().parse(request)
        customuser_serializer = CustomUserSerializer(data=customuser_data)
        if customuser_serializer.is_valid():
            customuser_serializer.save()
            return JsonResponse(customuser_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(customuser_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = CustomUser.objects.all().delete()
        return JsonResponse({'message': '{} Custom Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def customuser_detail(request, pk):
    try: 
        customuser = CustomUser.objects.get(pk=pk) 
    except CustomUser.DoesNotExist: 
        return JsonResponse({'message': 'The Custom User does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        customuser_serializer = CustomUserSerializer(customuser) 
        return JsonResponse(customuser_serializer.data) 
 
    elif request.method == 'PUT': 
        if not request.user.has_perm('startup.change_customuser'):  raise PermissionDenied()   
        customuser_data = JSONParser().parse(request) 
        customuser_data['name'] = customuser.name
        print(customuser_data)
        customuser_serializer = CustomUserSerializer(customuser, data=customuser_data) 
        print(customuser_serializer)
        if customuser_serializer.is_valid(): 
            customuser_serializer.save() 
            return JsonResponse(customuser_serializer.data) 
        return JsonResponse(customuser_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        print(request.user)
        if not request.user.has_perm('startup.delete_customuser'):  raise PermissionDenied()
        customuser.delete() 
        return JsonResponse({'message': 'Custom User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customuser_list_fired(request):
    customusers = CustomUser.objects.filter(fired=True)
        
    if request.method == 'GET': 
        customuser_serializer = CustomUserSerializer(customusers, many=True)
        return JsonResponse(customuser_serializer.data, safe=False)
