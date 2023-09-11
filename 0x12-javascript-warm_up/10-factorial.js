#!/usr/bin/node

const num1 = Number(process.argv[2]);
function factorial (num1) {
  if (!num1 || num1 < 1) {
    return (1);
  } else {
    return (num1 * factorial(num1 - 1));
  }
}
console.log(factorial(num1));
