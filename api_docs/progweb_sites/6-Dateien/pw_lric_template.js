(function($) {
  Drupal.behaviors.pw_lric_template = {
    attach: function (context, settings) {
      $LRIC.util.ready(function() {
        var lr_options = {};
        lr_options.apikey = Drupal.settings.apiVarSet;
        //console.log(lr_options.apikey);
        lr_options.templatename = "loginradiuscustome_tmpl";
        // Added to avoid interface renderred on all pages
        $interface_length = $('.interface_container').length;
        if($interface_length == 1) {
         $LRIC.renderInterface("interface_container", lr_options);
        }
      });
    }
  }
})(jQuery);
