var models = [
  {
    name: "HP LaserJet M1212nf",
    id: "hp_m1212nf",
    crawler: "hp_configpage"
  },
  {
    name: "HP Officejet Pro 8100 N811a",
    id: "hp_8100",
    crawler: "hp_devmgmt"
  },
  {
    name: "HP LaserJet 500 color M551",
    id: "hp_m551",
    crawler: "hp_usagepage"
  },
  {
    name: "HP LaserJet M4555 MFP",
    id: "hp_m4555",
    crawler: "hp_usagepage"
  },
  {
    name: "Brother DCP-8157dn",
    id: "brother_8157",
    crawler: "brother_maintenance"
  },
  {
    name: "Brother MFC-8890DW",
    id: "brother_8890",
    crawler: "brother_home"
  },
  { name: "Brother MFC-8480", id: "brother_8480", crawler: "brother_home" }
];

var printers = [];

$(document).ready(function() {
  models.map(function(model) {
    model.text = model.name;
  });
  $("#model-select").select2({
    data: models
  });
  $('.ip_address').mask('099.099.099.099');
  $('.pat').mask('0999');
  loadPrinters();
  renderModels();
});

function loadPrinters() {
  $.ajax({
    url: apiUrl + "printer",
    beforeSend: preloaderShow,
    complete: preloaderHide,
    error: errorHandler,
    success: function(data) {
      printers = data.printers;
      renderPrinters();
    }
  });
}

function renderPrinters() {
  $("#printers").html("");
  $template = $("#printer-template");
  $template.render(printers).appendTo("#printers");
}

function renderModels() {
  $("#models").html("");
  $template = $("#printer-template");
  $template.render(printers).appendTo("#printers");
}

function onChangeModel(element) {
  $select = $(element);
  var model_id = $select.val();
  var model = models.find(function(model) {
    return model.id == model_id;
  });
  $("#crawler").val(model.crawler);
  $("#name").val(model.name);
}

function addPrinter(event, form) {
  event.preventDefault();
  $form = $(form);
  var data = $form.serializeArray();
  $.ajax({
    url: apiUrl + "printer",
    data: data,
    beforeSend: preloaderShow,
    complete: preloaderHide,
    method: "POST",
    success: function(data) {
      defaultSuccess(data, function() {
        $("#addPrinter").modal("toggle");
        loadPrinters();
      });
    },
    error: errorHandler
  });
}
