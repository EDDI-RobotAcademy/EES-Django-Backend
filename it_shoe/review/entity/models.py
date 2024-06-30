from django.db import models

class Review(models.Model):
    reviewId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False)
    writer = models.CharField(max_length=32, null=False)
    content = models.TextField()
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)
    reviewImage = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=32, null=True)  # 카테고리 추가
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    reviewCount = models.IntegerField(null=True)  # 리뷰 수 추가

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'review'