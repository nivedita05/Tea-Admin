# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt


from __future__ import unicode_literals
import frappe
import json
from frappe.utils import cstr, flt
from frappe.model.document import Document
from datetime import datetime,timedelta
from frappe import _
from frappe import utils
from frappe.desk.notifications import clear_doctype_notifications
from dateutil.relativedelta import relativedelta

class SalaryforStaff(Document):
	
	def validate(self):
		self.get_basic()
		self.get_hra()
		self.get_da()
		self.get_vda()
		self.get_elf()
		self.get_add_total()

	def get_basic(self):
		get_basic=frappe.db.sql("""select basic from `tabSalary Staff` where emp_name=%s""",(self.emp_name))
		self.basic=get_basic
		return self.basic

	def get_hra(self):
		basic=self.get_basic()
		get_hra=frappe.db.sql("""select hra from `tabSalary Structure` where book_code=%s""",(self.book_code))
		self.hra=round((get_hra[0][0]*int(basic[0][0]))/100,2)
		return self.hra
	
	def get_da(self):
		basic=self.get_basic()
		get_da=frappe.db.sql("""select da from `tabSalary Structure` where book_code=%s""",(self.book_code))
		self.da=round((get_da[0][0]*int(basic[0][0]))/100,2)
		return self.da
	
	def get_vda(self):
		basic=self.get_basic()
		get_vda=frappe.db.sql("""select vda from `tabSalary Structure` where book_code=%s""",(self.book_code))
		self.vda=round((get_vda[0][0]*int(basic[0][0]))/100,2)
		return self.vda
	
	def get_elf(self):
		get_elf=frappe.db.sql("""select elf from `tabSalary Structure` where book_code=%s""",(self.book_code))
		self.elf=get_elf[0][0]
		return self.elf

	def get_add_total(self):
		pass