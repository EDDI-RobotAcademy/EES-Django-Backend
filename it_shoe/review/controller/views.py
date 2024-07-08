from rest_framework import viewsets, status
from rest_framework.response import Response

from review.entity.models import Review
from review.serializers import ReviewSerializer
from review.service.review_service_impl import ReviewServiceImpl
from viewCount.controller.views import view_count_review_service


class ReviewView(viewsets.ViewSet):
    queryset = Review.objects.all()
    reviewService = ReviewServiceImpl.getInstance()

    def list(self, request):
        reviewList = self.reviewService.list()
        serializer = ReviewSerializer(reviewList, many=True)
        return Response(serializer.data)

    def register(self, request):
        try:
            data = request.data

            reviewImage = request.FILES.get('reviewImage')
            title = data.get('title')
            writer = data.get('writer')
            content = data.get('content')
            rating = data.get('rating')

            if not all([reviewImage, title, writer, rating, content]):
                return Response({'error': '모든 내용을 채워주세요!'},
                                status=status.HTTP_400_BAD_REQUEST)

            review = self.reviewService.createReview(title, writer, content, rating, reviewImage)
            serializer = ReviewSerializer(review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            print('리뷰 등록 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def read(self, request, pk=None):
        view_count_review_service.increment_review_view_count(pk)
        review = self.reviewService.readReview(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)