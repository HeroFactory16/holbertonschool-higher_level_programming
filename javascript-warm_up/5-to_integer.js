#!/usr/bin/node
import { argv } from 'node:process';

function printNumber () {
  let x = parseInt(argv[2]);
  if (!x) {
    x = 'Not a number';
    console.log(x);
    return;
  }
  console.log('My number: ' + x);
}

printNumber();
