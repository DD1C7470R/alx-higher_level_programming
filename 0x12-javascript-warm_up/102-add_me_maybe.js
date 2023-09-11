#!/usr/bin/node

function addMeMaybe (num, cb) {
  cb(num + 1);
}

module.exports = { addMeMaybe };
