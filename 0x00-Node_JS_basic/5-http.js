const http = require('http');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.write('This is the list of our students');
    const countStudents = require('./3-read_file_async');
    countStudents("database.csv");
  }
  res.end();
});
app.listen(1245);
module.exports = app;
