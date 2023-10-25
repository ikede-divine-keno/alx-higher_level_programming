#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const filePath = process.argv[3];
const url = process.argv[2];
// request(url).pipe(fs.createWriteStream(filePath))
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    fs.writeFile(filePath, response.body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
