(function($){
  // $("a.login-social-tooltip").tooltip();
  var hideRegisterForm = true;
  $("#user-register-form #edit-account input").each(function() {
    if ($(this).hasClass('error')) {
      hideRegisterForm = false;
    }
  });
  if (hideRegisterForm) {
    $("#user-register-form #edit-custom-separtor").hide();
    $("#user-register-form #edit-account").hide();
    $("#user-register-form #edit-field-terms-of-service").hide();
    $("#user-register-form .captcha").hide();
    $("#user-register-form #edit-submit").hide();
    $(".become-member.user-member-login").hide();
    $("#user-register-form #edit-field-first-name").hide();
    $("#user-register-form #edit-field-last-name").hide();
    $("#user-register-form #edit-field-mobile-phone").hide();
    $("#user-register-form #edit-field-user-company").hide();
    $("#user-register-form #edit-field-title").hide();
  }

  $(".login-with-email").click(function() {
    $("#user-register-form #edit-custom-separtor").slideToggle("normal").css("overflow","inherit");
    $("#user-register-form #edit-account").slideToggle("normal");
    $("#user-register-form #edit-field-terms-of-service").slideToggle("normal");
    $("#user-register-form .captcha").slideToggle("normal");
    $("#user-register-form #edit-submit").slideToggle("normal");
    $(".become-member.user-member-login").slideToggle("normal");
    $("#user-register-form #edit-field-first-name").slideToggle("normal");
    $("#user-register-form #edit-field-last-name").slideToggle("normal");
    $("#user-register-form #edit-field-mobile-phone").slideToggle("normal");
    $("#user-register-form #edit-field-user-company").slideToggle("normal");
    $("#user-register-form #edit-field-title").slideToggle("normal");
  });
  pwt = 0;
  if ($('#edit-klaviyo-lists-klaviyo-programmableweb-today-subscribe').length) {
    if($('#edit-klaviyo-lists-klaviyo-programmableweb-today-subscribe').is(":checked")) {
      pwt = 1;
    }
    else {
      pwt = 0;
    }
  }
  $('#edit-klaviyo-lists-klaviyo-programmableweb-today-subscribe').change(function() {
    if($(this).is(":checked")) {
      pwt = 1;
    }
    else {
      pwt = 0;
    }
  });
})(jQuery);
