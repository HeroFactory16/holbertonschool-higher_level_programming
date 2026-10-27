#!/usr/bin/node
import { argv } from 'node:process';

function countArgv () {
  if (argv[3]) {
    console.log('Arguments found');
    return;
  }
  if (argv[2]) {
    console.log('Argument found');
    return;
  }
  console.log('No argument');
}

countArgv();
