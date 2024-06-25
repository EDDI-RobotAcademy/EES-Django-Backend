from board.repository.board_repository_impl import BoardRepositoryImpl
from board.service.board_service import BoardService


class BoardServiceImpl(BoardService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__board_repository = BoardRepositoryImpl.get_instance()

        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create_board(self, board):
        return self.board_repository.create_board(board)
    
    def get_board_list(self):
        return self.board_repository.get_boards()
    
    def get_board(self, board_id):
        return self.board_repository.get_board(board_id)
