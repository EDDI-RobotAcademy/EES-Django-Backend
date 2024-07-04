from community.entity.models import Community
from viewCount.entity.community_viewcount import CommunityViewCount
from .viewcount_repository import ViewCountRepository

class ViewCountRepositoryImpl(ViewCountRepository):
    def increment_view_count(self, community_id):
        try:
            community = Community.objects.get(pk=community_id)
            view_count, created = CommunityViewCount.objects.get_or_create(community=community)
            view_count.increment()
            return view_count.count
        except Community.DoesNotExist:
            return None
