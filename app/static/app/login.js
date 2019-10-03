function login(event, el) {
  event.preventDefault();
  var data = $(el).serializeArray();
  var button = $(el)
    .closest("form")
    .find(":submit");
  $.ajax({
    url: apiUrl + "security/login",
    data: data,
    method: "POST",
    beforeSend: buttonDisable(button),
    complete: buttonEnable(button),
    error: errorHandler,
    success: function(data) {
      loginRedirect(data);
    }
  });
}

function recover(event, el) {
  event.preventDefault();
  var data = $(el).serializeArray();
  var button = $(el)
    .closest("form")
    .find(":submit");
  $.ajax({
    url: apiUrl + "security/forgot",
    data: data,
    method: "POST",
    beforeSend: buttonDisable(button),
    complete: buttonEnable(button),
    error: errorHandler,
    success: function(data) {
      //TODO: Implement recover success
    }
  });
}

function logout(event, el) {
  var button = $(el);
  $.ajax({
    url: apiUrl + "security/logout",
    method: "GET",
    beforeSend: buttonDisable(button),
    complete: buttonEnable(button),
    error: errorHandler,
    success: function(data) {
      window.location = "/";
    }
  });
}
