from rest_framework import serializers
from .models import *
from category.serializers import CategorySerializer

class PostSerializer (serializers.ModelSerializer) :
    id_category = CategorySerializer (read_only=True)
    class Meta :
        model = post
        fields = ['id_post','id_category','title','content','created_at']
        # fields = "__all__"
