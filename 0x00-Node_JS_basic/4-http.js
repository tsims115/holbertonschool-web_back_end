const http = require('http');

app = http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write('Hello Holberton School!');
  res.end(); //end the response
}).listen(1245);

module.exports = app;
