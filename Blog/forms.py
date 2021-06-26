from django import forms
from .models import *
class CommentForm(forms.ModelForm):
    # author_email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'enter your email'}))
    comment_content=forms.CharField(label='',widget=forms.TextInput(attrs={'rows':"3",'placeholder':'write comment or reply .....','cols':'5'}))
    class Meta:
        model=comment
        fields='__all__'
        exclude=['comment_author','comment_blog','current_city','author_email','comment_reply']