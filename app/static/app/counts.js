var printers;

$(document).ready(function() {
  loadPrinters();
});

function loadPrinters() {
  $.ajax({
    url: apiUrl + "printer",
    beforeSend: preloaderShow,
    complete: preloaderHide,
    error: errorHandler,
    success: function(data) {
      printers = data.printers;
      renderTable();
    }
  });
}

function renderTable() {
  $("#count").DataTable({
    dom: "Bfrtip",
    responsive: false,
    data: printers,
    columns: [
      { data: "pat" },
      { data: "name" },
      { data: "ip" },
      { data: "location" },
      { data: "count" }
    ],
    buttons: ["copy", "csv", "excel", "pdf", "print"]
  });
}
