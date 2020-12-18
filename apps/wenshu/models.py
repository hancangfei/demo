from django.db import models
from six import python_2_unicode_compatible
from django.conf import settings
from apps.cases.models import Case

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
# Create your models here.
DOC_STATUS = (
    (0, u"创建"),
    (1, u"保存"),
    (2, u"审核"),
    (3, u"发送"),
    (4, u"回复"),
    (5, u"归档")
)


@python_2_unicode_compatible
class DocSuggestion(models.Model):

    sug_id = models.CharField(max_length=64, verbose_name="文书号")
    sug_title = models.CharField(max_length=128, verbose_name="文书标题")
    sug_content = models.TextField(verbose_name="文书内容")
    sug_status = models.SmallIntegerField(choices=DOC_STATUS, verbose_name="文书状态")
    sug_case = models.ForeignKey(Case, on_delete=models.CASCADE, verbose_name="文书所属案件", related_name="sugs")

    sug_create_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="创建者", related_name="sug_creator")
    sug_create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    sug_last_edit = models.DateTimeField(auto_now=True, verbose_name="最近一次修改时间")
    sug_last_edit_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="最近一次修改者", related_name="sug_editor")

    sug_edit_times = models.IntegerField(default=1, verbose_name="编辑次数")

    sug_reply_content= models.TextField(verbose_name="评价意见")
    sug_reply_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="评价人", related_name="sug_reply")
    sug_reply_time = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.sug_title

    class Meta:
        verbose_name = "检察建议信息"
        verbose_name_plural = verbose_name


class DocPlan(models.Model):
    plan_id = models.CharField(max_length=64, verbose_name="文书号")
    plan_title = models.CharField(max_length=128, verbose_name="文书标题")
    plan_content = models.TextField(verbose_name="文书内容")
    plan_status = models.SmallIntegerField(choices=DOC_STATUS, verbose_name="文书状态")
    plan_case = models.ForeignKey(Case, on_delete=models.CASCADE, verbose_name="文书所属案件", related_name="plans")

    plan_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="创建者",
                                    related_name="plan_creator")
    plan_create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    plan_last_edit = models.DateTimeField(auto_now=True, verbose_name="最近一次修改时间")
    plan_edit_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="最近一次修改者",
                                       related_name="plan_editor")

    plan_edit_times = models.IntegerField(default=1, verbose_name="编辑次数")
    plan_reply_content = models.TextField(verbose_name="评价意见")
    plan_reply_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="评价人", related_name="plan_reply")
    plan_reply_time = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.plan_title

    class Meta:
        verbose_name = u'整改计划文书'
        verbose_name_plural = verbose_name


class DocReport(models.Model):
    rep_id = models.CharField(max_length=64, verbose_name="文书号")
    rep_title = models.CharField(max_length=128, verbose_name="文书标题")
    rep_content = models.TextField(verbose_name="文书内容")
    rep_status = models.SmallIntegerField(choices=DOC_STATUS, verbose_name="文书状态")
    rep_case = models.ForeignKey(Case, on_delete=models.CASCADE, verbose_name="文书所属案件", related_name="reports")

    rep_create_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="创建者",
                                    related_name="rep_creator")
    rep_create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    rep_last_edit = models.DateTimeField(auto_now=True, verbose_name="最近一次修改时间")
    rep_last_edit_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="最近一次修改者",
                                       related_name="rep_editor")

    rep_edit_times = models.IntegerField(default=1, verbose_name="编辑次数")
    rep_reply_content = models.TextField(verbose_name="评价意见")
    rep_reply_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="评价人", related_name="rep_reply")
    rep_reply_time = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.rep_title

    class Meta:
        verbose_name = u'整改报告文书'
        verbose_name_plural = verbose_name


'''
class DocAssess(models.Model):
    doc_id = models.CharField(max_length=64, verbose_name="文书号")
    doc_title = models.CharField(max_length=128, verbose_name="文书标题")
    doc_content = models.TextField(verbose_name="文书内容")
    doc_status = models.SmallIntegerField(choices=DOC_STATUS, verbose_name="文书状态")
    doc_case = models.ForeignKey(Case, on_delete=models.CASCADE, verbose_name="文书所属案件", related_name="docs")
    
    create_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="创建者",
                                    related_name="creator")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    last_edit = models.DateTimeField(auto_now=True, verbose_name="最近一次修改时间")
    last_edit_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="最近一次修改者",
                                       related_name="editor")

    edit_times = models.IntegerField(default=1, verbose_name="编辑次数")

    def __str__(self):
        return self.doc_title
    
    class Meta:
        verbose_name = u'评价文书'
        verbose_name_plural = verbose_name
'''