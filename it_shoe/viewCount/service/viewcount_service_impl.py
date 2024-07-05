from viewCount.repository.viewcount_repository_impl import ViewCountRepositoryImpl
from .viewcount_service import ViewCountService

class ViewCountServiceImpl(ViewCountService):
    def __init__(self):
        self.repository = ViewCountRepositoryImpl()

    def increment_community_view_count(self, communityId):
        return self.repository.increment_community_view_count(communityId)

    def increment_review_view_count(self, reviewId):
        return self.repository.increment_review_view_count(reviewId)
