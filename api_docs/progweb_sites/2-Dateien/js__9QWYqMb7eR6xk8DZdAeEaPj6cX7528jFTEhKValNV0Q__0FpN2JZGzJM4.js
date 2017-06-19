/* Source and licensing information for the line(s) below can be found at https://www.programmableweb.com/sites/all/modules/custom/pw_ad/js/customscript.js. */
(function($){Drupal.behaviors.customscript={attach:function(context,settings){var flag=0;$('.pw_adblock',context).once('pw_ad',function(){var checkit=window.check_var;if(checkit===undefined){window.check_var=1}else{var timeoutId;clearTimeout(timeoutId);timeoutId=setTimeout(afterpwadready,8e3)}})
function afterpwadready(){var adblock=$('.pw_adblock');if(adblock.length>=1)if(adblock.height()<=20){if(flag==0){dataLayer.push({event:'adBlock',adBlockDetected:"Adblocker Detected"});flag=1}}else if(flag==0){dataLayer.push({event:'adBlock',adBlockDetected:"No Adblocker Detected"});flag=1}}}}})(jQuery);;
/* Source and licensing information for the above line(s) can be found at https://www.programmableweb.com/sites/all/modules/custom/pw_ad/js/customscript.js. */
/* Source and licensing information for the line(s) below can be found at https://www.programmableweb.com/sites/all/modules/custom/pw_ad/js/pw_adzerk.js. */
var p="http",d="static";if(document.location.protocol=="https:"){p+="s";d="engine"};var z=document.createElement("script");z.type="text/javascript";z.async=true;z.src=p+"://"+d+".adzerk.net/ados.js";var s=document.getElementsByTagName("script")[0];s.parentNode.insertBefore(z,s);if(Drupal.settings.adzerkVarSet!==undefined&&Drupal.settings.adzerkVarSet.primary_category!==undefined)var primary_category=Drupal.settings.adzerkVarSet.primary_category;if(Drupal.settings.adzerkVarSet!==undefined&&Drupal.settings.adzerkVarSet.primary_audience!==undefined)var primary_audience=Drupal.settings.adzerkVarSet.primary_audience;if(Drupal.settings.adzerkVarSet!==undefined&&Drupal.settings.adzerkVarSet.primary_channel!==undefined)var primary_channel=Drupal.settings.adzerkVarSet.primary_channel;if(Drupal.settings.adzerkVarSet!==undefined&&Drupal.settings.adzerkVarSet.secondary_category!==undefined)var secondary_category=Drupal.settings.adzerkVarSet.secondary_category;if(Drupal.settings.adzerkVarSet!==undefined&&Drupal.settings.adzerkVarSet.related_companies!==undefined)var related_companies=Drupal.settings.adzerkVarSet.related_companies;if(Drupal.settings.adzerkVarSet!==undefined&&Drupal.settings.adzerkVarSet.related_languages!==undefined)var related_languages=Drupal.settings.adzerkVarSet.related_languages;if(Drupal.settings.adzerkVarSet!==undefined&&Drupal.settings.adzerkVarSet.products!==undefined)var products=Drupal.settings.adzerkVarSet.products;var homepage="homepage",ados=ados||{};ados.run=ados.run||[];ados.run.push(function(){if(window.innerWidth<=780){if(!jQuery('body.page-api-university').length){jQuery('.top-ad-wrapper').hide();if(window.innerWidth<=767){jQuery('.region-content').css('padding-top','67px');if(jQuery('.page-node-add-api,.page-node-add-mashup,.page-node-add-resource,.page-node-add-library,.page-node-add-framework,.page-node-add-how-to-source-code').length){jQuery('.region-content').css('padding-top','0');jQuery('.page-node-add-api h1.page-header,.page-node-add-mashup h1.page-header,.page-node-add-resource h1.page-header,.page-node-add-library h1.page-header, .page-node-add-framework h1.page-header,.page-node-add-how-to-source-code h1.page-header').css('padding-top','73px')}}}}else ados_add_placement(9550,57566,"azk16406",4).setZone(63094).setProperties({company:[related_companies],language:[related_languages],audience:[primary_audience],channel:[primary_channel],products:[products]});if(window.innerWidth>=780);else ados_add_placement(9550,57566,"azk16407",23).setZone(63094).setProperties({company:[related_companies],language:[related_languages],audience:[primary_audience],channel:[primary_channel],products:[products]});if(window.innerWidth<=780){jQuery('.bottom-ad-wrapper').hide()}else ados_add_placement(9550,57566,"azk99048",4).setZone(63095).setProperties({company:[related_companies],language:[related_languages],audience:[primary_audience],channel:[primary_channel],products:[products]});if(window.innerWidth<=780);else ados_add_placement(9550,57566,"azk99049",23).setZone(63095).setProperties({company:[related_companies],language:[related_languages],audience:[primary_audience],channel:[primary_channel],products:[products]});ados_add_placement(9550,306915,"azk83139",5);ados_add_placement(9550,57566,"azk5965",[5,43]).setZone(63096).setProperties({company:[related_companies],language:[related_languages],audience:[primary_audience],channel:[primary_channel],products:[products]});ados_add_placement(9550,57566,"azk26869",983).setZone(125622).setProperties({company:[related_companies],language:[related_languages],audience:[primary_audience],channel:[primary_channel],products:[products]});if(window.innerWidth<=790&&window.innerWidth>=767){ados_add_placement(9550,57566,"azk19861",71).setZone(63097).setProperties({company:[related_companies],language:[related_languages],audience:[primary_audience],channel:[primary_channel],products:[products]})}else if(window.innerWidth<=940&&window.innerWidth>=791){ados_add_placement(9550,57566,"azk19861",18).setZone(63097).setProperties({company:[related_companies],language:[related_languages],audience:[primary_audience],channel:[primary_channel],products:[products]})}else ados_add_placement(9550,57566,"azk19861",5).setZone(63097).setProperties({company:[related_companies],language:[related_languages],audience:[primary_audience],channel:[primary_channel],products:[products]});if(jQuery('body.front').length){ados_setKeywords(homepage)}else ados_setKeywords(primary_category+", "+secondary_category);ados_load()});;
/* Source and licensing information for the above line(s) can be found at https://www.programmableweb.com/sites/all/modules/custom/pw_ad/js/pw_adzerk.js. */
/* Source and licensing information for the line(s) below can be found at https://www.programmableweb.com/sites/all/modules/custom/pw_ad/js/pw_adzerk_native_api_ads.js. */
(function($){Drupal.behaviors.pw_adzerk_native_api_ads={attach:function(context,settings){var pageCategory;if(Drupal.settings.common!==undefined&&Drupal.settings.common.pageCategory!==undefined){pageCategory=Drupal.settings.common.pageCategory}else if(Drupal.settings.search!==undefined&&Drupal.settings.search.pageCategory!==undefined)pageCategory=Drupal.settings.search.pageCategory;if(pageCategory===undefined){$.each($('.adzerk-native-ads',context),function(index,value){$(this).hide()});return};$.each($('.adzerk-native-ads',context),function(index,value){var element=$(this),zoneId=element.attr('zone');if(zoneId===undefined)return;var placements=[],divNames=[];$.each(element.find('.premium-ad'),function(index,value){var div=$(this),divName=div.attr('divname');divNames.push(divName);if(divName===undefined)return;placements.push({divName:divName,networkId:9550,siteId:57566,adTypes:[121],zoneIds:[parseInt(zoneId)]})});if(placements.length===0)return;var inputData={placements:placements,keywords:pageCategory},settings={data:JSON.stringify(inputData),dataType:'json',headers:{"content-type":'application/json'},type:'POST',success:function(data){var hasAds=false;for(var prop in data.decisions)if(data.decisions.hasOwnProperty(prop))if($.inArray(prop,divNames)>=0)if(data.decisions[prop.toString()]&&data.decisions[prop.toString()].contents.length){var innerHTML='';for(var i=0;i<data.decisions[prop.toString()].contents.length;i++)innerHTML+=data.decisions[prop.toString()].contents[i].body;if(innerHTML){element.find("[divname='"+prop.toString()+"']").append(innerHTML);hasAds=true;if(data.decisions[prop.toString()].impressionUrl!==undefined){console.log(data.decisions[prop.toString()].impressionUrl);$.get(data.decisions[prop.toString()].impressionUrl)}}}else if(!data.decisions[prop.toString()])element.find("[divname='"+prop.toString()+"']").remove();if(hasAds){var header=element.closest('.view-id-related_apis').find('.view-header').addClass('header-has-ad');element.addClass('container-has-ad');element.show()}else element.hide();if($("#myTabContent .tab-pane.in.active").length){var tabID=$("#myTabContent .tab-pane.in.active").attr("id");$('#myTab-accordion #'+tabID+'-collapse .panel-body').html($('#myTabContent #'+tabID).html())}}};$.ajax('//engine.adzerk.net/api/v2',settings)})}}})(jQuery);;
/* Source and licensing information for the above line(s) can be found at https://www.programmableweb.com/sites/all/modules/custom/pw_ad/js/pw_adzerk_native_api_ads.js. */
(function ($) {
  Drupal.behaviors.pw_api_university_report = {
    attach: function (context, settings) {
      var apiu_report_path = window.location.pathname;
      var pathArray = window.location.pathname.split( '/' );
      var pwPageLevel = pathArray;

        // Get the Landing Page Count
      if((apiu_report_path == '/api-university') || (apiu_report_path == '/api-university/api-provider-training') || (apiu_report_path ==  '/api-university/api-basics') || (apiu_report_path == '/api-university/api-developer-training')|| (apiu_report_path == '/api-university/apis-for-executives')){
          pw_apiu_get_landing_page_count();
        } else if (pwPageLevel[1] == "news") {
        //Check if the page belongs to story and Series
        pw_get_story_series_pages();
      } else if (pwPageLevel[1] == "api-university") {
        // Check if the page belongs to APIU Series home Page
        pw_apiu_series_home_page(apiu_report_path);
      } else {
        window.apiu = '#notapiu';
      }
     
      function pw_get_story_series_pages() {
        $('.field-name-field-article-body', context).once('pw_api_university', function () {
          var apiu_university_story = Drupal.settings.apiureportVarSet.apiu_university_story;
          if (typeof apiu_university_story == 'string') {
            if (apiu_university_story !== '"No"') {
              window.apiu = '#story';
             /* dataLayer.push({
                'event': 'apiu_story_event',
                'apiu_story_variable': 1
              });*/
            } else window.apiu = '#notapiu';
          }
          var apiu_university_series = Drupal.settings.apiureportVarSet.apiu_series_performance;
          if (typeof apiu_university_series == 'string') {
            if (apiu_university_series !== '') {
              window.apiu = '#story#' + apiu_university_series;
            }

           /* dataLayer.push({
              'event': 'apiu_title_event',
              'apiu_title': apiu_university_series
            });*/
          }
        });
      }
      // Function to get the last part of url : Determining APIU Series Home Page
      function getLastPart(url) {
        var parts = url.split("/");
        return (url.lastIndexOf('/') !== url.length - 1 ? parts[parts.length - 1] : parts[parts.length - 2]);
      }

      // Function to check if it belongs to APIU Series Home Page
      function pw_apiu_series_home_page(apiu_report_path) {
        $('.apiu-banner-logo', context).once('pw_api_university', function () {
          var str = apiu_report_path;
          var api_university_exists = str.indexOf("api-university");
          var lastparturl = getLastPart(str);
          if (api_university_exists == 1) {
            if (lastparturl !== 'api-university' || lastparturl !== 'api-provider-training' || lastparturl !== 'api-basics' || lastparturl !== 'api-developer-training' || lastparturl !== 'apis-for-executives') {
              var apiu_series_home_page = Drupal.settings.apiureportVarSet.apiu_series_home_page;
              if (apiu_series_home_page == lastparturl) {
                window.apiu = '#series-home-page';
               /* dataLayer.push({
                  'event': 'apiu_series_landing_event',
                  'apiu_series_landing_page': apiu_series_home_page
                });*/
              }
            }
          }
        });
      }
      // Check if the page belongs to APIU Landing Page
      function pw_apiu_get_landing_page_count() {
        $('.apiu-banner-logo', context).once('pw_api_university', function () {
            var apiu_university_landing = Drupal.settings.apiureportVarSet.apiu_university_landing;
            if(typeof apiu_university_landing == 'number') {
              window.apiu = '#landing';
            /*  dataLayer.push({
                'event': 'apiu_landingpage_event',
                'apiu_landing_page': apiu_university_landing
              });*/
            }
        });
      }
    }
  }
})(jQuery);
;/**/
/* Source and licensing information for the line(s) below can be found at https://www.programmableweb.com/sites/all/modules/custom/klaviyo/modules/pw_klaviyo/js/pw_clientside_validate.js. */
(function($){$("form#klaviyo-lists-user-subscribe-form").find(".g-recaptcha").hide();$('#edit-klaviyo-form-klaviyo-programmableweb-today-email').keydown(function(){$("form#klaviyo-lists-user-subscribe-form").find("p.help-block").css({display:"inline",width:"auto"});$("form#klaviyo-lists-user-subscribe-form").find("iframe").css({height:"auto",width:"auto"});$("form#klaviyo-lists-user-subscribe-form").find(".g-recaptcha").show()});$("#edit-klaviyo-form-submit").click(function(e){e.preventDefault();$emailValue=$('#edit-klaviyo-form-klaviyo-programmableweb-today-email').val();if($("#edit-klaviyo-form-submit").length)if($emailValue&&(pwEmailValidate($emailValue))){if(!pwInvalidEmailValidate($emailValue)){$("#klaviyo-lists-user-subscribe-form")[0].submit()}else return false}else{$('.messages.error.error-pwt').remove();$('#block-klaviyo-lists-1-klaviyo').append('<div class="messages error error-pwt">Please enter Valid Email Address</div>')}})
function pwInvalidEmailValidate(emailAddress){var expr=/^([0-9_\-\.][a-zA-Z0-9_\-\.]+)@(yahoo+)\.([a-zA-Z]{2,5})$/;return expr.test(emailAddress)}
function pwEmailValidate(emailAddress){var EMAIL_REGEXP=new RegExp('^[a-z0-9]+(\.[_a-z0-9]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,15})$','i');return EMAIL_REGEXP.test(emailAddress)}})(jQuery);;
/* Source and licensing information for the above line(s) can be found at https://www.programmableweb.com/sites/all/modules/custom/klaviyo/modules/pw_klaviyo/js/pw_clientside_validate.js. */
/* Source and licensing information for the line(s) below can be found at https://www.programmableweb.com/sites/all/themes/pw_bootstrap_two/js/bootstrap-tabcollapse.js. */
!function($){"use strict"
function accordionGroupTemplate(parentId,$heading){var tabSelector=$heading.attr('data-target'),active=$heading.parent().is('.active');if(!tabSelector){tabSelector=$heading.attr('href');tabSelector=tabSelector&&tabSelector.replace(/.*(?=#[^\s]*$)/,'')};var $tabContent=$(tabSelector),groupId=$tabContent.attr('id')+'-collapse';return'<div class="panel panel-default">   <div class="panel-heading">      <h4 class="panel-title">        <a class="'+(active?'':'collapsed')+'" data-toggle="collapse" data-parent="#'+parentId+'" href="#'+groupId+'">           '+$heading.html()+'        </a>      </h4>   </div>   <div id="'+groupId+'" class="panel-collapse collapse '+(active?'in':'')+'">       <div class="panel-body">           '+$tabContent.html()+'       </div>   </div></div>'}
function accordionTemplate(id,$headings,clazz){var accordionTemplate='<div class="panel-group '+clazz+'" id="'+id+'">';$headings.each(function(){var $heading=$(this);accordionTemplate+=accordionGroupTemplate(id,$heading)});accordionTemplate+='</div>';return accordionTemplate};$.fn.tabCollapse=function(options){return this.each(function(){var $this=$(this),$headings=$this.find('li:not(.dropdown) [data-toggle="tab"], li:not(.dropdown) [data-toggle="pill"]');options=$.extend({},$.fn.tabCollapse.defaults,options);var accordionHtml=accordionTemplate($this.attr('id')+'-accordion',$headings,options.accordionClass);$this.after(accordionHtml);$this.addClass(options.tabsClass);$this.siblings('.tab-content').addClass(options.tabsClass)})};$.fn.tabCollapse.defaults={accordionClass:'visible-xs',tabsClass:'hidden-xs'}}(window.jQuery);;
/* Source and licensing information for the above line(s) can be found at https://www.programmableweb.com/sites/all/themes/pw_bootstrap_two/js/bootstrap-tabcollapse.js. */
/* Source and licensing information for the line(s) below can be found at https://www.programmableweb.com/sites/all/themes/pw_bootstrap_two/js/pw_tabs.js. */
(function($){$('.navbar-collapse-search .form-type-textfield #edit-term--3').removeAttr('placeholder')})(jQuery);;
/* Source and licensing information for the above line(s) can be found at https://www.programmableweb.com/sites/all/themes/pw_bootstrap_two/js/pw_tabs.js. */
