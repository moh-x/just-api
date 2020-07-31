from rest_framework import serializers
from .models import Post
#from django import forms


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = (
#             'title',
#             'description',
#         )

# The serializers model follows the same syntax as a forms model

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'owner',
        )
