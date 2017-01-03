# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils


def execute(filters=None):
	data = []
	columns=get_columns()
	return columns, data


def get_columns():
		
		columns = [{
			"fieldname": "date",
				"label": _("Date"),
				"fieldtype": "date",
				"option":"attendence",
				"width": 135

		}]
		columns.append({
				"fieldname": "emp_code",
				"label": _("Emp Code"),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 135
	    })


		columns.append({
				"fieldname": "name1",
				"label": _("Emp Name"),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 135
	    })


		

	    
		return columns