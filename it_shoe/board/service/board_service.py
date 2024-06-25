from abc import ABC, abstractmethod


class BoardService(ABC):
    @abstractmethod
    def create_board(self, board):
        pass