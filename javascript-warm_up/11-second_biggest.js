#!/usr/bin/node
const process = require('process');

function getSecondBiggest () {
  if (!process.argv[3]) {
    return 0;
  }

  const array = [];

  for (let i = 2; i < process.argv.length; i++) {
    array.push(process.argv[i]);
  }

  array.sort(function (a, b) { return b - a; });

  return array[1];
}

console.log(getSecondBiggest());
