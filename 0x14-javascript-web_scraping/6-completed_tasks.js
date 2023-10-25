#!/usr/bin/node
const request = require('request');

// const url = 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json';
const url = process.argv[2];
request(url, function (error, response, body) {
  const userstask = {};
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    for (const t in tasks) {
      const task = tasks[t];

      if (task.completed === true) {
        if (userstask[task.userId] === undefined) {
          userstask[task.userId] = 1;
        } else {
          userstask[task.userId]++;
        }
      }
    }
    console.log(userstask);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
