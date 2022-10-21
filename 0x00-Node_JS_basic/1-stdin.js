console.log("Welcome to Holberton School, what is your name?");
let name;
process.stdin.once('readable', (name) => {
  name = process.stdin.read()
  process.stdout.write("Your name is: " + name);
  console.log('This important software is now closing');
});
