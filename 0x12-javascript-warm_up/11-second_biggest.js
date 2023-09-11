#!/usr/bin/node

const myArray = [];
for (let i = 2; i < process.argv.length; i++) {
  if (Number(process.argv[i])) { myArray.push(Number(process.argv[i])); }
}

function secondLargest (myArrary) {
  if (myArray.length <= 1) {
    return (0);
  } else {
    myArray.sort();
    return myArray[myArray.length - 2];
  }
}
console.log(secondLargest(myArray));
