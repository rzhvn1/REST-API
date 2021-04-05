from .models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Comment
        fields = ['id', 'text', 'date_created', 'meal', 'profile']


class CommentHardSerializer(serializers.Serializer):

    text = serializers.CharField(min_length=1, required=True)


