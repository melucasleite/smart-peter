$(document).ready(function() {
  loadConfig();
});

function loadConfig() {
  $.ajax({
    url: apiUrl + "config",
    method: "GET",
    beforeSend: preloaderShow,
    complete: preloaderHide,
    success: function(data) {
      var config = data.config;
      console.log(config)
      $("[name='name']").val(config.name);
      $("[name='api']").val(config.api);
      $("[name='token']").val(config.token);
    }
  });
}

function saveConfig(event, form) {
  event.preventDefault();
  defaultConfirm(function() {
    $form = $(form);
    var data = $form.serializeArray();
    $.ajax({
      url: apiUrl + "config",
      data: data,
      beforeSend: preloaderShow,
      complete: preloaderHide,
      method: "POST",
      success: function(data) {
        defaultSuccess(data, function() {
          loadConfig();
        });
      },
      error: errorHandler
    });
  });
}
