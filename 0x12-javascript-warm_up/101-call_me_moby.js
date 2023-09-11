#!/usr/bin/node
const callMeMoby = (x, func) => {
  while (x > 0) {
    func();
    x--;
  }
};
module.exports = { callMeMoby };
