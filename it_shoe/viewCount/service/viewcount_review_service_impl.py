from viewCount.repository.viewcount_review_repository_impl import ViewCountReviewRepositoryImpl
from viewCount.service.viewcount_review_service import ViewCountReviewService


class ViewCountReviewServiceImpl(ViewCountReviewService):
    def __init__(self):
        self.repository = ViewCountReviewRepositoryImpl()

    def increment_review_view_count(self, reviewId):
        return self.repository.increment_review_view_count(reviewId)