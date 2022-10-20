from django.shortcuts import render
from flight_management.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, "crud.html")

class UserListView(generic.ListView):
    model = User
    paginate_by = 10

class UserDetailView(generic.DetailView):
    model = User

class UserCreate(CreateView):
    model = User
    fields = ['tx_name','nm_role','tx_username','tx_hash_key']

class UserUpdate(UpdateView):
    model = User
    fields = ['tx_name','nm_role','tx_hash_key']

class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('users')




from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from flight_management.serializer import UserSerializer
from rest_framework.decorators import api_view
@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        
        username = request.GET.get('tx_username', None)
        if username is not None:
            users = users.filter(title__icontains=username)
        
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)