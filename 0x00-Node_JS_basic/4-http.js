const http = require('http');

http.createServer(function (req, res) {
  res.write('Hello Holberton School!'); //write a response to the client
  res.end(); //end the response
}).listen(1245);
