from board.serializers import BoardSerializer
from board.service.board_service_impl import BoardServiceImpl
from rest_framework import status, viewsets
from rest_framework.response import Response


class BoardView(viewsets.ViewSet):
    board_service = BoardServiceImpl.get_instance()

    def create(self, request):
        serializer = BoardSerializer(data=request.data)

        if serializer.is_valid():
            board = self.board_service.create_board(serializer.validated_data)
            return Response(BoardSerializer(board).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
