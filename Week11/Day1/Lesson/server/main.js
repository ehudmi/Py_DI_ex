const http= require('http');

const server= http.createServer((req, res)=>{
    if(req.url== '/'){
        if(req.method== 'GET'){
            res.end('<h1>Home</h1>')
        }
    }
    else if(req.url=='/about'){
        res.end('<h1>About</h1>');
    }
    else{
        res.end('<h1>404 page not found</h1>')
    }
})

server.listen(3001, ()=>{
    console.log('run on 3001');
})