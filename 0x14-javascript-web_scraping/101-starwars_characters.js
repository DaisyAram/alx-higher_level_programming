#!/usr/bin/node
const request = require('request');

const movieId = 3;
const apiBaseUrl = 'https://swapi.dev/api';

request(`${apiBaseUrl}/films/${movieId}`, (error, response, body) => {
  if (!error && response.statusCode == 200) {
    const movie = JSON.parse(body);
    const charactersUrls = movie.characters;

    charactersUrls.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode == 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.log(`Error: ${error}`);
        }
      });
    });
  } else {
    console.log(`Error: ${error}`);
  }
});
