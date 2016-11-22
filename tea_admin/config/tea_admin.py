from __future__ import unicode_literals
from frappe import _

def get_data():
	return [


		{
			"label": _("Transaction"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Wages Entry",
					"description": _("Default settings for buying transactions.")
				}
		
		]
		},


		{
			"label": _("Setup files"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Labour Information",
					"description": _("Default settings for buying transactions.")
				}
		
		]
		},


		{
			"label": _("Benefits Information"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Medical Benefit Entry",
					"description": _("Default settings for buying transactions.")
				},

				{
					"type": "doctype",
					"name": "Other Benefit Entry",
					"description": _("Default settings for buying transactions.")
				}
		
		]
		},

		{
			"label": _("House Information"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "House Repairing Entry",
					"description": _("Default settings for buying transactions.")
				}

				
		]
		},


		{
			"label": _("Leave"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Leave Application",
					"description": _("Default settings for buying transactions.")
				}

				
		]
		},

		{
			"label": _("Electricity"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Electricity Charges",
					"description": _("Default settings for buying transactions.")
				}

				
		]
		},

		{
			"label": _("Ration"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Ration Distribution",
					"description": _("Default settings for buying transactions.")
				}

				
		]
		},






		{
			"label": _("Reports"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Personal Information Report",
					"doctype": "Labour Information",
				},


				{
					"type": "report",
					"is_query_report": True,
					"name": "Family Information Report",
					"doctype": "Dependent Details",
				},


				{
					"type": "report",
					"is_query_report": True,
					"name": "Medical Report",
					"doctype":"Medical Benefit Entry",
				}
			]
		},


		{
			"label": _("Attendance"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Attendance Sheet",
					"doctype": "Wages Entry",
				}
			]
		},


		{
			"label": _("Payment"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Pay Book",
					"doctype": "Salary Structure",
				}
			]
		}



	]
