from django.db import models

# 书籍信息模型
class BookInfo(models.Model):
    name = models.CharField(max_length=20) #图书名称
    pub_date = models.DateField(null=True) #发布日期
    readcount = models.IntegerField(default=0) #阅读量
    commentcount = models.IntegerField(default=0) #评论量
    isDelete = models.BooleanField(default=False) #逻辑删除

    #元类信息 : 修改表名
    class Meta:
        db_table = 'bookinfo'

# 人物信息模型
class PeopleInfo(models.Model):
    name = models.CharField(max_length=20) #人物姓名
    gender = models.BooleanField(default=True) #人物性别
    description = models.CharField(max_length=20) #人物描述
    isDelete = models.BooleanField(default=False) #逻辑删除
    book = models.ForeignKey(BookInfo) # 外键约束，人物属于哪本书

    # 元类信息 : 修改表名
    class Meta:
        db_table = 'peopleinfo'