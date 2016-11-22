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
		data.append([sle.emp_id,sle.name1,sle.sirdar,sle.status,sle.dob,sle.doj,sle.dor,sle.pf_no,sle.esi_no,sle.voter_card_no,sle.pan_card_no,sle.addhar_card_no])
	return columns, data



def get_report_entries(filters):
	return frappe.db.sql("""select distinct emp_id,name1,sirdar,status,dob,doj,dor,pf_no,esi_no,voter_card_no,pan_card_no,addhar_card_no from `tabLabour Information` where garden = %s """,(filters.garden),as_dict=1)




def get_columns():
		
		columns = [{
			"fieldname": "emp_id",
				"label": _("Emp Code"),
				"fieldtype": "Data",
				"width": 80

		}]

		columns.append({
				"fieldname": "name1",
				"label": _("Emp Name"),
				"fieldtype": "Data",
				"width": 90
	    })


		

	    	columns.append({
				"fieldname": "sirdar",
				"label": _(" Sirdar "),
				"fieldtype": "Data",
				"width": 90
	    })

	    
	    
	    	columns.append({
	    		"fieldname": "status",
				"label": _("Status"),
				"fieldtype": "Data",
				"width": 100
	    })


	    	columns.append({
	    		"fieldname": "dob",
				"label": _(" Date of Birth"),
				"fieldtype": "Date",
				"width": 100
	    })

	    	columns.append({
	    		"fieldname": "doj",
				"label": _(" Date of Joining"),
				"fieldtype": "Date",
				"width": 100
	    })


	    	columns.append({
	    		"fieldname": "dor",
				"label": _(" Date of Retirement"),
				"fieldtype": "Date",
				"width": 120
	    })

	    	columns.append({
	    		"fieldname": "pf_no",
				"label": _("PF No"),
				"fieldtype": "Data",
				"width": 100
	    })


	    	columns.append({
	    		"fieldname": "esi_no",
				"label": _(" ESI No"),
				"fieldtype": "Date",
				"width": 100
	    })

	    	columns.append({
	    		"fieldname": "voter_card_no",
				"label": _("Voter Card No"),
				"fieldtype": "Date",
				"width": 100
	    })


	    	columns.append({
	    		"fieldname": "pan_card_no",
				"label": _("Pan Card No"),
				"fieldtype": "Date",
				"width": 100
	    })

	    	columns.append({
	    		"fieldname": "addhar_card_no",
				"label": _("Adhar Card No"),
				"fieldtype": "Date",
				"width": 100
	    })
	    


		
		
		return columns


