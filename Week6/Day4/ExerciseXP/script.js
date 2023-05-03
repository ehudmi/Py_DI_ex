// 🌟 Exercise 1 : Find The Sum
// Instructions
// Create a one line function (ie. an arrow function) that receives two numbers as parameters and returns the sum.
// let sum= (para1, para2)=>para1+para2;

// 🌟 Exercise 2 : Kg And Grams
// Instructions
// Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)
// function kilo1(weight) {
//     return weight*1000;
// }

// let kilo2= weight=>weight*1000
//the difference is I cant invoke kilo2 before I define it while kilo1 is hoisted.
// First, use function declaration and invoke it.
// Then, use function expression and invoke it.
// Write in a one line comment, the difference between function declaration and function expression.
// Finally, use a one line arrow function and invoke it.


// 🌟 Exercise 3 : Fortune Teller
// Instructions
// Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
// The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."
// (function (childNum,partName,geo,job){
//     let text=document.createElement("div");
//     text.textContent=`You will be a ${job} in ${geo}, and married to ${partName} with ${childNum} kids.`
//     document.body.appendChild(text);
// })(4, "Jessy", "London","Data Analyst");

// 🌟 Exercise 4 : Welcome
// Instructions
// John has just signed in to your website and you want to welcome him.

// Create a Bootstrap Navbar in your HTML file.
// In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
// The function should add a div in the nabvar, displaying the name of the user and his profile picture.
// (function (username) {
//     console.log("Hi");
//     let container= document.createElement("div");
//     container.className="container-fluid";
//     let brand=document.createElement("a");
//     brand.className="navbar-brand";
//     container.appendChild(brand);
//     document.getElementsByTagName("nav")[0].appendChild(container);
//     let text=document.createElement("img");
//     text.src="https://www.pngitem.com/pimgs/m/150-1503945_transparent-user-png-default-user-image-png-png.png";
//     text.alt="ProfilePic";
//     text.width="30";
//     text.height="24";
//     text.className="d-inline-block align-text-top";
//     brand.appendChild(text);
//     brand.textContent=`Hello ${username}`;
// })("David");

// 🌟 Exercise 5 : Juice Bar
// Instructions
// You will use nested functions, to open a new juice bar.

// Part I:
// The outer function named makeJuice receives 1 argument: the size of the beverage the client wants - small, medium or large.

// The inner function named addIngredients receives 3 ingredients, and displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".

// Invoke the inner function ONCE inside the outer function. Then invoke the outer function in the global scope.
// let makeJuice=(size)=>
// {
//     let ingredients=[];
//     function addIngredients(ing1, ing2, ing3) {
//             ingredients.push(ing1);
//             ingredients.push(ing2);
//             ingredients.push(ing3);
//             let order=document.createElement("div");
//             order.textContent=`The client wants a ${size} drink, containing`;
//             ingredients.forEach(item=> {
//                 order.textContent=order.textContent+`, ${item}`;
//             })
//             document.body.appendChild(order);
//     }
//     return addIngredients;
// }
// makeJuice("Large")("Milk","Cheese","Honey");

// Part II:
// In the makeJuice function, create an empty array named ingredients.

// The addIngredients function should now receive 3 ingredients, and push them into the ingredients array.

// Create a new inner function named displayJuice that displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>". Use the forEach method.

// The client wants 6 ingredients in his juice, therefore, invoke the addIngredients function TWICE. Then invoke once the displayJuice function. Finally, invoke the makeJuice function in the global scope.
// let makeJuice=(size)=>
// {
//     let ingredients=[];
//     let count=0;
//     function addIngredients(ing1, ing2, ing3) {
//             ingredients.push(ing1);
//             ingredients.push(ing2);
//             ingredients.push(ing3);
//     }
//     function displayJuice() {
//         let order=document.createElement("div");
//             order.textContent=`The client wants a ${size} drink, containing`;
//             ingredients.forEach(item=> {
//                 order.textContent=order.textContent+`, ${item}`;
//             })
//             document.body.appendChild(order);
//     }
//     addIngredients("Salt","Vinegar","Pepper");
//     addIngredients("Milk","Sugar","Honey");
//     displayJuice();
// }
// makeJuice("Large");