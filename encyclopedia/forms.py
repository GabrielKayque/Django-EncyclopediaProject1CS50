from django import forms


class EditForm(forms.Form):
    title =  forms.CharField(label=False, max_length=80, widget=forms.TextInput({"placeholder":"Title - Filename"}))
    content = forms.CharField(label=False, widget=forms.Textarea(attrs={'rows': 20, 'cols': 20, "placeholder": "Content Here - Use Markdown Format"}))