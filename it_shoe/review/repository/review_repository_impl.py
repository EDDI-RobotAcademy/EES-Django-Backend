import os
from review.entity.models import Review
from review.repository.review_repository import ReviewRepository


class ReviewRepositoryImpl(ReviewRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return Review.objects.all().order_by('regDate')

    def create(self, title, writer, content, rating, reviewImage):
        uploadDirectory = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../../../../EES-Vue-Frontend/src/assets/images/reviewImages')
        )
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, reviewImage.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in reviewImage.chunks():
                destination.write(chunk)

        review = Review(
            title=title,
            writer=writer,
            content=content,
            rating=rating,
            reviewImage=reviewImage.name
        )
        review.save()
        return review

    def findByReviewId(self, reviewId):
        try:
            return Review.objects.get(reviewId=reviewId)
        except Review.DoesNotExist:
            return None
