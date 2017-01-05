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
import calendar
import datetime
from frappe.desk.notifications import clear_doctype_notifications
from dateutil.relativedelta import relativedelta

class SalaryforStaff(Document):
	
	def validate(self):
		self.get_basic()
		self.get_hra()
		self.get_da()
		self.get_vda()
		self.get_elf()
		self.get_fc()
		self.get_alw()
		self.get_oth()
		self.get_add_total()
		
		self.get_pf()
		self.get_p_tax()
		self.get_mis_ded()
		self.get_rev()
		self.get_advance()
		self.get_lic()
		self.get_ration()
		self.get_wl_fare()
		self.get_sub_total()

		self.get_gross_salary()
		self.get_net_salary()

	def get_basic(self):

		get_basic=frappe.db.sql("""select basic from `tabSalary Staff` where emp_name=%s""",(self.emp_name))
		now = datetime.datetime.now()
		days = calendar.monthrange(now.year, now.month)[1]
		self.basic=(int(float(get_basic[0][0]))*int(self.days_present))/days
		return self.basic

	def get_hra(self):
		basic=self.get_basic()
		get_hra=frappe.db.sql("""select hra from `tabSalary Structure` where book_code=%s""",(self.book_code))
		self.hra=round((get_hra[0][0]*int(basic))/100,2)
		return self.hra
	
	def get_da(self):
		basic=self.get_basic()
		get_da=frappe.db.sql("""select da from `tabSalary Structure` where book_code=%s""",(self.book_code))
		self.da=round((get_da[0][0]*int(basic))/100,2)
		return self.da
	
	def get_vda(self):
		basic=self.get_basic()
		get_vda=frappe.db.sql("""select vda from `tabSalary Structure` where book_code=%s""",(self.book_code))
		self.vda=round((get_vda[0][0]*int(basic))/100,2)
		return self.vda
	
	def get_elf(self):
		get_elf=frappe.db.sql("""select elf from `tabSalary Structure` where book_code=%s""",(self.book_code))
		self.elf=get_elf[0][0]
		return self.elf

	def get_fc(self):
		get_fc=frappe.db.sql("""select fc from `tabSalary Staff` where emp_name=%s""",(self.emp_name))
		self.fc=get_fc[0][0]
		return self.fc
	
	def get_alw(self):
		get_alw=frappe.db.sql("""select allowence from `tabSalary Staff` where emp_name=%s""",(self.emp_name))
		self.allowence=get_alw[0][0]
		return self.allowence

	def get_oth(self):
		get_oth=frappe.db.sql("""select other from `tabSalary Staff` where emp_name=%s""",(self.emp_name))
		self.other=get_oth[0][0]
		return self.other


	def get_add_total(self):
		get_basic=self.get_basic()
		get_hra=self.get_hra()
		get_da=self.get_da()
		get_vda=self.get_vda()
		get_elf=self.get_elf()
		get_fc=self.get_fc()
		get_alw=self.get_alw()
		get_oth=self.get_oth()

		get_salary=float(get_basic)+float(get_hra)+float(get_da)+float(get_vda)+float(get_elf)+float(get_fc)+float(get_alw)+float(get_oth)
		self.salary=round(get_salary,2)
		return self.salary

	def get_pf(self):
		get_basic=self.get_basic()
		get_hra=self.get_hra()
		get_da=self.get_da()
		get_vda=self.get_vda()
		get_elf=self.get_elf()
		get_fc=self.get_fc()
		get_alw=self.get_alw()
		get_oth=self.get_oth()
		get_salary=float(get_basic)+float(get_da)+float(get_vda)+float(get_fc)+float(get_alw)+float(get_oth)
		if get_salary>=15000:
			self.pf=1800
		else:
			self.pf=round(get_salary*0.12,2)
		return self.pf

	def get_p_tax(self):
		salary=self.get_add_total()
		
		if int(salary)<=8500:
			self.p_tax="0.0"
		if int(salary)>=8501 and int(salary)<=10000:
			self.p_tax="90"
		if int(salary)>=10001 and int(salary)<=15000:
			self.p_tax="110"
		if int(salary)>=15001 and int(salary)<=25000:
			self.p_tax="130"
		if int(salary)>=25001 and int(salary)<=40000:
			self.p_tax="150"
		if int(salary)>=40001:
			self.p_tax="200"
	

		return self.p_tax


	def get_mis_ded(self):
		get_mis_ded=frappe.db.sql("""select mis_ded from `tabSalary Staff` where emp_name=%s""",(self.emp_name))
		self.mislleneous_ded=get_mis_ded[0][0]
		return self.mislleneous_ded

	def get_rev(self):
		get_rev=frappe.db.sql("""select rev from `tabSalary Staff` where emp_name=%s""",(self.emp_name))
		self.rev=get_rev[0][0]
		return self.rev

	def get_advance(self):
		get_advance=frappe.db.sql("""select advance from `tabSalary Staff` where emp_name=%s""",(self.emp_name))
		self.advance=get_advance[0][0]
		return self.advance
	
	def get_lic(self):
		get_lic=frappe.db.sql("""select lic from `tabLic File` where emp_name=%s""",(self.emp_name))
		self.lic=get_lic[0][0]
		return self.lic

	def get_ration(self):
		get_ration=frappe.db.sql("""select ration from `tabSalary Staff` where emp_name=%s""",(self.emp_name))
		self.ration=get_ration[0][0]
		return self.ration

	def get_wl_fare(self):
		pass

    
	def get_sub_total(self):
		pf=self.get_pf()
		p_tax=self.get_p_tax()
		mis_ded=self.get_mis_ded()
		rev=self.get_rev()
		lic=self.get_lic()
		ration=self.get_ration()
		advance=self.get_advance()

		get_sub_total=float(p_tax)+float(pf)+float(mis_ded)+float(rev)+float(lic)+float(ration)+float(advance)
		self.ded_total=round(get_sub_total,2)
		return self.ded_total


	

	def get_gross_salary(self):
		get_basic=self.get_basic()
		get_da=self.get_da()
		get_vda=self.get_vda()
		get_alw=self.get_alw()
		get_oth=self.get_oth()

		add=float(get_basic)+float(get_da)+float(get_vda)+float(get_alw)+float(get_oth)
		gross_total=float(add)
		self.gross_salary=round(gross_total,2)
		return self.gross_salary

    
    	
	def get_net_salary(self):

		add=self.get_gross_salary()
		sub=self.get_sub_total()
		net_total=float(add)-float(sub)
		self.net_salary=round(net_total,2)
		if self.net_salary<0:
			self.net_salary="0.0"
		return self.net_salary


    	


		