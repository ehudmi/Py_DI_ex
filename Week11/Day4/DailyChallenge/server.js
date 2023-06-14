const express= require('express');
const cors= require('cors');


const server= express();
server.use(cors());
server.use(express.urlencoded())

server.get('/aboutMe/:hobby', (req, res)=>{
    let hobby=req.params;
    if(hobby.hobby.search(/[^a-z]/i)==-1){
        res.send(`Your hobby is ${hobby.hobby}`);
    }
    else{
        res.status(404).send(`Can't find that`);
    }
})
server.get('/pic', (req, res)=>{
    res.sendFile(__dirname+'/public/pic.html');
})

server.get('/form', (req, res)=>{
    res.sendFile(__dirname+'/public/index.html');
})
server.post('/formData', function (req, res, next){
    res.send(`${req.body.mail} has sent you a messege "${req.body.messege}"`);
})

server.listen(3030);