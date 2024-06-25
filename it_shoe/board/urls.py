from board.controller.views import BoardView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"board", BoardView)

urlpatterns = [
    path("", include(router.urls)),
    path("register", BoardView.as_view({"post": "create"}), name="board-register"),
]
