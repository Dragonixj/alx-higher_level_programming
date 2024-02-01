#!/usr/bin/node

// Javascript code that write the constant
// you pass to argv[3] into
// a file name argv[2].txt

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], (err) => {
    if (err) {
        console.log(err);
    }
});
