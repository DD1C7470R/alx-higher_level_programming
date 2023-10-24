#!/usr/bin/node
// A script  that prints the number of movies where the character
// “Wedge Antilles” is present.

const request = require('request');

const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error('error:', error);
  }

  const computedObj = {};
  const result = JSON.parse(response.body);

  for (const user of result) {
    if (user.completed) {
      computedObj[user.userId] = computedObj[user.userId] >= 1
        ? computedObj[user.userId] + 1
        : 1;
    }
  }
  console.log(computedObj);
});
