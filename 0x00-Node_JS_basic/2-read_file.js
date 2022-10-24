const fs = require('fs');

module.exports = function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, { encoding:'utf8', flag:'r' });
  } catch (error) {
    throw Error('Cannot load the database');
  }
  let i;
  const fields = {};
  data = data.split('\r\n');
  if (data[data.length - 1] === '') {
    data.pop();
  }
  console.log(`Number of students: ${data.length - 1}`);
  for (i = 1; i < data.length; i += 1) {
    data[i] = data[i].split(',')
    const fieldName = data[i][3];
    if (fields[fieldName] === undefined) {
      fields[fieldName] = [data[i][0]];
    } else {
      fields[fieldName].push(data[i][0]);
    }
  }
  Object.keys(fields).forEach((k) => {
    const sList = fields[k];
    process.stdout.write(`Number of students in ${k}: ${sList.length}. `);
    process.stdout.write(`List: ${sList.join(', ')}\n`);
  });
};
