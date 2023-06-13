const express= require('express');
const user = {
    firstname: 'John',
    lastname: 'Doe'};

const server=express();

// server.get('/users',(req, res)=>{
//     res.header('Access-Control-Allow-Origin', '*');
//     res.send(`${JSON.stringify(user)}`);
// })

server.listen(3000, ()=>{
    console.log('listening');
})
