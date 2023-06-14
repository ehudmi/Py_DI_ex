const express= require('express');
const cors= require('cors');
const user = {
    firstname: 'John',
    lastname: 'Doe'};

const server=express();
server.use(cors());
server.use(express.static('public'));
// server.get('/users',(req, res)=>{
//     res.header('Access-Control-Allow-Origin', '*');
//     res.send(`${JSON.stringify(user)}`);
// })

// server.get('/:id',(req, res)=>{
//     let id=req.params;
//     res.send(JSON.stringify(id));
// })


server.listen(3000, ()=>{
    console.log('listening');
})
