#!/usr/bin/node
let i = 0;
const input = process.argv[2];
if (!Number(input)) {
  console.log('Missing size');
} else {
  if (Number(input) > 0) {
    const inputs = Array(Number(process.argv[2])).fill('X');
    while (inputs[i]) {
      for (const x of inputs) {
        process.stdout.write(x);
      }
      console.log();
      i++;
    }
  }
}
