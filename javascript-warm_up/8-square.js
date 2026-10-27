#!/usr/bin/node
const process = require('process');

function printSquare () {
  const size = Math.abs(parseInt(process.argv[2]));
  if (!size) {
    console.log('Missing size');
    return;
  }

  let line = 'X';
  for (let i = 1; i < size; i++) {
    line += 'X';
  }
  for (let i = 0; i < size; i++) {
    console.log(line);
  }
}

printSquare();
