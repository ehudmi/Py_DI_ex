let text=document.getElementById("textInput");
let bestInput;
text.addEventListener("input",function(event) {
    let input=event.target.value;
    input=input.toLowerCase();
    input.search(/[^a-z]/g)!==-1 && input!==""?event.target.value=bestInput:bestInput=input;
})
