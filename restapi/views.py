from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import todoSerializer
from .models import todo
# Create your views here.


@api_view(['GET'])
def to_do(r):

	api_rl={
		'list':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/'
		}
	# return Response('API BASE',safe=False)
	return Response(api_rl)

@api_view(['GET'])
def tklist(r):
	tasks=todo.objects.all().order_by('-id')
	szr=todoSerializer(tasks, many=True)
	return Response(szr.data)

@api_view(['GET'])
def tkdetail(r,pk):
	tasks=todo.objects.get(id=pk)
	szr=todoSerializer(tasks, many=False)
	return Response(szr.data)

@api_view(['POST'])
def tkcreate(r):
	szr=todoSerializer(data=r.data)
	if szr.is_valid():
		szr.save()
	return Response(szr.data)

@api_view(['POST'])
def tkupdate(r,pk):
	tasks=todo.objects.get(id=pk)
	szr=todoSerializer(instance=tasks,data=r.data)
	if szr.is_valid():
		szr.save()
	return Response(szr.data)

@api_view(['DELETE'])
def tkdelete(r,pk):
	tasks=todo.objects.get(id=pk)
	# szr=todoSerializer(instance=tasks,data=r.data)
	# if szr.is_valid():
	# 	szr.delete()
	tasks.delete()
	return Response('Item deleted')