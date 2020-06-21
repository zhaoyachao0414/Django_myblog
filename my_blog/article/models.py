from django.db import models
#导入内建的User模型
from django.contrib.auth.models import User
#timezone用于处理时间相关事务
from django.utils import timezone

#博客文章数据模型
class ArticlePost(models.Model):
	#文章作者 参数on_delete用于指定数据删除的方式
	author = models.ForeignKey(User,on_delete=models.CASCADE)

	#文章标题 models.charfied为字符串字段，用于保存较短的字符串，比如标题
	title = models.CharField(max_length=100)

	#文章正文 保存大量文本使用TextField
	body = models.TextField()

	#文章创建时间 参数default=timezone.now指定其在创建数据时将默认写入当前的时间
	created = models.DateTimeField(default=timezone.now)

	#文章更新时间  参数auto_now= true 指定每次数据更新时自动写入当前时间
	updated = models.DateTimeField(auto_now=True)


	#内部类class Meta用于给model定义元数据
	class Meta:
		#ordering指定模型返回的数据的排列顺序 '-created'表明数据应以倒序排列
		ordering = ('-created',)

	#函数_str_定义当调用对象的str()方法时的返回值内容
	def _str_(self):
		return self.title 	#返回文章标题	

# Create your models here.
