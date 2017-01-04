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
from frappe.desk.notifications import clear_doctype_notifications
from dateutil.relativedelta import relativedelta

class MakePayment(Document):

	def validate(self):# validation function , validation during save
		self.get_pay()# get all the field which will added to get the paying value
		self.get_adv()# get advance value if any albour has taken any advance
		self.get_ded_adv()# get amount in which denomination they wants advance to be deducted
		self.get_incentive()# for extra working or for less working get some amount added to their paying amount or deducted
		self.get_pf()

	def on_submit(self):# updation done during submit
		self.get_advance_adjusted() # after deducting the value of advance deducted value will be updated accordingly
		

	def on_cancel(self): # updation done during cancel
		self.get_cancelled()# if some data is submitted and there after someone want to delete it

	def get_pay(self):# get all the field which will added to get the paying value
		for i in self.get('pay'):
			payment_amount = frappe.db.sql("""select sum(pay)+sum(food_conssesion)+sum(l_piece)+sum(sick)+sum(maternity)+sum(leave_pay)+sum(other) from `tabattendence` where emp_code=%s and book_code=%s and date between %s and %s""",(i.emp_code,self.book_code,self.from_date,self.to_date))
			if payment_amount:
				i.payment_amount=payment_amount[0][0]
			else:
				i.payment_amount="0.0"

	def get_pf(self):
		for i in self.get('pay'):
			pf_no=frappe.db.sql("""select pf_no from `tabLabour Information` where emp_id=%s""",(i.emp_code))
			i.pf_no=pf_no[0][0]

			
	def get_advance_adjusted(self): # after deducting the value of advance deducted value will be updated accordingly
		for i in self.get('pay'):
			
			deducted_advance_amount = frappe.db.sql("""select deducted_denomination from `tabAdvance Entry` where emp_code=%s""",(i.emp_code))
			if deducted_advance_amount:
				i.deducted_advance_amount=round(deducted_advance_amount[0][0],2)
				adjusted_value=frappe.db.sql("""select adjusted_values from `tabAdvance Entry` where emp_code=%s""",(i.emp_code))
				i.adjusted_value=float(adjusted_value[0][0])+round(deducted_advance_amount[0][0],2)
				frappe.db.sql("""Update `tabAdvance Entry` set adjusted_values=%s where emp_code=%s""",(i.adjusted_value,i.emp_code))
				
			else:
				i.deducted_advance_amount="0.0"
				i.adjusted_value="0.0"
			
			advance = frappe.db.sql("""select advance_amount from `tabAdvance Entry` where emp_code=%s""",(i.emp_code))
			if advance:
				i.advance_amount=round(advance[0][0],2)
				
			else:
				i.advance_amount="0.0"


			if (i.adjusted_value==i.advance_amount):
				frappe.db.sql("""Update `tabAdvance Entry` set advance_status=%s where emp_code=%s""",("Closed",i.emp_code))
				frappe.db.sql("""Update `tabAdvance Entry` set advance_amount=%s where emp_code=%s""",("0.0",i.emp_code))
				frappe.db.sql("""Update `tabAdvance Entry` set deducted_denomination=%s where emp_code=%s""",("0.0",i.emp_code))
		
			
	def get_ded_adv(self):# get amount in which denomination they wants advance to be deducted
		for i in self.get('pay'):
			deducted_advance_amount = frappe.db.sql("""select deducted_denomination from `tabAdvance Entry` where emp_code=%s""",(i.emp_code))
			if deducted_advance_amount:
				i.deducted_advance_amount=round(deducted_advance_amount[0][0],2)
			else:
				i.deducted_advance_amount="0.0"
		return str(i.deducted_advance_amount)	



	def get_adv(self):# get advance value if any albour has taken any advance
		for i in self.get('pay'):
			advance = frappe.db.sql("""select advance_amount from `tabAdvance Entry` where emp_code=%s""",(i.emp_code))
			if advance:
				i.advance_amount=round(advance[0][0],2)
			else:
				i.advance_amount="0.0"
	
	

	def get_incentive(self):# for extra working or for less working get some amount added to their paying amount or deducted
		adv=self.get_ded_adv()
		pay=self.get_pay()
		for i in self.get('pay'):
			payment_amount = frappe.db.sql("""select sum(pay)+sum(food_conssesion)+sum(l_piece)+sum(sick)+sum(maternity)+sum(leave_pay)+sum(other) from `tabattendence` where emp_code=%s and book_code=%s and date between %s and %s""",(i.emp_code,self.book_code,self.from_date,self.to_date))
			if payment_amount:	
				i.payment_amount=payment_amount[0][0]


			deducted_advance_amount = frappe.db.sql("""select deducted_denomination from `tabAdvance Entry` where emp_code=%s""",(i.emp_code))
			base_task=frappe.db.sql("""select sum(base_task) from `tabattendence` where emp_code=%s and date between %s and %s""",(i.emp_code,self.from_date,self.to_date))
			task_done=frappe.db.sql("""select sum(quantity) from `tabattendence` where emp_code=%s and date between %s and %s""",(i.emp_code,self.from_date,self.to_date))
			
			if base_task:
				if task_done:
					i.incentive=float(task_done[0][0])-float(base_task[0][0])
					
					if i.incentive>=1 and i.incentive<=6:
						i.incentive=i.incentive*3
						i.paid_amount=i.payment_amount+i.incentive
						pf_no=frappe.db.sql("""select pf_no from `tabLabour Information` where emp_id=%s""",(i.emp_code))
						i.pf_no=pf_no[0][0]
						if i.pf_no == "0":
							if deducted_advance_amount:
								i.paid_amount=round((i.payment_amount+i.incentive)-round(deducted_advance_amount[0][0],2),2)
							else:
								i.paid_amount=round((i.payment_amount+i.incentive),2)
						else:
							if deducted_advance_amount:
								i.paid_amount=round((i.payment_amount+i.incentive)*0.88-round(deducted_advance_amount[0][0],2),2)
							else:
								i.paid_amount=round(round((i.payment_amount+i.incentive),2)*0.88,2)
					
					elif i.incentive>6:
						i.incentive=18+(i.incentive-6)*3.5
						i.paid_amount=i.payment_amount+i.incentive
						if i.pf_no == "0":
							if deducted_advance_amount:
								i.paid_amount=round((i.payment_amount+i.incentive)-round(deducted_advance_amount[0][0],2),2)
							else:
								i.paid_amount=round((i.payment_amount+i.incentive),2)
						else:
							if deducted_advance_amount:
								i.paid_amount=round((i.payment_amount+i.incentive)*0.88-round(deducted_advance_amount[0][0],2),2)
							else:
								i.paid_amount=round(round((i.payment_amount+i.incentive),2)*0.88,2)
	

	def get_cancelled(self):# if some data is submitted and there after someone want to delete it
		for i in self.get('pay'):
			
			deducted_advance_amount = frappe.db.sql("""select deducted_denomination from `tabAdvance Entry` where emp_code=%s""",(i.emp_code))
			if deducted_advance_amount:
				i.deducted_advance_amount=round(deducted_advance_amount[0][0],2)
				adjusted_value=frappe.db.sql("""select adjusted_values from `tabAdvance Entry` where emp_code=%s""",(i.emp_code))
				i.adjusted_value=float(adjusted_value[0][0])-round(deducted_advance_amount[0][0],2)
				frappe.db.sql("""Update `tabAdvance Entry` set adjusted_values=%s where emp_code=%s""",(i.adjusted_value,i.emp_code))
				
			else:
				i.deducted_advance_amount="0.0"
				i.adjusted_value="0.0"



@frappe.whitelist()
def get_employees(**args):
	return frappe.get_list('Labour Information',filters=args['filters'], fields=['name1','emp_id'])