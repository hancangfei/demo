from django.db import models
from six import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Procuratorate(models.Model):
    ORG_LEVEL = {
        (0, u"区级"),
        (1, u"县级"),
        (2, u"市级"),
        (3, u"省级"),
        (4, u"最高检"),
    }

    org_id = models.CharField(max_length=64,verbose_name="检察院代码")
    org_name = models.CharField(max_length=64, verbose_name="检察院名称")
    org_province = models.CharField(max_length=64, verbose_name="所属省份")
    org_city = models.CharField(max_length=64, verbose_name="所在市")
    org_district = models.CharField(max_length=64, verbose_name="所在区")

    org_address = models.CharField(max_length=128, verbose_name="详细地址")
    org_tel = models.CharField(max_length=64, verbose_name="联系电话")
    org_mail = models.CharField(max_length=64, verbose_name="邮箱")

    org_level = models.SmallIntegerField(choices=ORG_LEVEL, verbose_name="检察院层级")

    class Meta:
        verbose_name = u"检察院信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.org_name


@python_2_unicode_compatible
class Administration(models.Model):
    ADM_LEVEL = {
        (0, u"区级"),
        (1, u"县级"),
        (2, u"市级"),
        (3, u"省级"),
        (4, u"最高检"),
    }

    ADM_TYPE = {
        (0, u"水利"),
        (1, u"土地"),
        (2, u"林业"),
        (3, u"食品"),
        (4, u"税务"),
    }
    adm_id = models.CharField(max_length=64,verbose_name="行政机关代码")
    adm_name = models.CharField(max_length=64, verbose_name="机关名称")
    #adm_type = models.SmallIntegerField(choices=ADM_TYPE, verbose_name="机关类型")
    adm_province = models.CharField(max_length=64, verbose_name="所属省份")
    adm_city = models.CharField(max_length=64, verbose_name="所在市")
    adm_district = models.CharField(max_length=64, verbose_name="所在区")

    adm_location = models.CharField(max_length=128, verbose_name="详细地址")
    adm_tel = models.CharField(max_length=64, verbose_name="联系电话")
    adm_mail = models.CharField(max_length=64, verbose_name="邮箱")

    adm_level = models.SmallIntegerField(choices=ADM_LEVEL, verbose_name="层级")

    class Meta:
        verbose_name = u"行政机关信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.adm_name
