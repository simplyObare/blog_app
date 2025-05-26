from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
        labels = {
            "body": "Comment",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input w-full", "placeholder": "Your name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "input w-full", "placeholder": "Your email"}
            ),
            "body": forms.Textarea(
                attrs={"class": "textarea h-24 w-full", "placeholder": "Your comment"}
            ),
        }
