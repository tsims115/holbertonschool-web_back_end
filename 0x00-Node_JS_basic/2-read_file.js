module.exports = function countStudents(path) {
  const fs = require('fs');
  let data = fs.readFileSync(path,
            {encoding:'utf8', flag:'r'});
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
    process.stdout.write(`Number of students in ${k}: ${s_list.length}`);
    process.stdout.write(` List: `);
    for (i = 0; i < s_list.length; i++) {
      process.stdout.write(`${s_list[i]}`);
      if (i === s_list.length - 1) {
        break;
      }
      process.stdout.write(', ');
    }
    process.stdout.write('\n');
  });
}
