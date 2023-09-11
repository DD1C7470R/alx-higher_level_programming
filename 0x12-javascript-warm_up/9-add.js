#!/usr/bin/node

const num1 = process.argv[2];
const num2 = process.argv[3];
function add (a, b) {
  if (!Number(num1) || process.argv.length < 4) {
    console.log(NaN);
  } else {
    console.log(Number(num1) + Number(num2));
  }
}
add(num1, num2);
