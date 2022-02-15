from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headline'].widget.attrs.update({'placeholder':'Type here...'})
        self.fields['tagline'].widget.attrs.update({'placeholder':'Type here...'})        
        self.fields['content'].widget.attrs.update({'placeholder':'Type here...'})
    class Meta:
        model = Post
        fields = [
            'headline',
            'tagline',
            'content',
        ]