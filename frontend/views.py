from django.shortcuts import render

# Create your views here.
def list(r):
	return render (r, 'frontend/list.html')

