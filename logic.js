getCities();

function getCities(){
    var mapOptions = {
        center: [41.013888888888886, 28.955555555555556],
        zoom: 10,
        preferCanvas: true
     }
    var map = new L.map('map', mapOptions);
    var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
    // Adding layer to the map
    map.addLayer(layer);
    fetch('/json')
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        response.json().then(
            json => {
                drawCities(json, map);
                getRoutes(map);
            }
        )
    })
}

function getRoutes(map){
    fetch('/directions')
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        response.json().then(
            json => {
                drawRoutes(json, map);
                getHotels(map)
            }
        )
    })
}

function getHotels(map) {
    fetch('/hotels')
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        response.json().then(
            json => {
                drawHotels(json, map);

            }
        )
    })
}

function drawCities(json, map) {
    var marker = new Array();
    for(var item in json.data) {
        var data = JSON.parse(json.data[item]);
        marker = new L.Marker([data.latitude, data.longitude]).bindPopup(data.location).addTo(map);
    }
}

function drawRoutes(json, map) {
    var lines = new Array();
    var i = 0;
    for (i = 0; i < json.directions.length; i++) {
        for (var item in json.directions[i].route) {
            lines.push([json.directions[i].route[item].lat, json.directions[i].route[item].lng]);
        }
        var polyline = new L.polyline(lines, {color: 'red'}).addTo(map);
    }
}

function drawHotels(json, map) {
    var marker = new Array();
    for (i = 0; i < json.data.length; i++) {
        for(var item in json.data[i].hotels) {
            marker = new L.circleMarker([json.data[i].hotels[item]["location"].lat, json.data[i].hotels[item]["location"].lng], { radius : 4, color: '#FFFF00', opacity : 10, fillOpacity : 10 }).bindPopup(json.data[i].hotels[item].name).addTo(map);
        }
    }
}
