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
        print(f"list() -> Review", Review)
        print(f"list() -> Review.objects", Review.objects)
        print(f"list() -> Review.objects.all()", Review.objects.all())

        reviewList = Review.objects.all()
        for review in reviewList:
            print(f"Review: {review}")

        return Review.objects.all().order_by('regDate')

    def create(self, reviewData):
        review = Review(**reviewData)
        review.save()
        return review

    def findByReviewId(self, reviewId):
        return Review.objects.get(reviewId=reviewId)

