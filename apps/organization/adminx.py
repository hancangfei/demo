from __future__ import absolute_import
import xadmin

from .models import Procuratorate, Administration


@xadmin.sites.register(Procuratorate)
class ProcuratorateAdmin(object):
    list_display = {"org_name", "org_address", "org_tel", "org_mail", "org_level"}
    list_display_links = ("org_name",)
    search_field = ["org_name", "org_address"]
    style_fields = {"hosts": "checkbox-inline"}


@xadmin.sites.register(Administration)
class Administration(object):
    list_display = {"adm_name", "adm_location", "adm_tel", "adm_mail", "adm_level"}
    list_display_links = ("adm_name",)
    search_field = ["adm_name", "adm_location"]
    style_fields = {"hosts": "checkbox-inline"}

