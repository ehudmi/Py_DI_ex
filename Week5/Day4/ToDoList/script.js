const tasks=[];
let taskNum=0;
let taskList=document.getElementsByClassName("listTasks")[0];

let doneTask= (target) =>
{
    let targetID= Array.from(target.parentElement.parentElement.children).indexOf(target.parentElement);
    console.log(targetID);
    let done= tasks[targetID]["done"];
    if(done==false)
    {
        target.labels[0].className="finished";
        tasks[targetID]["done"]=true;
    }
    else{
        target.labels[0].className="";
        tasks[targetID]["done"]= false;
    }
}
let addTask =()=>
{
    let taskText= document.getElementById("taskSub").value;
    if(taskText.length==0)
    {
        alert("There's nothing there!");
        document.getElementById("taskSub").value="";
        return;
    }
    let taskObject= {
        task_id:String(taskNum),
        text:taskText,
        done:false
    }
    tasks.push(taskObject);
    document.getElementById("taskSub").value="";
    let task=document.createElement("div");
    let xButt= document.createElement("i");
    xButt.className= "fas fa-window-close";
    task.appendChild(xButt);
    xButt.addEventListener("click", function(event) {
        let Id =xButt.parentElement.children[1].id;
        tasks.splice(Number(Id),1);
        taskList.removeChild(xButt.parentElement);
    })
    let checkBox= document.createElement("input");
    checkBox.type="checkbox";
    checkBox.id= String(taskNum);
    let label= document.createElement("label");
    label.setAttribute("for",checkBox.id);
    label.textContent= taskText;
    task.appendChild(checkBox);
    task.appendChild(label);
    taskList.appendChild(task)
    taskNum=taskNum+1;
    checkBox.addEventListener("change", function(event) {
        doneTask(event.target);
    })
}

let clearTasks = () =>
{
    let taskLength= tasks.length;
    for(let x=0;x<taskLength;x++)
    {
        taskList.removeChild(taskList.firstChild);
        tasks.pop();
    }
}
let subButt= document.getElementById("add");
subButt.addEventListener("click", addTask);
let clearButt= document.getElementById("clear");
clearButt.addEventListener("click", clearTasks);