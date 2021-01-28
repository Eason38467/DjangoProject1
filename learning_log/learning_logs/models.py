from django.db import models

# Create your models here.

class Topic(models.Model):
    """用户学习的主题"""

    text = models.CharField(max_length=200)
    data_added= models.DateField(auto_created=True)

    def __str__(self):
        """返回模型的字符串"""

        return self.text


class Entry(models.Model):
    """学到的某个主题的具体知识"""
    #这里和书里的描写不太一样，可能是我用的新版的缘故， ForeignKey 必须要on_delete参数
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)

    text = models.TextField()
    date_added = models.DateField(auto_created=True)

    class Mera:
        verbose_name_plural = 'entries'

    def __str__(self):

        return self.text[:50] + '...'