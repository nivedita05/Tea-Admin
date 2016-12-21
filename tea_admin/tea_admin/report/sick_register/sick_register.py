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
	
	rep=get_report_entries(filters)
	
	for i in rep:
		data.append([i.emp_code,i.name1,i.sick])


	
	return columns, data


def get_report_entries(filters):
	return frappe.db.sql("""select emp_code,name1,sick from `tabattendence` where attendence="SICK" and date between %s and %s and garden=%s""",(filters.date1,filters.date2,filters.garden),as_dict=1)



def get_columns():
		
		columns = [{
				"fieldname": "emp_code",
				"label": _("Emp Code"),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 90
	    }]
		
		columns.append({
				"fieldname": "name1",
				"label": _("Emp Name"),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 120
	    })


	    	columns.append({
				"fieldname": "sick",
				"label": _("Paid"),
				"fieldtype": "Float",
				"width": 120
	    })


	 	return columns

