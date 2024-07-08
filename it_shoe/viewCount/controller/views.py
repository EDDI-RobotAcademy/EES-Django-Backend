from rest_framework import viewsets
from rest_framework.response import Response

from viewCount.service.viewcount_community_service_impl import ViewCountCommunityServiceImpl
from viewCount.service.viewcount_review_service_impl import ViewCountReviewServiceImpl
from viewCount.service.viewcount_product_service_impl import ViewCountProductServiceImpl

view_count_community_service = ViewCountCommunityServiceImpl()
view_count_review_service = ViewCountReviewServiceImpl()
view_count_product_service = ViewCountProductServiceImpl()

class ViewCountView(viewsets.ViewSet):

    def increment_community(self, request, pk=None):
        new_view_count = view_count_community_service.increment_community_view_count(pk)
        if new_view_count is not None:
            return Response({'status': 'success', 'viewCount': new_view_count})
        else:
            return Response({'status': 'error', 'message': 'Community not found'}, status=404)

    def increment_review(self, request, pk=None):
        new_view_count = view_count_review_service.increment_review_view_count(pk)
        if new_view_count is not None:
            return Response({'status': 'success', 'viewCount': new_view_count})
        else:
            return Response({'status': 'error', 'message': 'Community not found'}, status=404)

    def increment_product(self, request, pk=None):
        new_view_count = view_count_product_service.increment_product_view_count(pk)
        if new_view_count is not None:
            return Response({'status': 'success', 'viewCount': new_view_count})
        else:
            return Response({'status': 'error', 'message': 'Community not found'}, status=404)