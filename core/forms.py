import django.forms as forms

from core.models import Note


class NoteForm(forms.ModelForm):
    """Форма записки"""
    class Meta:
        model = Note
        fields = ["title", "text", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
