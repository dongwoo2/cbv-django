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
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["button_label"] = '등록'
        return context
    
    
class BoardDetail(generic.DetailView):
    model = Board
    
    # 조회수 증가 기능 적용
    def get_object(self): # 재정의
        item = super().get_object()
        item.increment_read_count()
        return item
        
from django.shortcuts import reverse        
from .forms import BoardUpdateForm

class BoardUpdate(generic.UpdateView):
    model = Board
    form_class = BoardUpdateForm
    # success_url = reverse_lazy('board:list') # 수정 후 목록으로 리다이렉트 응답
    
    def get_success_url(self): # 재정의 
        return reverse('board:detail', args=(self.object.id, ))
    
    def get_context_data(self, **kwargs: any) -> dict[str, any]: # > dict[str, any] 는 반환자료형이 무엇인지 명시해주는 것 글등록에 있는 함수처럼 없어도 무관함
            context = super().get_context_data(**kwargs)
            context["button_label"] = '수정'
            return context
        
        
class BoardDelete(generic.DeleteView):
    model = Board
    success_url = reverse_lazy('board:list')
        