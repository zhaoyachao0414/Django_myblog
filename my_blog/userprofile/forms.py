# 引入表单类
from django import forms
# 引入 User 模型
from django.contrib.auth.models import User

# 登录表单，继承了 forms.Form 类
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class UserRegisterForm(foms.ModelForm):
	"""docstring for UserRegisterForm"foms.ModelFormf __init__(self, arg):
		super(UserRegisterForm,foms.ModelForm.__init__()
		self.arg = arg
		