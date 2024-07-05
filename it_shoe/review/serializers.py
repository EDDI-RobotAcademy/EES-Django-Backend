from rest_framework import serializers
from review.entity.models import Review
from viewCount.entity.review_viewcount import ReviewViewCount


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다
class ReviewSerializer(serializers.ModelSerializer):
    viewCount = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['reviewId', 'title', 'writer', 'content','reviewImage','rating', 'regDate', 'updDate', 'viewCount']
        read_only_fields = ['regDate', 'updDate', 'viewCount']

    def get_viewCount(self, obj):
        try:
            return obj.view_count.count
        except ReviewViewCount.DoesNotExist:
            return 0