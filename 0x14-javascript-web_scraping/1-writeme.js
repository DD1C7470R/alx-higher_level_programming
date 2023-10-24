#!/usr/bin/node
// A script that reads and prints the content of a file.

const fs = require('fs');
const fileName = process.argv[2];
const content = process.argv[3];

fs.writeFileSync(fileName, content, 'utf-8');
