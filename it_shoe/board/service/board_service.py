from abc import ABC, abstractmethod


class BoardService(ABC):
    @abstractmethod
    def create_board(self, board):
        pass
    
    @abstractmethod
    def get_board_list(self):
        pass
    
    @abstractmethod
    def get_board(self, board_id):
        pass