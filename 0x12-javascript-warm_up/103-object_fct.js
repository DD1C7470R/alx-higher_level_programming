#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
function inc () { myObject.value = myObject.value + 1; }
myObject.incr = inc;
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
