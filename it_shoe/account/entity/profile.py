from django.db import models

from account.entity.account import Account


class Profile(models.Model):
    nickname = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=64, unique=True)
    gender = models.CharField(max_length=64)    # 성별 필드 추가
    birthyear = models.IntegerField()           # 생년월일 필드 추가
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile -> email: {self.email}, nickname: {self.nickname}"

    class Meta:
        db_table = 'profile'
        app_label = 'account'