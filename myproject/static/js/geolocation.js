var watchId = null;

var geoloc = function() {
  if (navigator.geolocation) {
    var optn = {
        enableHighAccuracy : true,
        timeout : Infinity,
        maximumAge : 0
    };
    watchId = navigator.geolocation.watchPosition(sendPosition, showError, optn);
  } else {
    alert('Geolocation is not supported in your browser');
  }
};

var sendPosition = function(position) {
  $.post('/geo/', { 'lat': position.coords.latitude, 'lng': position.coords.longitude });
};

var stopWatch = function() {
  if (watchId) {
    navigator.geolocation.clearWatch(watchId);
    watchId = null;
  }
};

// TODO: Show error message somewhere
var showError = function (error) {
  switch(error.code) {
  case error.PERMISSION_DENIED:
    //console.log("User denied the request for Geolocation.");
    break;
  case error.POSITION_UNAVAILABLE:
    //console.log("Location information is unavailable.");
    break;
  case error.TIMEOUT:
    //console.log("The request to get user location timed out.");
    break;
  case error.UNKNOWN_ERROR:
    //console.log("An unknown error occurred.");
    break;
  }
};

$(function(){
  geoloc();
});
