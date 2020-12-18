from __future__ import absolute_import
import xadmin

from .models import Case

@xadmin.sites.register(Case)
class CaseAdmin(object):
    list_display = {"case_id", "case_title", "case_type", "case_status", "case_subject", "create_time", "finish_time", "case_decision"}
    list_display_links = ("case_id", "case_title")
    search_field = ["case_title", "case_description"]
    style_fields = {"hosts": "checkbox-inline"}