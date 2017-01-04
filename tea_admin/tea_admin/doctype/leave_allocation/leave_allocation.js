// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Leave Allocation', {
	refresh: function(frm) {

	}
});


cur_frm.fields_dict['emp_code'].get_query = function(doc) {
  return {
    filters: [
			['Labour Information', 'enabled', '=', 'Active']
		]
  }
}
