#!/usr/bin/node

const request = require('request');
const episodes = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + episodes, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
