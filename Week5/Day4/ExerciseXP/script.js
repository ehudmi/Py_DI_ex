// 🌟 Exercise 1 : Timer

// Using this HTML code:

// <!DOCTYPE html>
//     <html>
//     <head>
//         <style>
//         p {
//           background: yellow;
//           color: red;
//         }
//         </style>
//     </head>
//     <body>
//         <div id="container"></div>
//         <button id="clear">Clear Interval</button>
//     </body>
//     </html>


// Part I
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.
// let hello= () =>
// {
//     alert("Hello World");
// }
// setTimeout(hello,2000);
// Part II
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// let para= () =>
// {
//     let par=document.createElement("p");
//     let text=document.createTextNode("Hello World");
//     par.appendChild(text);
//     document.getElementById("container").appendChild(par);
//     if (document.getElementsByTagName("p").length==5)
//     {
//         clear()
//     }
// }
// setTimeout(para,2000);

// Part III
// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.
// let timer=setInterval(para,2000);
// let but= document.getElementById("clear");
// let clear= ()=>
// {
//     clearInterval(timer);
// }
// but.addEventListener("click",clear);


// 🌟 Exercise 2 : Move The Box
// Instructions
// <!DOCTYPE html>
//     <html>
//     <head>
//         <style>
//         #container {
//           width: 400px;
//           height: 400px;
//           position: relative;
//           background: yellow;
//         }
//         #animate {
//           width: 50px;
//           height: 50px;
//           position: absolute;
//           background-color: red;
//         }
//         </style>
//     </head>
//     <body>
//         <p><button onclick="myMove()">Click Me</button></p>
//         <div id="container">
//           <div id="animate"></div>
//         </div>
//     </body>
//     </html>


// Copy the code above, to a structured HTML file.
// In your Javascript file, use setInterval to move the <div id="animate"> to the right side of the <div id="container">, when the button is clicked on.
// The <div id="animate"> should move 1px to the right every milisecond, until it reaches the end of the <div id="container">.
// Hint : use clearInterval as soon as the box reaches the right end side of the container
// Hint : check out the demonstration in the Course Noted named JS Functions
// let pixel=0;
// let box=document.getElementById("animate");
// let myMove=()=>
// {  
//     let clear= ()=>
// {
//     clearInterval(timer);
// }

// let move=() =>
// {
//     pixel++;
//     box.style.left= `${pixel}px`;
//     if(box.style.left==`350px`)
//     {
//         clear();
//     }
// }
// let timer=setInterval(move,1);
// }




// 🌟 Exercise 3: Drag & Drop
// Instructions
// <!DOCTYPE html>
//     <html>
//     <head>
//         <style>
//         #target {
//           width: 200px;
//           height: 200px;
//           position: relative;
//           background: yellow;
//         }
//         #box {
//           width: 50px;
//           height: 50px;
//           position: absolute;
//           background-color: red;
//         }
//         </style>
//     </head>
//     <body>
//         <div id="target"></div>
//         <br>
//         <div id="box"></div>
//     </body>
//     </html>


// Copy the code above, to a structured HTML file.
// In your Javascript file add the functionality which will allow you to drag the box and drop it into the target. Check out the Course Notes named DOM animations.
let box= document.getElementById("box");
box.setAttribute("draggable","true");
box.addEventListener("dragstart",function(event) {
    event.dataTransfer.setData("text/plain",event.target.id);
})
let container= document.getElementById("target");
container.addEventListener("dragover",function(event) {
    event.preventDefault();
})
container.addEventListener("drop", function(event) {
    let data=event.dataTransfer.getData("text/plain");
    let target=document.getElementById(data);
    container.appendChild(target);
})