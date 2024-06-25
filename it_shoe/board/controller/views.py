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
    
    def list(self, request):
        board_list = self.board_service.get_boards()
        serializer = BoardSerializer(board_list, many=True)
        return Response(serializer.data)
    
    def read(self, request, pk=None):
        board = self.board_service.get_board(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)
    
    def modify_board(self, request, pk=None):
        board = self.board_service.get_board(pk)
        serializer = BoardSerializer(board, data=request.data, partial=True)

        if serializer.is_valid():
            updated_board = self.board_service.update_board(pk, serializer.validated_data)
            return Response(BoardSerializer(updated_board).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def remove_board(self, request, pk=None):
        self.board_service.delete_board(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
