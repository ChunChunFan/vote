# 小型的投票系统

## 命令

1. 创建一个项目
```
django-admin.py startproject wardrobe 
```
1. 启动项目
```
python3 manage.py runserver 8080 
```
1. 创建一个app
```
python3 manage.py startapp polls 
```
1. 让 Django 知道我们在我们的模型有一些变更
```
python3 manage.py makemigrations TestModel
```
1. 储存在 polls/migrations/0001_initial.py
```
python3 manage.py sqlmigrate polls 0001
```
1. 创建表结构
```
python3 manage.py migrate TestModel
```
1. 创建超级用户
```
python3 manage.py createsuperuser
```
1. 控制台
```
python3 manage.py shell
```

## 功能介绍

1. 使用了django的admin后台管理
1. 简单的更改了管理页面的名称
1. 后台管理的列表页的筛选 过滤器、添加页面的嵌套
1. app内自己的样式以及路由(命名空间)
1. get_object_or_404的使用
1. 锁的使用
```
selected_choice.votes = F('votes') + 1  
```
1. HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 跳转
1. 页面的路由
```html
<a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a>
```
