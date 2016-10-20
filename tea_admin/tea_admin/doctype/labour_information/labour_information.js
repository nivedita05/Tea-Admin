// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Labour Information", "validate", function(frm) {
    frm.lab_id="";
    name=frm.doc.abb+"-"+frm.doc.emp_code;
    frm.set_value("lab_id",name);
});
   