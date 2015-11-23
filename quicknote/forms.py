from django import forms

from .models import Notebook

class NoteForm(forms.ModelForm):

	class Meta:
		model = Notebook
		fields = ('note','title',)