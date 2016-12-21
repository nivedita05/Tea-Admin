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

	total_add=0
	total_sub=0

	net_amount=0

	report_entries=get_report_entries(filters)

	for i in report_entries:

		emp_category_and_pf_no=get_category_and_pf_no(i.emp_code,filters)
		attendence=get_attendence(i.emp_code,filters)
		special=get_attendence_special(i.emp_code,filters)
		normal=get_attendence_normal(i.emp_code,filters)

		pay=get_pay(i.emp_code,filters)
		fc=get_fc(i.emp_code,filters)
		l_piece=get_l_piece(i.emp_code,filters)
		sick=get_sick(i.emp_code,filters)
		maternity=get_mat(i.emp_code,filters)
		leave_pay=get_leave_pay(i.emp_code,filters)
		other=get_other(i.emp_code,filters)

		total_add=pay[0][0]+fc[0][0]+l_piece[0][0]+sick[0][0]+maternity[0][0]+leave_pay[0][0]+other[0][0]

		p_per_fund=pay[0][0]*0.12
		kharcha=get_kharcha(i.emp_code,filters)
		lp_paid=get_lp_paid(i.emp_code,filters)
		advance=get_advance(i.emp_code,filters)
		ration=get_ration(i.emp_code,filters)
		lic=get_lic(i.emp_code,filters)


		total_sub=p_per_fund+kharcha[0][0]+lp_paid[0][0]+advance[0][0]+ration[0][0]+lic[0][0]
	
		net_amount=total_add-total_sub

		data.append([i.emp_code,i.name1,emp_category_and_pf_no[0][0],attendence,special,normal,emp_category_and_pf_no[0][1],pay,fc,l_piece,sick,maternity,leave_pay,other,total_add,p_per_fund,kharcha,lp_paid,advance,ration,lic,total_sub,net_amount])
	

	return columns,data


#--------------------------------------------------------------------------------------
def get_report_entries(filters):
	return frappe.db.sql("""select distinct emp_code,name1 from `tabattendence` where date between %s and %s""",(filters.date1,filters.date2),as_dict=1)

def get_category_and_pf_no(emp_code,filters):
	return frappe.db.sql("""select category,pf_no from `tabLabour Information` where emp_id=%s and garden=%s""",(emp_code,filters.garden))

def get_attendence(emp_code,filters):
	return frappe.db.sql("""select count(emp_code) from `tabattendence` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))

def get_attendence_special(emp_code,filters):
	return frappe.db.sql("""select count(emp_code) from `tabattendence` where date between %s and %s and emp_code=%s and attendance_3rd_char_1="SPECIAL" """,(filters.date1,filters.date2,emp_code))

def get_attendence_normal(emp_code,filters):
	return frappe.db.sql("""select count(emp_code) from `tabattendence` where date between %s and %s and emp_code=%s and attendance_3rd_char_1="NORMAL" """,(filters.date1,filters.date2,emp_code))

#------------------------------------------------------------------------------------
def get_pay(emp_code,filters):
	return frappe.db.sql("""select sum(pay) from `tabattendence` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))

def get_fc(emp_code,filters):
	return frappe.db.sql("""select sum(food_conssesion) from `tabattendence` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))

def get_l_piece(emp_code,filters):
	return frappe.db.sql("""select sum(l_piece) from `tabattendence` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))

def get_sick(emp_code,filters):
	return frappe.db.sql("""select sum(sick) from `tabattendence` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))

def get_mat(emp_code,filters):
	return frappe.db.sql("""select sum(maternity) from `tabattendence` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))


def get_leave_pay(emp_code,filters):
	return frappe.db.sql("""select sum(leave_pay) from `tabattendence` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))

def get_other(emp_code,filters):
	return frappe.db.sql("""select sum(other) from `tabattendence` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))






def get_kharcha(emp_code,filters):
	return frappe.db.sql("""select sum(kharcha) from `tabattendence` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))

def get_lp_paid(emp_code,filters):
	return frappe.db.sql("""select sum(lp_paid) from `tabattendence` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))

def get_ration(emp_code,filters):
	return frappe.db.sql("""select sum(ration) from `tabattendence` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))


def get_lic(emp_code,filters):
	return frappe.db.sql("""select sum(lic) from `tabattendence` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))

def get_advance(emp_code,filters):
	return frappe.db.sql("""select sum(advance) from `tabattendence` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))




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
				"fieldname": "attendance_2nd_char",
				"label": _("Designated Category"),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 90
	    })

	    	

	    	
	    	columns.append({
				"fieldname": "count_attendance_3rd_char_1",
				"label": _(" Total Persent "),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 120
	    })

	    	columns.append({
				"fieldname": "count_attendance_special",
				"label": _(" Special "),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 120
	    })

	    	columns.append({
				"fieldname": "count_attendance_normal",
				"label": _(" Normal "),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 120
	    })

	    	columns.append({
				"fieldname": "pf_no",
				"label": _("PF No"),
				"fieldtype": "Data",
				"option":"Labour Information",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "pay",
				"label": _("Pay"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "food_conssesion",
				"label": _("Food Conssesion"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "l_piece",
				"label": _("L/Piece"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "sick",
				"label": _("Sick"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "maternity",
				"label": _("Maternity"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "leave_pay",
				"label": _("Leave Pay"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "other",
				"label": _("Other"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "total_addition",
				"label": _("After Addition"),
				"fieldtype": "Float",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "p_per_fund",
				"label": _("P/Fund"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "kharcha",
				"label": _("Kharcha"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "lp_paid",
				"label": _("Lp Paid"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "advance",
				"label": _("Advance"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "ration",
				"label": _("Ration"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })



	    	columns.append({
				"fieldname": "lic",
				"label": _("LIC"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "total_deduction",
				"label": _("After Deduction"),
				"fieldtype": "Float",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "net_amount",
				"label": _("Net Amount"),
				"fieldtype": "Float",
				"width": 90
	    })




		return columns
