#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  const characters = body.characters;
  characters.forEach(characterUrl => {
    request(characterUrl, { json: true }, (err, res, characterBody) => {
      if (err) { return console.log(err); }
      console.log(characterBody.name);
    });
  });
});
