const fs= require('fs');

function pointerCount(data){
    console.log(data);
    let step=0;
    let first=0;
    let len=data.length;
    for(let x=0;x<len;x++){
        if(data[x]=='<'){
            step=step-1;
            if(step==-1 && first==0){
                console.log(`it takes ${x} steps to reach -1`);
                first++;
            }
        }
        else{
            step=step+1;
        }
    }
    step>0?
    console.log(`${step} to the right`):
    console.log(`${step} to the left`);
}

fs.readFile('RightLeft.txt','utf-8',(err, data)=>{
    if(err){
        console.error(err);
    }
    else{
        pointerCount(data.split(``));
    }
})
