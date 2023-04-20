// Exercise 1
// Analyse the code below without running it, what will be the output ?

// var num = 8;
// var num = 10;
// console.log(num);
// the output is 10.
// Exercise 2
// function numbers() {
//   for (var i = 0; i < 5; i += 1) {
//     console.log(i);
//   }
//     console.log(i);
// }
// numbers();
// Change the code so the var i will be undefined outside of the for loop
// function numbers() {
//   for (let i = 0; i < 5; i += 1) {
//     console.log(i);
//   }
//     console.log(i);
// }
// numbers();
// Exercise 3
// You have to decide which type of variables you have to use

// Create a global variable that save the amount of money you have in your account
// Create a variable that saves the amount of VAT
// Create a variable that saves the amout of all the expenses and revenu you did /received for the past last month
// Create a JS code that multiplies of the expenses by the VAT
// Create a JS code that changes the amount of the money you have in your account depending on your expenses/revenu.
// Display it
let money=0;
const vat=0.17;
let expenses=0;
let revenue=0;
console.log(`your VAT expenses are ${expenses*vat}`);
money= money+revenue-expenses;
console.log(`your new balance is ${money}`);