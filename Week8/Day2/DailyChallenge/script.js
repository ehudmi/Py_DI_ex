function showInput(event){
    event.preventDefault();
    let str=document.getElementById("text");
    let userName= document.forms[0].elements.name.value;
    let userLN= document.forms[0].elements.lastName.value;
    str.textContent=`{"name":"${userName}","lastName":${userLN}}`
}