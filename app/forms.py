from django import forms
from app.models import Comments,Subscribe
from django.utils.translation import gettext_lazy as _



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {'content','email','name','website'}
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
                'placeholder': 'Type your comment...',
            })
        self.fields['email'].widget.attrs.update({
                'placeholder': 'Email',
            })
        self.fields['name'].widget.attrs.update({
                'placeholder': 'Name',
            })
        self.fields['website'].widget.attrs.update({
                'placeholder': 'Website',
            })
        
class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {'email':_('')}
    
    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
                'placeholder': 'example@example.com',
            })



