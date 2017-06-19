if (Drupal.settings.user !== undefined) {
  var id_value;
  var email_value;
  id_value = Drupal.settings.user.uid;
  email_value = Drupal.settings.user.email;

  var _learnq = _learnq || [];

  _learnq.push(['account', 'gmh6f2']);

  _learnq.push(['identify', {
    // Change the line below to dynamically print the user's email.
    '$id'   : id_value,
    '$email' : email_value
  }]);
  var pageCategory;
  if (Drupal.settings.common !== undefined && Drupal.settings.common.pageCategory !== undefined) {
    pageCategoryValue = Drupal.settings.common.pageCategory;
  }
  else if (Drupal.settings.search !== undefined && Drupal.settings.search.pageCategory !== undefined) {
    pageCategoryValue = Drupal.settings.search.pageCategory;
  }
  else if (pageCategory === undefined) {
    pageCategoryValue = "none";
  }

  var pageURL;
  pageURL = window.location.href;
  _learnq.push(['track','Page Category',{'Page URL':pageURL ,'Category Type': pageCategoryValue}]);
(function () {
  var b = document.createElement('script'); b.type = 'text/javascript'; b.async = true;
  b.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'a.klaviyo.com/media/js/analytics/analytics.js';
  var a = document.getElementsByTagName('script')[0]; a.parentNode.insertBefore(b, a);
})();

}
