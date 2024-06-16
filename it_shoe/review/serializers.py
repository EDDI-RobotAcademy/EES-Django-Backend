from rest_framework import serializers

from review.entity.models import Review


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['reviewId', 'title', 'writer', 'content', 'regDate', 'updDate']
        read_only_fields = ['regDate', 'updDate']