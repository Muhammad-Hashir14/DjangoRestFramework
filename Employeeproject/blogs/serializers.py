from rest_framework import serializers
from .models import Comments, Blogs

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comments
        fields = "__all__"

class BlogsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Blogs
        fields = "__all__"
        
