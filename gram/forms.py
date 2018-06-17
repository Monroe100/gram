from django.contrib.auth.forms import AuthenticationForm
from .models import Image, Comment, Profile
from django import forms


class ProfileForm(forms.ModelForm):
    '''
    classs that creates a profile update form
    '''
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio', 'user']


# class ImagePostForm(forms.ModelForm):
#     '''
#     Class to create a new post
#     '''
#     class Meta:
#         model = Image
#         fields = ['image', 'image_name', 'image_caption']


# class CommentForm(forms.ModelForm):
#     '''
#     class that creates the comment form
#     '''
#     class Meta:
#         model = Comment
#         fields = ['comment']

# class CreateProfileForm(forms.ModelForm):
#     '''
#     classs that creates a profile update form
#     '''
#     class Meta:
#         model = Profile
#         fields = ['profile_photo', 'bio', 'user']