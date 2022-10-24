const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.write('This is the list of our students\n');
    let sList;
    try {
      const path = process.argv[2];
      List = await countStudents(path);
      sList = sList.join('\n');
      res.end(String(sList));
    } catch (error) {
      res.end(error.message);
    }
  }
  res.end();
});
app.listen(1245);
module.exports = app;
