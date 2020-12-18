from __future__ import absolute_import
import xadmin

from .models import DocSuggestion,DocPlan,DocReport


@xadmin.sites.register(DocSuggestion)
class DocSuggestionAdmin(object):
    list_display = ['sug_id', "sug_title", "sug_status", "sug_case", "sug_create_time", "sug_last_edit"]
    list_display_links = ("sug_id", "sug_title")
    search_field = ["sug_title"]
    style_fields = {"hosts": "checkbox-inline"}


@xadmin.sites.register(DocPlan)
class DocPlanAdmin(object):
    list_display = ['plan_id', "plan_title", "plan_status", "plan_case", "plan_create_time", "plan_last_edit"]
    list_display_links = ("plan_id", "plan_title")
    search_field = ["plan_title"]
    style_fields = {"hosts": "checkbox-inline"}


@xadmin.sites.register(DocReport)
class DocReportAdmin(object):
    list_display = ['rep_id', "rep_title",  "rep_status", "rep_case", "rep_create_time", "rep_last_edit"]
    list_display_links = ("rep_id", "rep_title")
    search_field = ["rep_title"]
    style_fields = {"hosts": "checkbox-inline"}
