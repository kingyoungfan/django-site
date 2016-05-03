# coding=utf-8
import datetime
from django.db import models


# Create your models here.
# 模型，每个模型用一个类标示
from django.utils import timezone


class Question(models.Model):
    def __str__(self):  # __unicode__ on Python 2
        return self.question_text
    # 第一个参数：字段的自述名
    question_text = models.CharField('问题', max_length=200)
    pub_date = models.DateTimeField('发布时间')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    def __str__(self):  # __unicode__ on Python 2
        return self.choice_text

    class Meta:
        proxy = True

    question = models.ForeignKey(Question, verbose_name='问题')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
