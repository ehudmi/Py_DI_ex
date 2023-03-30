// Exercise 1 : Favorite Color
// Instructions
let sentence = ["my", "favorite", "color", "is", "blue"];
// Write some simple Javascript code that will join all the items in the array above, and console.log the result.

console.log(sentence.join(" "));

// Exercise 2 : Mixup
// Instructions
// Create 2 variables. The values should be strings. For example:
// let str1 = "mix";
// let str2 = "pod";

let str1 = "magic";
let str2 = "fudge";

// 2. Slice out and swap the first 2 characters of the two strings from part 1.

tempSlice = str1.slice(0, 2);
str1 = str2.slice(0, 2) + str1.slice(2);
str2 = tempSlice + str2.slice(2);

// 3. Create a third variable where the value is the concatenation of the two strings from the part 1 (separated by a space).

let str3 = str1 + " " + str2;

// 4. Finally console.log the new concatenated string.
console.log(str3);

// Some Examples

// let str1 = "mix";
// let str2 = "pod";
// let newWord should be equal to 'pox mid'

// let firstWord = "Hello";
// let secondWord = "World";
// let thirdWord should be equal to 'Wollo Herld'

// Exercise 3 : Calculator
// Instructions
// Make a Calculator. Follow the instructions:

// Prompt the user for the first number.
// Store the first number in a variable called num1.
// Hint : console.log the type of the variable num1. What should you do to convert it to a number ?
// Prompt the user for the second number.
// Store the second number in a variable called num2.
// Create an Alert where the value is the SUM of num1 and num2.
// BONUS: Make a program that can subtract, multiply, and also divide!

let num1 = Number(prompt("Please input the first number"));
let num2 = Number(prompt("Please input the second number"));
let operation = prompt("select operation type using + or - or * or /");
let result;
switch (operation) {
	case "+":
		result = num1 + num2;
		break;
	case "-":
		result = num1 - num2;
		break;
	case "*":
		result = num1 * num2;
		break;
	case "/":
		result = num1 / num2;
		break;
}
alert(result);
