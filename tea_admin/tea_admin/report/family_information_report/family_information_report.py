# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

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
		data.append([sle.emp_code,sle.emp_name,sle.family_id,sle.dependent_name,sle.dob,sle.dependent_age,sle.dependent_type,sle.relation,sle.gender,sle.school_going])
	return columns, data



def get_report_entries(filters):
	return frappe.db.sql("""select distinct emp_code,emp_name,family_id,dependent_name,dob,dependent_age,dependent_type,relation,gender,school_going from `tabDependent Details` where garden = %s """,(filters.garden),as_dict=1)





def get_columns():
		
		columns = [{
			"fieldname": "emp_code",
				"label": _("Emp Code"),
				"fieldtype": "Data",
				"width": 80

		}]

		columns.append({
				"fieldname": "emp_name",
				"label": _("Emp Name"),
				"fieldtype": "Data",
				"width": 90
	    })


		columns.append({
				"fieldname": "family_id",
				"label": _("Family Id"),
				"fieldtype": "Data",
				"width": 90
	    })


		

	    	columns.append({
				"fieldname": "dependent_name",
				"label": _(" Dependent Name "),
				"fieldtype": "Data",
				"width": 90
	    })

	    
	    
	    	columns.append({
	    		"fieldname": "dob",
				"label": _("DOB"),
				"fieldtype": "Data",
				"width": 100
	    })


	    	columns.append({
	    		"fieldname": "dependent_age",
				"label": _(" Dependent Age"),
				"fieldtype": "Int",
				"width": 100
	    })

	    	columns.append({
	    		"fieldname": "dependent_type",
				"label": _(" Dependent Type"),
				"fieldtype": "Select",
				"width": 100
	    })


	    	columns.append({
	    		"fieldname": "relation",
				"label": _("Relation"),
				"fieldtype": "Select",
				"width": 120
	    })

	    	columns.append({
	    		"fieldname": "gender",
				"label": _("Gender"),
				"fieldtype": "Select",
				"width": 100
	    })


	    	columns.append({
	    		"fieldname": "school_going",
				"label": _(" School Going"),
				"fieldtype": "Select",
				"width": 100
	    })

	    	

		
		
		return columns


