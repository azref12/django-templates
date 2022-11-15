from rest_framework import serializers
from .models import *

class PostSerializer (serializers.ModelSerializer) :
    
    class Meta :
        model = post
        fields = ['id_post','title','content']
        # fields = "__all__"