#!/usr/bin/node
import { argv } from 'node:process';

function printFirstArgv () {
  if (argv[2]) {
    console.log(argv[2]);
    return;
  }
  console.log('No argument');
}

printFirstArgv();
