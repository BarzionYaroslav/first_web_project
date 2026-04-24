from django import forms
from .models import Book

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
        fields = ['name', 'description', 'price', 'stock']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control"}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }