#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};

myObject.incr = function () {
  myObject.value = myObject.incr + 1;
};

console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
