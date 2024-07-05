from community.entity.models import Community
from review.entity.models import Review

from viewCount.entity.community_viewcount import CommunityViewCount
from .viewcount_repository import ViewCountRepository
from ..entity.review_viewcount import ReviewViewCount


class ViewCountRepositoryImpl(ViewCountRepository):
    def increment_community_view_count(self, communityId):
        try:
            community = Community.objects.get(pk=communityId)
            view_count, created = CommunityViewCount.objects.get_or_create(community=community)
            view_count.increment()
            return view_count.count
        except Community.DoesNotExist:
            return None

    def increment_review_view_count(self, reviewId):
        try:
            review = Review.objects.get(pk=reviewId)
            view_count, created = ReviewViewCount.objects.get_or_create(review=review)
            view_count.increment()
            return view_count.count
        except Review.DoesNotExist:
            return None
