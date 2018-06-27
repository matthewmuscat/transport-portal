$(function() {
  // This moves the background shape on the login screen.
  $("input").focus(function() {
    $(".login-mask").addClass("login-mask-move");
  });

  $("input").on("focusout", function() {
    $(".login-mask").removeClass("login-mask-move");
  });
});