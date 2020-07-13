from django.contrib import admin
from .models import Choice, Question

# admin.StackedInline 按照行的展示  TabularInline 按照表格的展示
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2  # 默认创建几个关联

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    # 字段分类展示
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('时间说明', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # 外键的展示
    inlines = [ChoiceInline]
    # 列表展示的列
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 侧边栏过滤器
    list_filter = ['pub_date']
    # 列表筛选
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
