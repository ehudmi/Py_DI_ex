const express= require('express');

const server= express();

server.get('/',(req, res)=>{
    res.send(`<h1>This is an HTML tag<h1>`);
})

server.listen(3000, ()=>{
    console.log('listening');
})