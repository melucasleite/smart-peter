var apiUrl = "/api/";
var defaultApiError = "Occoreu um erro com sua solicitação.";
var applicationError = "Erro na aplicação. Entre em contato com o suporte.";
var connectionApiError =
  "Erro de conexão com o servidor. Verifique sua conexão de internet. Caso esteja on-line. Entre em contato com o suporte.";
var defaultApiSuccess = "";

function errorHandler(data) {
  if (data.readyState == 4) {
    try {
      message = data.responseJSON.message;
      Swal.fire("Error", message, "error");
    } catch {
      Swal.fire("Error", defaultApiError, "error");
    }
  } else if (data.readyState == 0) {
    Swal.fire("Error", connectionApiError, "error");
  } else {
    Swal.fire("Error", applicationError, "error");
  }
}

function defaultSuccess(data, callback) {
  message = data.message ? data.message : defaultApiSuccess;
  Swal.fire({
    title: "Pronto.",
    text: message,
    timer: 2000,
    type: "success"
  }).then(callback);
}

function loginRedirect(data) {
  window.location.href = "/";
}

function defaultConfirm(callback) {
  Swal.fire({
    title: "Tem certeza?",
    text: "",
    type: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Sim",
    cancelButtonText: "Cancelar"
  }).then(result => {
    if (result.value) {
      callback();
    }
  });
}
