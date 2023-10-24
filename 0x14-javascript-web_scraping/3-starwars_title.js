#!/usr/bin/node
// A script that  prints the title of a Star Wars movie
// where the episode number matches a given integer.

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response) {
  if (error) {
    console.error('error:', error);
  }
  const resultInjson = JSON.parse(response.body);
  console.log(resultInjson.title);
});
