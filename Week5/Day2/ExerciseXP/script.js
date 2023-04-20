// 🌟 Exercise 1 : Change The Article
// Instructions
// Copy the code below, into a structured HTML file:

// <article>
//     <h1> Some Facts </h1>
//     <h2> The Chocolate </h2>
//     <h3> History of the chocolate </h3>
//     <p> Chocolate is made from tropical Theobroma cacao tree seeds. 
//     Its earliest use dates back to the Olmec civilization in Mesoamerica.</p>
//     <p> After the European discovery of the Americas, chocolate became 
//     very popular in the wider world, and its demand exploded. </p>
//     <p> Chocolate has since become a popular food product that millions enjoy every day, 
//     thanks to its unique, rich, and sweet taste.</p> 
//     <p> But what effect does eating chocolate have on our health?</p> 
// </article>


// Using a DOM property, retrieve the h1 and console.log it.
// console.log(document.body.firstElementChild.firstElementChild);
// // Using DOM methods, remove the last paragraph in the <article> tag.
// document.getElementsByTagName("p")[3].remove();
// // Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
// let h2= document.getElementsByTagName("h2")[0];
// let changeToRed= ()=>
// {
//     h2.style.color= "red";
// }
// h2.addEventListener("click",changeToRed);
// // Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
// let h3= document.getElementsByTagName("h3")[0];
// let hide= ()=>
// {
//     h3.style.display="none";
// }
// h3.addEventListener("click",hide);
// // Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
// let button= document.createElement("button");
// document.body.appendChild(button);
// button.style.width= "100%";
// button.innerText= "Bold!!";
// let para= document.getElementsByTagName("p");
// let bold= () =>
// {
//     for(let x=0;x<para.length;x++)
//     {
//         para[x].style.fontWeight= "bold";
//     }
// }
// button.addEventListener("click", bold);
// // BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)
// let h1= document.getElementsByTagName("h1")[0];
// let randFont= () =>
// {
//     h1.style.fontSize= `${Math.round(Math.random()*100)}px`;
// }
// h1.addEventListener("mouseover",randFont);
// // BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
// para[1].style.transition= "opacity 2s";
// let anim= () =>
// {
//     para[1].style.opacity= "0";
// }
// para[1].addEventListener("mouseover",anim);


// 🌟 Exercise 2 : Work With Forms
// Instructions
// Copy the code below, into a structured HTML file:

// <form>
//   <label for="fname">First name:</label><br>
//   <input type="text" id="fname" name="fname"><br>
//   <label for="lname">Last name:</label><br>
//   <input type="text" id="lname" name="lname"><br><br>
//   <input type="submit" value="Submit" id="submit">
// </form> 
// <ul class="usersAnswer"></ul>


// Retrieve the form and console.log it.
// console.log(document.forms[0]);
// // Retrieve the inputs by their id and console.log them.
// console.log(document.getElementById("fname"));
// console.log(document.getElementById("lname"));
// console.log(document.getElementById("submit"));
// // Retrieve the inputs by their name attribute and console.log them.
// console.log(document.forms[0].elements);
// let form1= document.forms[0];
// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ?
// so the page doesn't refresh.
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.
// The output should be :
// let submission= ()=>
// {
//     for(let x=0;x<2;x++)
//     {
//         let input=form1.elements[x].value;
//         if(input=="")
//         {
//             alert("please fill all text boxes");
//             return;
//         }
//         let li= document.createElement("li");
//         li.textContent=input;
//         document.body.lastElementChild.appendChild(li);
//     }
//     event.preventDefault();
// }

// form1.addEventListener("submit",submission);
// <ul class="usersAnswer">
//     <li>first name of the user</li>
//     <li>last name of the user</li>
// </ul>


// 🌟 Exercise 3 : Transform The Sentence
// Instructions
// Add this sentence to your HTML file then follow the steps :

// <p><strong>Hello</strong> I hope you are enjoying <strong>this</strong> class. At the
// <strong>end</strong> you <strong>will</strong> be great Developers!
// <strong>Enjoy</strong> the <strong>JavaScript </strong> lessons</p>


// In the JS file:

// Declare a global variable named allBoldItems.
let allBoldItems=[];
// Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.
let getBold_items= ()=>
{
    for(let x=0;x<document.getElementsByTagName("strong").length;x++)
    {
        allBoldItems.push(document.getElementsByTagName("strong")[x].textContent);  
    }
}
getBold_items();
console.log(allBoldItems);
// Create a function called highlight() that changes the color of all the bold text to blue.

// Create a function called return_normal() that changes the color of all the bold text back to black.

// Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() on mouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example


// 🌟 Exercice 4 : Volume Of A Sphere
// Instructions
// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:
// <!doctype html> 
// <html lang="en"> 
//     <head> 
//         <meta charset="utf-8"> 
//         <title>Volume of a Sphere</title> 
//         <style>  
//             body {
//                 padding-top:30px;
//             } 

//             label,input {
//                 display:block;
//             }  
//         </style> 
//     </head> 
//     <body> 
//         <p>Input radius value and get the volume of a sphere.</p> 
//         <form  id="MyForm"> 
//             <label for="radius">Radius</label><input type="text" name="radius" id="radius" required> 
//             <label for="volume">Volume</label><input type="text" name="volume" id="volume"> 
//             <input type="submit" value="Calculate" id="submit">    
//         </form> 
//     </body> 
// </html> 


// Exercise 5 : Event Listeners
// Instructions
// Add many events listeners to one element on your webpage. Use the click, mouseover, mouseout and dblclick events.
// Each listener should do a different thing, for instance - change position x, change position y, change color, change the font size… and more.