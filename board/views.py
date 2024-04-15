from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import Board

class BoardList(generic.ListView):
    model = Board
    ordering = ['-pk'] # object_list = Board.objects.all().order_by()
    
    
from .forms import BoardForm
from django.urls import reverse_lazy

class BoardCreate(generic.CreateView): # 생성하는데 사용, 앱이름/board_form.html로 알아서 템플릿 찾아감
    model = Board 
    form_class = BoardForm 
    #템플릿 찾아가는거 바꾸고 싶다면 template_name 으로 바꾸기
    success_url = reverse_lazy('board:list') # 클래스는 실행되기전에 미리 메모리상에 로딩이 되는데 미리 url을 뽑아낼 수 없으니 얘는 로딩이되면 그 떄 서야 하겠다는 예약같은 함수