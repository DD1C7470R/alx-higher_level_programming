#!/usr/bin/node
// Get command-line arguments starting from the third argument
const args = process.argv.slice(2);

function findSecondLargest (arr) {
  if (arr.length < 2) {
    return 0;
  }

  // Convert the arguments to integers and filter out any non-integer arguments
  const numbers = arr.map(Number).filter(Number.isInteger);

  if (numbers.length < 2) {
    return 0;
  }

  // Sort the numbers in descending order and return the second largest
  const sortedNumbers = numbers.sort((a, b) => b - a);
  return sortedNumbers[1];
}

// Call the function and log the result
const result = findSecondLargest(args);
console.log(result);
