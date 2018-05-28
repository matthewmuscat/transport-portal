$(function() {
  $("input").focus(function() {
    $(".login-mask").addClass("login-mask-move");
  });
});

$(function() {
  $("input").on("focusout", function() {
    $(".login-mask").removeClass("login-mask-move");
  });
});