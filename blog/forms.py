from django import forms
from .models import Post, Comment


# with these codes we add a post easily because we just import the form from django and only thins we add is what to add in the form page
class PostForm(forms.ModelForm):
    
    class Meta: 
        model = Post
        fields = ('title', 'text',)
        
        
        
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)