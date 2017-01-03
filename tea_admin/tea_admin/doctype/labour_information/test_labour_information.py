# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

test_records = frappe.get_test_records('Labour Information')

class TestLabourInformation(unittest.TestCase):
	#from erpnext.stock.get_item_details import get_item_details
	#from frappe import MandatoryError
	def make_employee(self,emp_id):
		if not frappe.db.get_value("Labour Information",{"emp_id": emp_id}):
			test_record = {
				"doctype": "Labour Information",
				"title": "_Test Labour Information",
				"category": "STAFF",
				"name1":"abc",
				"sirdar":"aaa",
				"status":"Permanent",
				"gender1":"Male",
				"doj":"2016-08-19",
				"book_code":"STAFF",
				"emp_id":"001",
				"garden": "Ghatia Tea Estate"
			}
			frappe.get_doc(test_record).insert()
	def employee_name(self):
		employee = self.make_employee("001")
		self.assertEqual(employee.name1, "abc")
		res = frappe.get_list("Labour Information", filters=[["Labour Information", "name1", "like", "abc%"]], fields=["emp_id", "name1"])
		self.assertEquals(len(res), 1)	
		