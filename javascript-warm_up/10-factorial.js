#!/usr/bin/node
const process = require('process');

function factorial (a, b = 1) {
  let result = b;
  if (a > 0) {
    result *= a;
    a--;
    return factorial(a, result);
  }

  return result;
}

console.log(factorial(process.argv[2]));
