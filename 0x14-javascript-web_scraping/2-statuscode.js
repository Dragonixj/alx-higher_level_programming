#!/usr/bin/node
// A script that displays the status code of
// GET request.

const request = require('request');

if (process.argv.length < 3) {
    console.log(`Usage : ./${process.argv[1]} <URL>`);
    process.exit(1);
}

const url = process.argv[2];

request(url, (error, response) => {
    if (error) {
        console.log('Error:', error.message);
        process.exit(1);
    }
    console.log('code', response.statusCode);
});
