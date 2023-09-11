#!/usr/bin/node
let i = 0;
const input = process.argv[2];
if (!Number(input)) {
  console.log('Missing number of occurrences');
} else {
  if (Number(input) > 0) {
    const inputs = Array(Number(process.argv[2])).fill('C is fun');
    while (inputs[i]) {
      console.log(inputs[i++]);
    }
  }
}
