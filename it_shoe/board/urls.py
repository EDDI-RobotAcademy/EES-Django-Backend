from django.urls import include, path
from rest_framework.routers import DefaultRouter

from board.controller.views import BoardView

router = DefaultRouter()
router.register(r"board", BoardView)

urlpatterns = [
    path("", include(router.urls)),
    path("register", BoardView.as_view({"post": "create"}), name="board-register"),
    path("list/", BoardView.as_view({"get": "list"}), name="board-list"),
    path("read/<int:pk>", BoardView.as_view({"get": "read"}), name="board-read"),
    path(
        "modify/<int:pk>",
        BoardView.as_view({"put": "modity_board"}),
        name="board-modify",
    ),
    path(
        "delete/<int:pk>",
        BoardView.as_view({"delete": "remove_board"}),
        name="board-remove",
    ),
]
