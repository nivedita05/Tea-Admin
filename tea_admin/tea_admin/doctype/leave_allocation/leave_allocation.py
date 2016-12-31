# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils
from frappe.utils import flt
from datetime import datetime
import os

class LeaveAllocation(Document):
	def validate(self):
		self.get_allocated_leave()




	def get_allocated_leave(self):
		
		from_date=datetime.strptime(self.from_date,'%Y-%m-%d')
		to_date=datetime.strptime(self.to_date,'%Y-%m-%d')
		if (to_date<from_date):
			frappe.throw("Please enter the date correctly, from date can't be greater than to date")
		if (to_date>=from_date):
			diff=abs(to_date.date()-from_date.date()).days
			self.allocated_days=diff
			return self.allocated_days
			
			