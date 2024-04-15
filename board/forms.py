from django import forms
from .models import Board


class BoardForm(forms.ModelForm): # 유효성 검증은 아직 안한 상태
    class Meta:
        model = Board
        fields = ['title', 'writer', 'content']