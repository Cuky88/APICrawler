function detectmob() {
  if (navigator.userAgent.match(/Android/i) || navigator.userAgent.match(/webOS/i) ||
    navigator.userAgent.match(/iPhone/i) || navigator.userAgent.match(/iPad/i) ||
    navigator.userAgent.match(/iPod/i) || navigator.userAgent.match(/BlackBerry/i) ||
    navigator.userAgent.match(/Windows Phone/i)) {
    return true;
  }
  else {
    return false;
  }
}

(function($){
   if($("a.login-social-tooltip").length)
  {
   $("a.login-social-tooltip").tooltip();
  }
  if($("a.manage-social-tooltip").length) {
    $("a.manage-social-tooltip").tooltip();
  }
  if ($('#edit-lr-social-login-linked').length) {
    $('#edit-lr-social-login-linked .social-login-links').hide();
    $('#edit-lr-social-login-linked .social-plus-icon').addClass('glyphicon-plus');
    $('#edit-lr-social-login-linked .social-container').toggle(
      function() {
        $('#edit-lr-social-login-linked .social-login-links').slideDown('fast');
        $('#edit-lr-social-login-linked .social-plus-icon').removeClass('glyphicon-plus');
        $('#edit-lr-social-login-linked .social-plus-icon').addClass('glyphicon-minus');
      },
      function() {
        $('#edit-lr-social-login-linked .social-login-links').slideUp('fast');
        $('#edit-lr-social-login-linked .social-plus-icon').removeClass('glyphicon-minus');
        $('#edit-lr-social-login-linked .social-plus-icon').addClass('glyphicon-plus');
      }
    );
  };

})(jQuery);
