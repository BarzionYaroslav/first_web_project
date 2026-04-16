from django import forms

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