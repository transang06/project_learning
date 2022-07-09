const express = require("express");
const cors = require("cors");
var app = express();
var fs = require("fs");
app.use(cors());
var bodyParser = require('body-parser');

var urlencodedParser = bodyParser.urlencoded({ extended: false })

app.get('/listUsers', function (req, res) {
   fs.readFile( __dirname + "/" + "users.json", 'utf8', function (err, data) {
      console.log( data );
      res.end( data );
   });
})

app.get('/', function (req, res) {
   fs.readFile( __dirname + "/" + "index.html", 'utf8', function (err, data) {
      console.log( data );
      res.end( data );
   });
})

app.post('/addUser',urlencodedParser, function (req, res) {
   fs.readFile( __dirname + "/" + "users.json", 'utf8', function (err, data) {
      data = JSON.parse( data );
      data[Object.keys(data).length] ={
         first_name: req.body.first_name,
         last_name: req.body.last_name,
         email: req.body.email
      };
      fs.writeFile(__dirname + "/" + "users.json",JSON.stringify(data) , (err) => {
         if (err) throw err;
         console.log('Data written to file');
      });
      res.end( JSON.stringify(data));
   });
})

app.get('/:id', function (req, res) {
   fs.readFile( __dirname + "/" + "users.json", 'utf8', function (err, data) {
      var users = JSON.parse( data );
      var user = users[req.params.id]
      console.log( user );
      res.end( JSON.stringify(user));
   });
})


app.delete('/deleteUser', function (req, res) {
   fs.readFile( __dirname + "/" + "users.json", 'utf8', function (err, data) {
      data = JSON.parse( data );
      delete data["user" + 2];
       
      console.log( data );
      res.end( JSON.stringify(data));
   });
})


var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port)
})
