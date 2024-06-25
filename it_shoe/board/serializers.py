from board.entity.models import Board
from rest_framework import serializers


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ["board_id", "title", "writer", "content", "register_date", "update_date"]
        read_only_fields = ["regDate", "updDate"]
