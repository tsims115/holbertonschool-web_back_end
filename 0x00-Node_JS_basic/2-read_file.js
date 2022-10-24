const fs = require('fs');
module.exports = function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, {encoding:'utf8', flag:'r'});
  } catch(error) {
    throw Error('Cannot load the database');
  }
  let i;
  let fields = {};
  data = data.split('\r\n');
  if (data[data.length - 1] === '') {
    data.pop();
  }
  console.log(`Number of students: ${data.length - 1}`);
  for (i = 1; i < data.length; i++) {
    data[i] = data[i].split(',')
    let field_name = data[i][3];
    if (fields[field_name] === undefined) {
      fields[field_name] = [data[i][0]];
    } else {
      fields[field_name].push(data[i][0]);
    }
  }
  Object.keys(fields).forEach((k) => {
    let s_list = fields[k];
    process.stdout.write(`Number of students in ${k}: ${s_list.length}. `);
    process.stdout.write(`List: ${s_list.join(', ')}\n`);
  });
}
