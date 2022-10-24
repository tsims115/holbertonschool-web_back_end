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
      const data1 = data.split('\n');
      if (data1[data1.length - 1] === '') {
        data1.pop();
      }
      console.log(`Number of students: ${data1.length - 1}`);
      for (i = 1; i < data1.length; i += 1) {
        data1[i] = data1[i].split(',');
        const fieldName = data1[i][3];
        if (fields[fieldName] === undefined) {
          fields[fieldName] = [data1[i][0]];
        } else {
          fields[fieldName].push(data1[i][0]);
        }
      }
      console.log(`Number of students in CS: ${fields.CS.length}. List: ${fields.CS.join(', ')}`);
      console.log(`Number of students in SWE: ${fields.SWE.length}. List: ${fields.SWE.join(', ')}`);
      resolve();
    });
  });
};
