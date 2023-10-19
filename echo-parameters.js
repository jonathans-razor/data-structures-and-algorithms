
if (process.argv.length < 3) {
  console.error('- Parameter(s) expected.');
  return
}

process.argv.forEach((val, index) => {
  console.log(`${index}: ${val}`);
});
