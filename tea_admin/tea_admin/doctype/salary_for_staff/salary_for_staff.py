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
		self.get_hra()
		self.get_vda()
		self.get_da()
		self.get_elf()
		self.get_salary()



	def get_hra(self):
		get_hra=frappe.db.sql("""select hra from `tabSalary Structure` where book_code=%s""",(self.book_code))
		self.hra=(get_hra[0][0]*int(self.basic))/100

	def get_vda(self):
		get_vda=frappe.db.sql("""select vda from `tabSalary Structure` where book_code=%s""",(self.book_code))
		self.vda=(get_vda[0][0]*int(self.basic))/100

	def get_da(self):
		get_da=frappe.db.sql("""select da from `tabSalary Structure` where book_code=%s""",(self.book_code))
		self.da=(get_da[0][0]*int(self.basic))/100

	def get_elf(self):
		get_elf=frappe.db.sql("""select elf from `tabSalary Structure` where book_code=%s""",(self.book_code))
		self.alw=get_elf[0][0]

	def get_salary(self):
		get_hra=frappe.db.sql("""select hra from `tabSalary Structure` where book_code=%s""",(self.book_code))
		get_vda=frappe.db.sql("""select vda from `tabSalary Structure` where book_code=%s""",(self.book_code))
		get_da=frappe.db.sql("""select da from `tabSalary Structure` where book_code=%s""",(self.book_code))
		get_elf=frappe.db.sql("""select elf from `tabSalary Structure` where book_code=%s""",(self.book_code))

		self.salary=int(self.basic)+(get_hra[0][0]*int(self.basic))/100+(get_vda[0][0]*int(self.basic))/100+(get_da[0][0]*int(self.basic))/100+get_elf[0][0]