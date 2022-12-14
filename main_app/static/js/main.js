var dateEl = document.getElementById("id_date");
M.Datepicker.init(dateEl, {
  format: "yyyy-mm-dd",
  defaultDate: new Date(),
  setDefaultDate: true,
  autoClose: true,
});

// add additional JS to initialize select below
var selectEl = document.getElementById("id_food");
M.FormSelect.init(selectEl);
