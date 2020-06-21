#引入表单类
from django import forms
#引入文章中模型
from .models import ArticlePost

#写文章的表单类
class ArticlePostForm(forms.ModelForm):
	class Meta:
		#知名数据模型来源
		model=ArticlePost
		fields = ('title','body')






