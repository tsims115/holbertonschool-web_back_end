const http = require('http');
const express = require('express');

const app = express();


const server = http.createServer(app);

server.listen(7865);
console.log("API available on localhost port 7865");

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});
