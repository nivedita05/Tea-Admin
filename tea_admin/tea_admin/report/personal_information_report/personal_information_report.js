// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt


frappe.query_reports["Personal Information Report"] = {
	"filters": [
	 {
            "fieldname":"date",
            "label": __("DATE"),
            "fieldtype": "Date",
            "options": "",
            "default": frappe.datetime.get_today(),
            "reqd":0
        },

        {

            "fieldname":"garden",
            "label": __("Garden"),
            "fieldtype": "Link",
            "options":"Estate",
            "default":"",
            "reqd":0



        },

        {

            "fieldname":"company_name",
            "label": __("Company"),
            "fieldtype": "Select",
            "options":["Rungamattee", "Rawjute"],
            "default": "",
            "reqd":0



        },


        {

        	"fieldname":"status",
            "label": __("Status"),
            "fieldtype": "Select",
            "options":["Permanent", "Casual","Tempurary"],
            "default":"",
            "reqd":0



        },

        {

            "fieldname":"gender",
            "label": __("Gender"),
            "fieldtype": "Select",
            "options":["Female", "Male"],
            "default": "",
            "reqd":0



        },


        {

        	"fieldname":"dor",
            "label": __("Date of Retirement"),
            "fieldtype": "Date",
            "options": "",
            "default": frappe.datetime.get_today(),
            "reqd":0



        },



        {

        	"fieldname":"pf_no",
            "label": __("PF No"),
            "fieldtype": "Data",
            "options": "",
            "default": "",
            "reqd":0



        }


     	


       

	]
		
    }