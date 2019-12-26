var express = require('express');
var app = express();

//setting middleware
var path = './static'
app.use(express.static( path )); //Serves resources from public folder

var server = app.listen(80, '0.0.0.0');

console.log("Serving " + path + " on 80")