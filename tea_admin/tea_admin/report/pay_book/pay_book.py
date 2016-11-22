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
	total_other=0
	total_sick=0
	total_pay=0
	total_maternity=0
	tota_leave=0
	total_food_conssesion=0
	total_l_piece=0

	total_addition=0
	
	total_p_per_fund=0
	total_kharcha=0
	total_lp_paid=0
	total_advance=0
	total_ration=0
	total_electricity=0
	total_lic=0

	total_deduction=0

	report_entries = get_report_entries(filters)
	


	for sle in report_entries:
		actual_category= get_actual_category(sle.emp_code)
		pf=get_pf_no(sle.emp_code)
		desig=get_des_category(sle.emp_code)

		# ADDITION REALATED
		pay=get_pay(pf)
		total_pay=pay[0][0]*actual_category[0][0]
		food_conssesion=get_food_conssesion(pf)
		total_food_conssesion=food_conssesion[0][0]*actual_category[0][0]
		l_piece=get_l_piece(pf)
		total_l_piece=l_piece[0][0]*actual_category[0][0]
		sick=get_sick(pf)
		total_sick=sick[0][0]*actual_category[0][0]
		maternity=get_maternity(pf)
		total_maternity=maternity[0][0]*actual_category[0][0]
		leave_pay=get_leave_pay(pf)
		tota_leave=leave_pay[0][0]*actual_category[0][0]
		other=get_other(pf)
		total_other=other[0][0]*actual_category[0][0]

		total_addition=total_other+total_sick+total_pay+total_maternity+tota_leave+total_food_conssesion+total_l_piece



		# DEDUCTION RELATED
		p_per_fund=get_p_per_fund(pf)
		total_p_per_fund=p_per_fund[0][0]*actual_category[0][0]
		kharcha=get_kharcha(pf)
		total_kharcha=kharcha[0][0]*actual_category[0][0]
		lp_paid=get_lp_paid(pf)
		total_lp_paid=lp_paid[0][0*actual_category[0][0]]
		advance=get_advance(pf)
		total_advance=advance[0][0]*actual_category[0][0]
		ration=get_ration(pf)
		total_ration=ration[0][0]*actual_category[0][0]
		electricity=get_electricity(pf)
		total_electricity=electricity[0][0]*actual_category[0][0]
		lic=get_lic(pf)
		total_lic=lic[0][0]*actual_category[0][0]

		total_deduction=total_p_per_fund+total_kharcha+total_lp_paid+total_advance+total_ration+total_electricity+total_lic

		data.append([sle.emp_code,sle.name1,desig,actual_category,pf,pay[0][0]*actual_category[0][0],food_conssesion[0][0]*actual_category[0][0],l_piece[0][0]*actual_category[0][0],sick[0][0]*actual_category[0][0],maternity[0][0]*actual_category[0][0],leave_pay[0][0]*actual_category[0][0],other[0][0]*actual_category[0][0],total_addition,p_per_fund[0][0]*actual_category[0][0],kharcha[0][0]*actual_category[0][0],lp_paid[0][0]*actual_category[0][0],advance[0][0]*actual_category[0][0],ration[0][0]*actual_category[0][0],electricity[0][0]*actual_category[0][0],lic[0][0]*actual_category[0][0],total_deduction,total_addition-total_deduction])
		#ata.append(["","","","","","","",total_pay,total_food_conssesion,total_l_piece,total_sick,total_maternity,tota_leave,total_other,total_p_per_fund,total_kharcha,total_lp_paid,total_advance,total_ration,total_electricity,total_lic])	
		#ata.append(["","","","","","","Total",total_addition,"","","",total_deduction])
		#ata.append(["","","","","","Net Pay",total_addition-total_deduction])
	return columns, data

def get_report_entries(filters):
	return frappe.db.sql(""" select distinct  emp_code,name1 from `tabattendence` where date between %s  and %s  order by date asc""",(filters.date1,filters.date2),as_dict=1)

def get_actual_category(emp_code):
	return frappe.db.sql(""" select count(attendance_3rd_char_1) from `tabattendence` where emp_code=%s order by date asc""",(emp_code))


def get_des_category(emp_code):
	return frappe.db.sql(""" select category from `tabLabour Information` where emp_id=%s""",(emp_code))



def get_pf_no(emp_code):
	return frappe.db.sql(""" select pf_no from `tabLabour Information` where emp_id=%s""",(emp_code))



# EVERYTHING RELATED TO ADDITION

def get_pay(pf):
	return frappe.db.sql(""" select sum(pay) from `tabSalary Structure`  where pf_no = %s group by pf_no""",(pf))

def get_food_conssesion(pf):
	return frappe.db.sql(""" select sum(food_conssesion) from `tabSalary Structure` where pf_no = %s""",(pf))

def get_l_piece(pf):
	return frappe.db.sql(""" select sum(l_piece) from `tabSalary Structure` where pf_no = %s""",(pf))

def get_sick(pf):
	return frappe.db.sql(""" select sum(sick) from `tabSalary Structure` where pf_no = %s""",(pf))

def get_maternity(pf):
	return frappe.db.sql(""" select sum(maternity) from `tabSalary Structure` where pf_no = %s""",(pf))

def get_leave_pay(pf):
	return frappe.db.sql(""" select sum(leave_pay) from `tabSalary Structure` where pf_no = %s""",(pf))

def get_other(pf):
	return frappe.db.sql(""" select sum(other) from `tabSalary Structure` where pf_no = %s""",(pf))


# EVERYTHING RELATED TO DEDUCTION


def get_p_per_fund(pf):
	return frappe.db.sql(""" select sum(p_per_fund) from `tabSalary Structure` where pf_no = %s """,(pf))

def get_kharcha(pf):
	return frappe.db.sql(""" select sum(kharcha) from `tabSalary Structure` where pf_no = %s""",(pf))

def get_lp_paid(pf):
	return frappe.db.sql(""" select sum(lp_paid) from `tabSalary Structure` where pf_no = %s""",(pf))

def get_advance(pf):
	return frappe.db.sql(""" select sum(advance) from `tabSalary Structure` where pf_no = %s""",(pf))

def get_ration(pf):
	return frappe.db.sql(""" select sum(ration) from `tabSalary Structure` where pf_no = %s""",(pf))

def get_electricity(pf):
	return frappe.db.sql(""" select sum(electricity) from `tabSalary Structure` where pf_no = %s""",(pf))

def get_lic(pf):
	return frappe.db.sql(""" select sum(lic) from `tabSalary Structure` where pf_no = %s""",(pf))



# THE COLUMNS SHOWN IN THE REPORT


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
				"label": _(" count on Actual Category "),
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
				"fieldname": "electricity",
				"label": _("Electricity"),
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
