// Exercise 1 : Evaluation
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.

// Evaluate the comparisons found below:

// Look at this link for help

5 >= 1;
// Prediction:true
// Actual:
// Explanation:5 is bigger than 1

0 === 1;
// Prediction:false
// Actual:
// Explanation:0 is not equal to 1

4 <= 1;
// Prediction:false
// Actual:
// Explanation:4 is not smaller or equal to 1

1 != 1;
// Prediction:false
// Actual:
// Explanation:1 is equal to 1

"A" > "B";
// Prediction:NaN
// Actual:false
// Explanation:when comparing string single characters their ASCI code value is compared

"B" < "C";
// Prediction:NaN
// Actual:true
// Explanation:when comparing string single characters their ASCI code value is compared

"a" > "A";
// Prediction:NaN
// Actual:true
// Explanation:when comparing string single characters their ASCI code value is compared

"b" < "A";
// Prediction:NaN
// Actual:false
// Explanation:when comparing string single characters their ASCI code value is compared

true === false;
// Prediction:false
// Actual:false
// Explanation:true is not the same as false

true != true;
// Prediction:false
// Actual:false
// Explanation:true can not be false

// Exercise 2 : Ask For Numbers
// Instructions
// Ask the user for a string of numbers separated by commas
// Console.log the sum of the numbers.
// Hint: use some string methods
// Examples
// "2,3"➞ 5

// let numbersString = prompt(
// 	"Please insert a string of numbers separated by commas"
// );
// let stringArray = numbersString.split(",");
// let calc = stringArray.reduce((total, value) => {
// 	return Number(total) + Number(value);
// });
// console.log(calc);

// Exercise 3 : Find Nemo
// Instructions
// Hint: if statement (tomorrow’s lesson)

// Ask the user to give you a sentence containing the word “Nemo”. For example "I love the movie named Nemo"
// Find the word “Nemo”
// Console.log a string as follows: "I found Nemo at [the position of the word Nemo]".
// If you can’t find Nemo, console.log “I can’t find Nemo”.
// Some examples:

// "I love the movie named Nemo" ➞ "I found Nemo at 5"
// "Nemo is a cute fish" ➞ "I found Nemo at 0"
// "My fish is called Nemo, I love it" ➞ "I found Nemo at 4"

// let sentence = prompt("please give me a sentence containing the word “Nemo”");
// if (sentence.search("Nemo") > 0) {
// 	let sentenceArray = sentence.split(" ");
// 	console.log("I found Nemo at " + sentenceArray.indexOf("Nemo"));
// } else console.log("I can’t find Nemo");

// Exercise 4 : Boom
// Instructions
// Hint: if statement (tomorrow’s lesson)

// Prompt the user for a number. Depending on the users number you will return a string of the word “Boom”. Follow the rules below:

// If the number given is less than 2 : return “boom”
// If the number given is bigger than 2 : the string should include n number of “o”s (n being the number given)
// If the number given is evenly divisible by 2, add a exclamation mark to the end.
// If the number given is evenly divisible by 5, return the string in ALL CAPS.
// If the number given is evenly divisible by both 2 and 5, return the string in ALL CAPS and add an exclamation mark to the end.
// Examples
// 4 ➞ "Boooom!"
// There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)
// 1 ➞ "boom"
// 1 is lower than 2, so we return "boom"

let numberString = prompt("Please give me a number");
let userNumber = Number(numberString);
console.log(userNumber);
let result;
if (isNaN(userNumber)) {
	result = "Are you fucking with me?";
	alert(result);
} else if (userNumber < 2) {
	result = "boom";
	alert(result);
} else if (userNumber > 2) {
	result = "b" + "o".repeat(userNumber) + "m";
	if (userNumber % 2 == 0 && userNumber % 5 == 0) {
		result = result.toUpperCase() + "!";
	} else if (userNumber % 2 == 0) {
		result = result + "!";
	} else if (userNumber % 5 == 0) {
		result = result.toUpperCase();
	}
	alert(result);
}
