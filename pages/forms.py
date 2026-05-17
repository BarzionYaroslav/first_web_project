from django import forms
from .models import Book, Comment
from django.contrib.auth.forms import UserCreationForm
from typing import Any

class FeedbackForm(forms.Form):
    subject = forms.CharField(
        label='Why did you contact us?', 
        max_length=256,
        widget=forms.TextInput(attrs={"placeholder":"John Contacter", "class": "form-control"})
        )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={"placeholder":"name@example.com", "class": "form-control"})
        )
    message = forms.CharField(
        label='Message', 
        widget=forms.Textarea(attrs={"placeholder":"Place your message here", "class": "form-control"})
        )
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'price', 'stock', 'image', 'tags']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control"}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={"class": "form-control"}),
            'tags': forms.SelectMultiple(attrs={"class": "form-control"}),
        }

class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }