# blog/forms.py
from django import forms

from blog.models import Blog, Comment


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'display_picture', 'tag', 'image_source', )


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text', )

    def __init__(self, *args, **kwargs):
        super(CommentCreateForm, self).__init__(*args, **kwargs)
        self.fields['comment_text'].label = False
        self.fields['comment_text'].help_text = 'Press enter to post the comment!!'


