function preloaderShow() {
  $(".preloader").fadeIn();
}

function preloaderHide() {
  $(".preloader").fadeOut();
}

function buttonDisable(button) {
  button.attr("disabled", true);
}

function buttonEnable(button) {
  button.attr("disabled", false);
}
