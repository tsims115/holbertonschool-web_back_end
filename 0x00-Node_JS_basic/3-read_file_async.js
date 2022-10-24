const fs = require('fs');
const { resolve } = require('path');

module.exports = function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
      }
      let i;
      const fields = {};
      data = data.split('\n');
      if (data[data.length - 1] === '') {
        data.pop();
      }
      console.log(`Number of students: ${data.length - 1}`);
      for (i = 1; i < data.length; i += 1) {
        data[i] = data[i].split(',');
        const fieldName = data[i][3];
        if (fields[fieldName] === undefined) {
          fields[fieldName] = [data[i][0]];
        } else {
          fields[fieldName].push(data[i][0]);
        }
      }
      console.log(`Number of students in CS: ${fields.CS.length}. List: ${fields.CS.join(', ')}`);
      console.log(`Number of students in SWE: ${fields.SWE.length}. List: ${fields.SWE.join(', ')}`);
      resolve('resolved');
    });
  });
};
