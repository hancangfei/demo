from django.db import models
from six import python_2_unicode_compatible
from apps.organization.models import Procuratorate,Administration

# Create your models here.


class Case(models.Model):
    CASE_STATUS = (
        (0, u"立案"),
        (1, u"检察建议阶段"),
        (2, u"整改计划阶段"),
        (3, u"整改报告阶段"),
        (4, u"评估阶段"),
        (5, u"办理完毕")
    )
    CASE_DECISION = (
        (0, u"起诉"),
        (1, u"不起诉")
    )
    case_id = models.CharField(max_length=64, verbose_name="案件编号")
    case_title = models.CharField(max_length=128, verbose_name="案件标题")
    case_description = models.TextField(verbose_name="案情描述")
    case_status = models.SmallIntegerField(choices=CASE_STATUS, verbose_name="办理状态", default=0)
    case_type = models.CharField(max_length=64, verbose_name="案件类别")
    case_subject = models.ForeignKey(Procuratorate, on_delete=models.CASCADE, verbose_name='办案机构', related_name='subject')
    case_object = models.ManyToManyField(Administration,verbose_name="涉案机构", related_name='object')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="立案时间")
    finish_time = models.DateTimeField(blank=True, null=True, verbose_name="结案时间")

    case_decision = models.SmallIntegerField(choices=CASE_DECISION, null=True, blank=True, verbose_name="处理决定")

    def __str__(self):
        return self.case_title

    class Meta:
        verbose_name = "案件信息"
        verbose_name_plural = verbose_name

