console.log('Welcome to Holberton School, what is your name?');
process.stdin.once('readable', () => {
  const name = process.stdin.read();
  process.stdout.write(`Your name is:  + ${name}`);
  console.log('This important software is now closing');
});
