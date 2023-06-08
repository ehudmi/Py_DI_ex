const { largNumber, fullDate } = require("./main");
const http= require("http");

const b=5;
// console.log(largNumber+b);

const server=http.createServer((req, res)=>{
    res.setHeader('Content-Type','text/html');
    // res.end(`My module is ${largeNumber+b}<br> <h1>Hi there at the frontend<h1>`)
    res.end(`The date and time are currently ${fullDate}`);
});

server.listen(3001, ()=>{
    console.log('Im listening')
})

