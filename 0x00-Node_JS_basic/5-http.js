const countStudents = require('./3-read_file_async');
const http = require('http');

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.write('This is the list of our students');
    try {
      const path = process.argv[2];
      let sList = await countStudents(path);
      sList = sList.join('\n');
      res.end(sList);
    } catch (error) {
      res.end(error.message);
    }
  }
  res.end();
});
app.listen(1245);
module.exports = app;
