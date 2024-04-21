from django import forms
from .models import Board


class BoardForm(forms.ModelForm): # 유효성 검증은 아직 안한 상태
    class Meta:
        model = Board
        fields = ['title', 'writer', 'content']
        
        
        
class BoardUpdateForm(forms.ModelForm): 
    class Meta:
        model = Board
        fields = ['title', 'writer', 'content']
        
    writer = forms.CharField(disabled=True) # writer 인풋폼은 수정 불가하게 이것도 재정의 한 것
    
    
class BoardSearchForm(forms.Form):
    keyword = forms.CharField(label="키워드:", required=True) # 인풋폼에 문자열 받을 수 있게 charField 설정