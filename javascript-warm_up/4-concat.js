#!/usr/bin/node
import { argv } from 'node:process';

function printSentence () {
  const subject = (argv[2]) ? argv[2] : 'undefined';
  const adj = (argv[3]) ? argv[3] : 'undefined';
  console.log(subject + ' is ' + adj);
}

printSentence();
