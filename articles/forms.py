# articles/forms.py
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    # Явно задаем виджеты с id
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_title',
            'placeholder': 'Введите заголовок статьи'
        }),
        label='Заголовок'
    )

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'id_content',
            'rows': 10,
            'placeholder': 'Введите содержание статьи'
        }),
        label='Содержание'
    )