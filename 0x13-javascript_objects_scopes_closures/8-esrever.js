#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  for (let idx = 1; idx <= list.length; idx++) {
    reversedList.push(list[list.length - idx]);
  }
  return reversedList;
};
