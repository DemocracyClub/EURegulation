from django import forms

class SearchByDocumentForm(forms.Form):
    document_text = forms.CharField(widget=forms.Textarea)
