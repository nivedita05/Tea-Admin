// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Salary for Staff', {
	refresh: function(frm) {

	}
});
frappe.ui.form.on("Salary for Staff", "validate", function(frm) {
    frm.naming_ser="";
    name=frm.doc.emp_code+"/"+frm.doc.date;
    frm.set_value("naming_ser",name);
});

cur_frm.fields_dict['emp_code'].get_query = function(doc) {
  return {
    filters: [
			['Labour Information', 'enabled', '=', 'Active']
		]
  }
}