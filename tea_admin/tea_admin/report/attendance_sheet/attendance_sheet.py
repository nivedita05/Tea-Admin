# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils

def execute(filters=None):
	data = []
	columns = get_columns()


	report_entries = get_report_entries(filters)



	for sle in report_entries:
		
		data.append([sle.date,sle.emp_code,sle.name1,sle.kamjari_code,sle.kamjari_head,sle.attendence,sle.attendance_2nd_char,sle.attendance_3rd_char_1])
	
	return columns, data

def get_report_entries(filters):
	return frappe.db.sql(""" select date, emp_code,name1,kamjari_code,kamjari_head,attendence,attendance_2nd_char,attendance_3rd_char_1 from `tabattendence` where date between %s  and %s order by date asc""",(filters.date1,filters.date2),as_dict=1)



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


		columns.append({
				"fieldname": "kamjari_code",
				"label": _("Kamjari Code"),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 135
	    })


		

	    	columns.append({
				"fieldname": "kamjari_head",
				"label": _(" Kamjari Head "),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 135
	    })

	    	columns.append({
				"fieldname": "attendence",
				"label": _("Attendance Status"),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 135
	    })

	    	columns.append({
				"fieldname": "attendance_2nd_char",
				"label": _("Designated Category"),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 135
	    })

	    	columns.append({
				"fieldname": "attendance_3rd_char_1",
				"label": _(" Actual Category "),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 135
	    })


		
	    
		return columns