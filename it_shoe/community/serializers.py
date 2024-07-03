from rest_framework import serializers

from community.entity.models import Community


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다
class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['communityId', 'title', 'writer', 'content', 'regDate', 'updDate']
        read_only_fields = ['regDate', 'updDate']
