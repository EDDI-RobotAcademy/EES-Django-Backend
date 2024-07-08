from review.entity.models import Review
from viewCount.entity.review_viewcount import ReviewViewCount
from viewCount.repository.viewcount_review_repository import ViewCountReviewRepository


class ViewCountReviewRepositoryImpl(ViewCountReviewRepository):

    def increment_review_view_count(self, reviewId):
        try:
            review = Review.objects.get(pk=reviewId)
            view_count, created = ReviewViewCount.objects.get_or_create(review=review)
            view_count.increment()
            return view_count.count
        except Review.DoesNotExist:
            return None