from django import forms
from .models import Comment,Post
from ckeditor.widgets import CKEditorWidget
class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    to=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder':'To'}))
    comment=forms.CharField(required=False,widget=forms.Textarea(attrs={'placeholder':'Comment','rows':3}))

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['body']
        widgets={'body':forms.Textarea(attrs={'rows':1,'placeholder':'Comment'})}

class SearchForm(forms.Form):
    query=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Search'}))


class PostForm(forms.ModelForm):
    body=forms.CharField(widget=CKEditorWidget(attrs={'cols':90}))
    class Meta:
        model=Post
        fields=['tags','title','slug','body','image']
        