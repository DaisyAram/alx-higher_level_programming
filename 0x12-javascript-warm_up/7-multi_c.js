#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  const i = Number(process.argv[2]);
  let x = 0;
  while (x < i) {
    console.log('C is fun');
    x++;
  }
}
