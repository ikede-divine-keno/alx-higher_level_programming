#!/usr/bin/node
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body);
    results.characters.forEach(element => {
      request(element, function (error, response, body) {
        if (!error) {
          const list = JSON.parse(body);
          console.log(list.name);
        }
      });
    });
  }
});
