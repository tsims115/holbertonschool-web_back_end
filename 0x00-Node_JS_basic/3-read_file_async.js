const fs = require('fs');

module.exports = function countStudents(path) {
  let data;
  try {
    data = fs.readFile(path, 'utf8');
  } catch (error) {
    throw Error('Cannot load the database');
  }
  console.log(data);
};
