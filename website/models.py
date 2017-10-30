from django.db import models
from django.utils import timezone


# 게시글 번호(정의하지 않으면 자동적으로 생성 ), 제목, 내용, 저자, 날짜, 조회수
class Board(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
