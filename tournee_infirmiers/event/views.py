from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def add_need(request):
	return render(request, 'need/add_need.html')
