// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Dependent Details", "validate", function(frm) {

	var birth_date=frm.doc.dob
	var today_date=frappe.datetime.nowdate()
	
   
    frm.set_value("dependent_age",parseInt(today_date)-parseInt(birth_date));
});


frappe.ui.form.on("Dependent Details", "validate", function(frm) {
    frm.dep_id="";
    name=frm.doc.dependent_name;
    frm.set_value("dep_id",name);
});
