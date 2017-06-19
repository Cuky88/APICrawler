(function($) {
  Drupal.behaviors.pw_loginlric_script = {
    attach: function (context, settings) {
      var providers = $.parseJSON(Drupal.settings.providers);
      $.each(providers, function(key, val) {
        setInterval(function () {
          $('.lr_' + val).parent().parent().hide();
        }, 10);
      });
      var LocalDomain = Drupal.settings.localVarSet;
     // console.log(LocalDomain);
      if (window.LoginRadiusSDK) {
        LoginRadiusSDK.setLoginCallback(function () {
          var token = LoginRadiusSDK.getToken();
         // console.log(token);
          redirect(token);
        });
      }
      function redirect(token, name) {
        var token_name = name ? name : 'token';
        jQuery('#fade').show();
        var form = document.createElement('form');
        form.action = LocalDomain;
        form.method = 'POST';

        var hiddenToken = document.createElement('input');
        hiddenToken.type = 'hidden';
        hiddenToken.value = token;
        hiddenToken.name = token_name;
        form.appendChild(hiddenToken);
        if ((window.lr_source) && (lr_source == 'wall_post' || lr_source == 'friend_invite')) {
          var hiddenToken = document.createElement('input');
          hiddenToken.type = 'hidden';
          hiddenToken.value = lr_source;
          hiddenToken.name = 'lr_source';
          form.appendChild(hiddenToken);
        }

        var hiddenPWT = document.createElement('input');
        hiddenPWT.type = 'hidden';
        hiddenPWT.value = pwt;
        hiddenPWT.name = 'pwt';
        form.appendChild(hiddenPWT);

        document.body.appendChild(form);
        form.submit();
      }
    }
  }
})(jQuery);
