var express = require('express');
var app = express();
const fs = require('fs').promises;

app.get('/', function (req, res) {
    fs.readFile(__dirname + "/map.html")
        .then(contents => {
            res.setHeader("Content-Type", "text/html");
            res.writeHead(200);
            res.end(contents);
        });
    })

app.get('/json', function (req, res) {
    console.log("Hello from server");
    fs.readFile( __dirname + "/data.json")
        .then(data => {
            console.log("Yeheaa")
            res.setHeader("Content-Type", "application/json")
            res.writeHead(200);
            res.end( data );
    });
});
 

 app.get('/logic.js', function (req, res) {
    res.sendFile(__dirname + "/" + "logic.js");
  });

var server = app.listen(8000, function () {
    var host = server.address().address
    var port = server.address().port
    console.log("Example app listening at http://%s:%s", host, port)
 })