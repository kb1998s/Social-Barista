let map;
let service;
let infowindow;
/*This function initializes the map, and the area in which it is focusing. Also, initializes the request
 or search of the map (what is to be found)
 @param takes in no parameters
 @return map of the specified location
 @see Map of location, finding Starbucks locations
*/
function initMap() {
  const ellensburg = new google.maps.LatLng(46.9965, 120.5478);

  infowindow = new google.maps.InfoWindow();
  map = new google.maps.Map(document.getElementById("map"), {
    center: ellensburg,
    zoom: 15,
  });

  const request = {
    query: "Starbucks",
    fields: ["name", "geometry"],
  };

  service = new google.maps.places.PlacesService(map);
  service.findPlaceFromQuery(request, (results, status) => {
    if (status === google.maps.places.PlacesServiceStatus.OK && results) {
      for (let i = 0; i < results.length; i++) {
        createMarker(results[i]);
      }

      map.setCenter(results[0].geometry.location);
    }
  });
}
/* This function returns the marker on the map which actually locates the Starbucks 
and places a tag on that location. It takes in the place that was written before as an arg
and this is the location of what the map is showing
@param place the location that was written above and is where the map is located
@return returns the mark of the Starbucks location on map
@see red tag on the map of location
*/
function createMarker(place) {
  if (!place.geometry || !place.geometry.location) return;

  const marker = new google.maps.Marker({
    map,
    position: place.geometry.location,
  });

  google.maps.event.addListener(marker, "click", () => {
    infowindow.setContent(place.name || "");
    infowindow.open(map);
  });
}