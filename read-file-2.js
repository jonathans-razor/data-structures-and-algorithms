const { readFile } = require('fs').promises;

async function hello() {
  const file = await readFile('hello.txt', 'utf8');
  console.log(file.toString());
}

// Notice that the hello function print AFTER the start because it is async.
hello();
console.log('start');