from viewCount.repository.viewcount_repository_impl import ViewCountRepositoryImpl
from .viewcount_service import ViewCountService

class ViewCountServiceImpl(ViewCountService):
    def __init__(self):
        self.repository = ViewCountRepositoryImpl()

    def increment_view_count(self, community_id):
        return self.repository.increment_view_count(community_id)
