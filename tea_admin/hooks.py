# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "tea_admin"
app_title = "Tea Admin"
app_publisher = "Frappe"
app_description = "to manage the details of tea admin work"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tea_admin/css/tea_admin.css"
# app_include_js = "/assets/tea_admin/js/tea_admin.js"

# include js, css files in header of web template
# web_include_css = "/assets/tea_admin/css/tea_admin.css"
# web_include_js = "/assets/tea_admin/js/tea_admin.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "tea_admin.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "tea_admin.install.before_install"
# after_install = "tea_admin.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tea_admin.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tea_admin.tasks.all"
# 	],
# 	"daily": [
# 		"tea_admin.tasks.daily"
# 	],
# 	"hourly": [
# 		"tea_admin.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tea_admin.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tea_admin.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "tea_admin.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tea_admin.event.get_events"
# }

