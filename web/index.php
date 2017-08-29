<!--  Adapted from https://jqueryui.com/autocomplete/#custom-data 
 Non case sensitive autosearch from https://stackoverflow.com/questions/11237394/jquery-autocomplete-case-sensitive-for-utf-8-characters -->
<!doctype html>
<html>
	<head>
		<title>Webapi Clustering</title>
		<style>
		
		 li {
		 
		  	cursor:pointer;
		  	margin-bottom:10px;
		 
		 }
		 
		 div.descr {
		 
		  	display:none;
		  	margin-bottom:20px;
		 
		 }
		 
		 div.descr input[type=button] {
		 
		 	margin:5px;
		 
		 }
		 
		 p {
		 
		 	margin-bottom:5px;
		 
		 }
		 
		 
		
		</style>
		<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
        <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
        <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
        <script>

        var accentMap = {
                "á": "a",
                "ö": "o",
                "İ": "i",
                "ş": "s"
            };
        var normalize = function(term) {
                var ret = "";
                for (var i = 0; i < term.length; i++) {
                    ret += accentMap[term.charAt(i)] || term.charAt(i);
                }
                return ret;
        };        
		
		function showDescr(id) {

			$('#descr_'+id).toggle();

		}

		function writeVote(bool,id,name,cluster_id) {

		    /* Get from elements values */
		    var values = "bool=" + bool + "&id="+id+"&name="+name+"&cluster_id="+cluster_id;

		    /* Send the data using post and put the results in a div */
		    /* I am not aborting previous request because It's an asynchronous request, meaning 
		       Once it's sent it's out there. but in case you want to abort it  you can do it by  
		       abort(). jQuery Ajax methods return an XMLHttpRequest object, so you can just use abort(). */
		       ajaxRequest= $.ajax({
		            url: "vote.php",
		            type: "post",
		            data: values
		        });

		      /*  request cab be abort by ajaxRequest.abort() */

		     ajaxRequest.done(function (response, textStatus, jqXHR){
		          // show successfully for submit message
		          alert(response);
		     });

		     /* On failure of request this function will be called  */
		     ajaxRequest.fail(function () {

		       // show error
		       alert("Your vote was not submitted to the server, please try again!");
		     });		

		}

        function yes(id,name,cluster_id) {

        	writeVote(true,id,name,cluster_id);

        }		

        function no(id,name,cluster_id) {

        	writeVote(false,id,name,cluster_id);

        }       
		
        
        $( function() {
			var projects = [];
			var api = []
			$.getJSON( "data.json", function( data ) {
    			$.each( data, function( key, val ) {
    		    	api.push(val['api_name']);
    		    	projects.push([val['id'], val['api_name'], val['cluster_id'],val['progweb_descr']]);
				});
			});   
         
         $( "#project" ).autocomplete({
         	minLength: 3,
            source: function(request, response) {
                var matcher = new RegExp($.ui.autocomplete.escapeRegex(request.term), "i");
                response($.grep(api, function(value) {
                    value = value.label || value.value || value;
                    return matcher.test(value) || matcher.test(normalize(value));
                }));
            },
            focus: function( event, ui ) {
            	$( "#project" ).val( ui.item.label );
                return false;
            },
            select: function( event, ui ) {
            $( "#project" ).val( ui.item.label );
            $( "#project-id" ).val( ui.item.value );
         
            	return false;
            }
		})
        .autocomplete( "instance" )._renderItem = function( ul, item ) {
        	return $( "<li>" )
            	.append( "<div>" + item.label + "</div>" )
            	.appendTo( ul );
         };

         //Start search for neighbour APIs
         $('#search').click(function() {

             	$('#suggestions ul').empty();

				name = $('#project').val();
				cluster_id = -1;

        	    $('#loadingImage').show();
        	    setTimeout(function() {

        	        jQuery.each( projects, function( i, project ) {

      	        	  // Will stop running after api with "name" was found.
        	        	if(project[1]==name) {
							cluster_id = project[2];
							return;
        	        	}
        	        });

        	        //Find APIs with same cluster id
        	        neighbours = []; 
        	        jQuery.each( projects, function( i, project ) {

            	        if(project[1]==name) {

            	        	$('#descrSearched').append("Description: <br>" + project[3]);

            	        }

          	        	if(project[2]==cluster_id && project[1]!=name) {
              	        	$('#suggestions ul').append('<li onClick="showDescr(' + project[0] + ');">' + project[1] + '</li><div class="descr" id="descr_' + project[0] + '">' + project[3] + '<div id="eval"><input type="button" value="useful" id="useful" onClick="yes(' + project[0] + ', \'' + project[1] + '\', \'' + project[2] + '\')"><input type="button" value="not useful" id="no"  onClick="no(' + project[0] + ', \'' + project[1] + '\', \'' + project[2] + '\')"></div></div>');
          	        	}

						$('#suggestions').show();
          	        	
          	        });
                	$('#loadingImage').hide();        	        
        	    }, 0);
        	});
         });

          </script>		 
	</head>
	<body>
		<p> --- Work in progress --- </p>
		<h1>Webapi Clustering</h1>
		<p>Are you using a webapi which is broken? Are you looking for a replacement? Try one of our suggestions!
		</p>
		<form>
    		<input id="project">
    		<input type="hidden" id="project-id"><br><br>
    		<input type="button" value="search" id="search">
		</form>
		<div id="descrSearched"></div>
		<div id="loadingImage" style="display:none";>Loading...</div>
		<div id="suggestions" style="display:none";>
			<p>We suggest one of these APIs as replacement:</p>
			<p>Please rate with a click on the buttons below the description whether this suggestion was helpful for you or not.</p>
			<ul id="list"></ul>
		</div>
		<br><br><br><br>
		<footer style="font-size:12px">Impressum: Jan-Peter Schmidt, Lilienweg 5a, 74847 Obrigheim, KDD Seminar 2017, KIT</footer>
	</body>
</html>









