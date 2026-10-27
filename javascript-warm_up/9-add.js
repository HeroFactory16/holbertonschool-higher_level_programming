#!/usr/bin/node
const process = require('process');

function add (a, b) {
  const result = a + b;
  console.log(Number(result));
}

add(process.argv[2], process.argv[3]);
