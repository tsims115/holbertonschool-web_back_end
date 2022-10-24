const http = require('http');

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write('This is the list of our students');
    const countStudents = require('./3-read_file_async');
    countStudents("database.csv")
    .then(() => {
    })
        .catch((error) => {
        console.log(error);
    });

  }
  res.end();
});
app.listen(1245);
module.exports = app;
