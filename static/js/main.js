function hide(target){
		document.getElementById(target).style.display= "none";
	}

	function show(target){
		document.getElementById(target).style.display= "block";
	}
  function goBack() {
	window.history.back()
  }
  
  function getID(target) {
	var elemnt = document.getElementById(target);
	return elemnt;
  }
  

function submitReview(target) {
     console.log('its working');
     loadURLPostAsynch(getID(target), '', '', function(res){
        if (res != "OK") {
            alert(res)
        }
        else {
            alert('success')
        }
     });
}

function loadURLAsynch(url, whereto, callback) {
	
	// Create an XMLHttpRequest object or ActiveX control
	if (window.XMLHttpRequest)  {
		var request = new XMLHttpRequest();
		var neednull = 1;
	}
	else if (window.ActiveXObject) {
		var request = new ActiveXObject("Microsoft.XMLHTTP");
		var neednull = 0;
	}
	
	// If XMLHTTPRequest is supported
	if (request) {
		// Set up asynchronous request
		try {
			request.open("GET", url, true);
		}
		catch (e) {
			alert("Error accessing server:\n"+e.toString());
		}

		request.onload = function(e) {
			if (request.readyState == 4)
				if (request.status == 200) {
            		var content = request.responseText;
					if (typeof(whereto) == 'object')
						whereto.innerHTML = content;
					if (callback)
						callback(content);
					return;
				}
			alert('Error ' + request.status + ' ' + request.responseText);
		}

		request.onerror = function(e) {
			alert('Error ' + request.status + ' ' + request.responseText);
		}

		// Send asynchronous request
		if (neednull) request.send(null)
		else request.send();
	}
}

function loadURLPostAsynch(url, data, whereto, callback) {
	
	// url may be a URI string or a form
	// If it is a form, it is sent using formdata and data is ignored
	// data may be a string or a dictionary
	if (window.XMLHttpRequest) 
		var request = new XMLHttpRequest();
	else if (window.ActiveXObject)
		var request = new ActiveXObject("Microsoft.XMLHTTP");
	
	// If XMLHTTPRequest is supported
	if (request) {
		// Set up asynchronous request
		var fd = null;
		if (typeof(url) == 'object' && url.nodeName == 'FORM') {
			var dest = url.action;
			fd = new FormData(url);
		}
		else
			var dest = url;

		try {
			request.open("POST", dest, true);
		}
		catch (e) {
			alert("Error accessing server:\n"+e.toString());
		}

		request.onload = function(e) {
			if (request.readyState == 4)
				if (request.status == 200) {
            		var content = request.responseText;
					if (typeof(whereto) == 'object')
						whereto.innerHTML = content;
					if (callback)
						callback(content);
					return;
				}
			alert('Error ' + request.status + ' ' + request.responseText);
		}

		request.onerror = function(e) {
			alert('Error ' + request.status + ' ' + request.responseText);
		}

		// Send asynchronous request
		if (fd)
			var senddata = fd;
		else if (typeof(data) == 'object') {
			var senddata = new FormData();
			for (var x in data) {
				senddata.append(x, data[x]);
			}
		}
		else {
			var senddata = data;
			request.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
		}

		request.send(senddata);
	}
}








$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});