const countStudents = require('./3-read_file_async');
const http = require('http');
const { count } = require('console');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.write('This is the list of our students');
    try {
      let sList = await countStudents(process.argv[2]);
      sList = sList.join('\n');
      res.end(sList);
    } catch (err) {
      res.end(err);
    }
  }
  res.end();
});
app.listen(1245);
module.exports = app;
