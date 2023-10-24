#!/usr/bin/node
// A script  that prints the number of movies where the character
// “Wedge Antilles” is present.

const request = require('request');
const movieUrl = process.argv[2];
let counter = 0;

request(movieUrl, function (error, response) {
  if (error) {
    console.error('error:', error);
    return;
  }
  const resultInjson = JSON.parse(response.body);

  const data = resultInjson.results;

  for (const obj of data) {
    for (const character of obj.characters) {
      if (character.includes('https://swapi-api.alx-tools.com/api/people/18')) {
        counter += 1;
      }
    }
  }
  console.log(counter);
});
