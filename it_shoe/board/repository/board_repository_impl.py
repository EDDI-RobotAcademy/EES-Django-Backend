from board.entity.models import Board
from board.repository.board_repository import BoardRepository


class BoardRepositoryImpl(BoardRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create_board(self, board):
        return Board.objects.create(
            title=board.title, writer=board.writer, content=board.content
        )

    def get_board_list(self):
        return Board.objects.all()

    def get_board(self, board_id):
        return Board.objects.get(id=board_id)

    def update_board(self, board):
        target_board = Board.objects.get(board_id=board.board_id)
        target_board.title = board.title
        target_board.writer = board.writer
        target_board.content = board.content
        target_board.save()

    def delete_board(self, board_id):
        Board.objects.get(board_id=board_id).delete()
