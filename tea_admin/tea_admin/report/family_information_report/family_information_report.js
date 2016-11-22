// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.query_reports["Family Information Report"] = {
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

            "fieldname":"gender",
            "label": __("Gender"),
            "fieldtype": "Select",
            "options":["Female", "Male"],
            "default": "",
            "reqd":0



        },

        {

            "fieldname":"school_going",
            "label": __("School Going"),
            "fieldtype": "Select",
            "options":["Yes ", "No"],
            "default":"",
            "reqd":0



        },



        {

            "fieldname":"dependent_type",
            "label": __("Dependent Type"),
            "fieldtype": "Select",
            "options":["Adult", "Minor"],
            "default": "",
            "reqd":0



        }
  


       


        

        


    ]
}
