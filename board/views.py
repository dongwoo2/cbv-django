from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import Board

class BoardList(generic.ListView):
    model = Board
    ordering = ['-pk']