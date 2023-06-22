const http= require('http');

const server= http.createServer((req, res)=>{
    res.end(`<h1>This is my first response<h1>
    <h1> This is my seconed response<h1>
    <h3>This is my third resposne<h3>`);
})

server.listen(3000,()=>{
    console.log('listening');
})

