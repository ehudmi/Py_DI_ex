// 🌟 Exercise 1 : Scope
// Instructions
// Analyse the code below, and predict what will be the value of a in all the following functions.
// Write your prediction as comments in a js file. Explain your predictions.
// // #1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }

// // #1.1 - run in the console:
// funcOne()
//a will be 3.
// // #1.2 What will happen if the variable is declared 
// // with const instead of let ?
//an error will pop up because we are trying to force a different value to a const.

// //#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }
// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// // #2.1 - run in the console:
// funcThree()
// funcTwo()
// funcThree()
// a is 0, then is 5, then is 5. it willbe alerted once is 0, then once as 5.
// // #2.2 What will happen if the variable is declared 
// // with const instead of let ?
//it will be alerted once as 0, then an error will pop when trying to call funcTwo.


// //#3
// function funcFour() {
//     window.a = "hello";
// }

// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // #3.1 - run in the console:
// funcFour()
// funcFive()
//it will alert in a window "hello".
// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }


// // #4.1 - run in the console:
// funcSix()
//it will alert "test".
// // #4.2 What will happen if the variable is declared 
// // with const instead of let ?
//it will alert "test" because we assign a value to a different parameter in the function (should not do in real code!).

// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// // #5.1 - run the code in the console
// // #5.2 What will happen if the variable is declared 
// // with const instead of let ?
//the same thing.


// 🌟 Exercise 2 : Ternary Operator
// Instructions
// Using the code below:
// function winBattle(){
//     return true;
// }

// Transform the winBattle() function to an arrow function.
// Create a variable called experiencePoints.
// Assign to this variable, a ternary operator. If winBattle() is true, the experiencePoints variable should be equal to 10, else the variable should be equal to 1.
// Console.log the experiencePoints variable.
const winBattle=()=>{ return true}
let experiencePoints;
winBattle()===true?experiencePoints=10:experiencePoints=1;
console.log(experiencePoints);

// 🌟 Exercise 3 : Is It A String ?
// Instructions
// Write a JavaScript arrow function that checks whether the value of the argument passed, is a string or not. Use ternary operator
// Check out the example below to see the expected output
// Example:

// console.log(isString('hello')); 
// //true
// console.log(isString([1, 2, 4, 0]));
// //false
let isString= arg => { return typeof arg=="string"?true:false}
// 🌟 Exercise 4 : Colors
// Instructions
// Using this array :

const colors1 = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
// Write a JavaScript program that displays the colors in the following order : “1# choice is Blue.” “2# choice is Green.” “3# choice is Red.” ect…
// Check if at least one element of the array is equal to the value “Violet”. If yes, console.log("Yeah"), else console.log("No...")
// Hint : Use the array methods taught in class. Look at the lesson Array Methods.
colors1.forEach((item, index)=>
{
    console.log(`${index}# choice is ${item}.`)
})
colors1.includes("Violet")==true?console.log("Yeah"):console.log("No...")

// 🌟 Exercise 5 : Colors #2
// Instructions
// Using these arrays :

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];
// Write a JavaScript program that displays the colors in the following order : “1st choice is Blue .” “2nd choice is Green.” “3rd choice is Red.” ect…
// Hint : Use the array methods taught in class and ternary operator.
colors.forEach((item, index)=>
{
    let str;
    index>2?str=ordinal[0]:str=ordinal[index+1];
    console.log(`${index+1}${str} choice is ${item}`);
})

// Exercise 6 : Bank Details
// Instructions
// In this exercise, you have to decide which type of variables you have to use (ie. let or const):

// Create a global variable called bankAmount which value is the amount of money currently in your account.
// Create a variable that saves the % amount of VAT (In Israel, it’s 17%).
// Create an array with all your monthly expenses, both positive and negative (money made and money spent).
// Example : const details = ["+200", "-100", "+146", "+167", "-2900"]
// Create a program that modifies the expenses (ie. the positive AND the negative expenses) so that they will include taxes (multiply each expense by the VAT).
// Display your current bankAccount standing at the end of the month.
let bankAmount= 2000;
const VAT=0.17;
const details=[200, -1200, 500, 700, 3000, -2000];
details.forEach(moneyChange=>
    {
        moneyChange>=0?moneyChange=moneyChange-VAT*moneyChange:moneyChange=moneyChange+VAT*moneyChange;
        bankAmount=bankAmount+moneyChange;
    })
console.log(bankAmount);