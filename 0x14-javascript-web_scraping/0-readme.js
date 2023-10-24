#!/usr/bin/node
// A script that reads and prints the content of a file.

const fs = require('fs')
file_name = process.argv[2]
fs.readFile(file_name, 'utf-8', (error, content) => {
	if (error) {
		console.log(error)
		return;
	}
	console.log(content.toString())
})
