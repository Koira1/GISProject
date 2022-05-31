getjson();

function getjson(){
    console.log("fetching..");
    fetch('/json')
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        response.json().then(
            json => {
                console.log(json);
                this.users = json;
                //console.log(this.users);
                drawPoints(json);
            }
        )
    })
}

 var latlngs = [
     [17.385044, 78.486671],
     [16.506174, 80.648015],
     [17.000538, 81.804034],
     [17.686816, 83.218482]
 ];

 var latlang = [
[[17.385044, 78.486671], [16.506174, 80.648015], [17.686816, 83.218482]],
[[13.082680, 80.270718], [12.971599, 77.594563],[15.828126, 78.037279]]
];
 
 // Adding layer to the map
 map.addLayer(layer);

function drawPoints(json) {
    var mapOptions = {
        center: [17.385044, 78.486671],
        zoom: 10
     }
    var map = new L.map('map', mapOptions);
    // Creating a Layer object
    var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
    var marker = new Array();
     // Adding layer to the map
     map.addLayer(layer);
    var doc = document.getElementById('map');
    for(var item in json.data) {
        var data = JSON.parse(json.data[item]);
        console.log(data.location);
        marker = new L.Marker([data.latitude, data.longitude]).addTo(map);
    }
}
