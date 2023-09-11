#!/usr/bin/node

function addMeMaybe (num, cb) {
  const nb = num + 1;
  cb((nb));
}

module.exports = { addMeMaybe };
