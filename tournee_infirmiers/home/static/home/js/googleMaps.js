

var map = null;
function initialize() {
    console.log("initializing");
  var myOptions = {
    zoom: 10,
    center: new google.maps.LatLng(-33.9, 151.2),
    mapTypeControl: true,
    mapTypeControlOptions: {style: google.maps.MapTypeControlStyle.DROPDOWN_MENU},
    navigationControl: true,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  map = new google.maps.Map(document.getElementById("map_canvas"),
                                myOptions);

  google.maps.event.addListener(map, 'click', function() {
        infowindow.close();
        });
  setMarkers(map, addresses);
}
var icons = new Array();
icons["red"] = new google.maps.MarkerImage("http://www.google.com/intl/en_us/mapfiles/ms/micons/red-dot.png",
      // This marker is 32 pixels wide by 32 pixels tall.
      new google.maps.Size(32, 32),
      // The origin for this image is 0,0.
      new google.maps.Point(0,0),
      // The anchor for this image is at 16,32.
      new google.maps.Point(16, 32));
function getMarkerImage(iconColor) {
   if ((typeof(iconColor)=="undefined") || (iconColor==null)) {
      iconColor = "red";
   }
   if (!icons[iconColor]) {
      icons[iconColor] = new google.maps.MarkerImage("http://www.google.com/intl/en_us/mapfiles/ms/micons/"+ iconColor +"-dot.png",
      // This marker is 32 pixels wide by 32 pixels tall.
      new google.maps.Size(32, 32),
      // The origin for this image is 0,0.
      new google.maps.Point(0,0),
      // The anchor for this image is at 16,32.
      new google.maps.Point(16, 32));
   }
   return icons[iconColor];

}
  // Marker sizes are expressed as a Size of X,Y
  // where the origin of the image (0,0) is located
  // in the top left of the image.

  // Origins, anchor positions and coordinates of the marker
  // increase in the X direction to the right and in
  // the Y direction down.

  var iconImage = new google.maps.MarkerImage('http://www.google.com/intl/en_us/mapfiles/ms/micons/red-dot.png',
      // This marker is 32 pixels wide by 32 pixels tall.
      new google.maps.Size(32, 32),
      // The origin for this image is 0,0.
      new google.maps.Point(0,0),
      // The anchor for this image is at 16,32.
      new google.maps.Point(16, 32));
  var iconShadow = new google.maps.MarkerImage('http://maps.google.com/mapfiles/ms/micons/msmarker.shadow.png',
      // The shadow image is larger in the horizontal dimension
      // while the position and offset are the same as for the main image.
      new google.maps.Size(59, 32),
      new google.maps.Point(0,0),
      new google.maps.Point(16, 32));
      // Shapes define the clickable region of the icon.
      // The type defines an HTML &lt;area&gt; element 'poly' which
      // traces out a polygon as a series of X,Y points. The final
      // coordinate closes the poly by connecting to the first
      // coordinate.
  var iconShape = {
      coord: [19,0, 24,5, 24,12, 23,13, 23,14, 20,17, 20,18, 19,19,
19,20, 18,21, 18,22, 17,23, 17,26, 16,27, 16,31, 14,31, 14,26, 13,25,
13,23, 12,22, 12,20, 10,18, 10,17, 7,14, 7,13, 6,12, 6,6, 7,5, 7,4, 11,0],
      type: 'poly'
  };
var infowindow = new google.maps.InfoWindow(
  {
    size: new google.maps.Size(150,50)
  });

function createMarker(map, latlng, label, html, color) {
    var contentString = '<b>'+label+'</b><br>'+html;
    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        shadow: iconShadow,
        icon: getMarkerImage(color),
        shape: iconShape,
        title: label,
        zIndex: Math.round(latlng.lat()*-100000)<<5
        });

    google.maps.event.addListener(marker, 'click', function() {
        infowindow.setContent(contentString);
        infowindow.open(map,marker);
        });
}

/**
 * Data for the markers consisting of a name, a LatLng and a zIndex for
 * the order in which these markers should display on top of each
 * other.
 */
var addresses = [
  ['Bondi Beach', -33.890542, 151.274856, "red"],
  ['Coogee Beach', -33.923036, 151.259052, "blue"],
  ['Cronulla Beach', -34.028249, 151.157507, "green"],
  ['Manly Beach', -33.80010128657071, 151.28747820854187, "yellow"],
  ['Maroubra Beach', -33.950198, 151.259302, "orange"],
  ['Fullerton Cove', -32.831712,151.918945,"purple"],
  ['Bar Beach',-32.940403,151.768398,"pink"],
  ['Readhead',-33.019495,151.709733,"ltblue"]
];

function setMarkers(map, locations) {
  // Add markers to the map
  var bounds = new google.maps.LatLngBounds();
  for (var i = 0; i < locations.length; i++) {
    var address = locations[i];
    var myLatLng = new google.maps.LatLng(address[1], address[2]);
    var marker = createMarker(map,myLatLng,address[0],address[0],address[3]);
    bounds.extend(myLatLng);
  }
  map.fitBounds(bounds);
}