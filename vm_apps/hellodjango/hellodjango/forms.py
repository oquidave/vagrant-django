from django.forms import ModelForm

from .models import Post

class PostForm1(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('phone', 'sms_message',)
        form = PostForm1()