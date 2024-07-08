from django.db import models
from django.utils import timezone
from account.entity.account import Account
from account.entity.profile_gender_type import ProfileGenderType


class Profile(models.Model):
    nickname = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=64, unique=True)
    gender = models.ForeignKey(ProfileGenderType, on_delete=models.CASCADE)   # 성별 필드 추가
    birthyear = models.IntegerField()           # 생년월일 필드 추가
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # 최초 등록일자 필드 추가
    last_login = models.DateTimeField(auto_now=True)      # 최근 접속시간 필드 추가

    def save(self, *args, **kwargs):
        if not self.pk:  # 객체가 처음 생성될 때
            self.created_at = timezone.now() + timedelta(hours=9)
        self.last_login = timezone.now() + timedelta(hours=9)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Profile -> email: {self.email}, nickname: {self.nickname}"

    class Meta:
        db_table = 'profile'
        app_label = 'account'
