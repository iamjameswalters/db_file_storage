# django
from django import forms
# third party
from db_file_storage.form_widgets import DBClearableFileInput, \
    DBAdminClearableFileInput
# project
from .models import Book, SoundDevice


class BookForm(forms.ModelForm):
    class Meta(object):
        model = Book
        exclude = []
        widgets = {
            'index': DBClearableFileInput,
            'pages': DBClearableFileInput,
            'cover': DBClearableFileInput,
        }


class BookAdminForm(forms.ModelForm):
    class Meta(object):
        model = Book
        exclude = []
        widgets = {
            'index': DBAdminClearableFileInput,
            'pages': DBAdminClearableFileInput,
            'cover': DBAdminClearableFileInput,
        }


class SoundDeviceForm(forms.ModelForm):
    class Meta(object):
        model = SoundDevice
        exclude = []
