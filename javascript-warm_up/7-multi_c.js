#!/usr/bin/node
const process = require('process');

function printXTimes () {
  const x = parseInt(process.argv[2]);
  if (!x) {
    console.log('Missing number of occurrences');
    return;
  }

  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}

printXTimes();
