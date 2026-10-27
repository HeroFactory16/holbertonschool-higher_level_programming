#!/usr/bin/node
import { argv } from 'node:process';

function printXTimes () {
  const x = parseInt(argv[2]);
  if (!x) {
    console.log('Missing number of occurrences');
    return;
  }

  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}

printXTimes();
