// Exercise 1: Random Number
// Instructions
// Get a random number between 1 and 100.
// Console.log all even numbers from 0 to the random number.
// let RandNum= () =>
// {
//     let numArray=[];
//     let num= Math.floor((Math.random() * 100) + 1);
//     console.log(num);
//     for(let x=1;x<=num;x++)
//     {
//         x%2==0?numArray=numArray.concat(x):numArray=numArray;
//     }
//     console.log(numArray);
// }
// RandNum()

// Exercise 2: Capitalized Letters
// Instructions
// Create a function that takes a string as an argument.
// Have the function return:
// The string but all letters in even indexes should be capitalized.
// The string but all letters in odd indexes should be capitalized.
// Note:

// Index 0 will be considered even.
// The argument of the function should be a lowercase string with no spaces.
// For example,

// capitalize("abcdef") will return ['AbCdEf', 'aBcDeF']
// let capitalize= (str) =>
// {
//     let output= ["",""];
//     for(let i=0;i<str.length;i++)
//     {
//         if(i%2==0)
//         {
//             output[0]=output[0]+str[i].toUpperCase();
//             output[1]=output[1]+str[i].toLowerCase();
//         }
//         else
//         {
//             output[0]=output[0]+str[i].toLowerCase();
//             output[1]=output[1]+str[i].toUpperCase();
//         }
//     }
//     return output;
// }
// console.log(capitalize("abcdefg"))

// Exercise 3 : Is Palindrome?
// Instructions
// Write a JavaScript function that checks whether a string is a palindrome or not.
// Note A palindrome is a word, phrase or sequence that is spelled the same both backwards and forward, e.g., madam, bob or kayak.
// palindrome
// let checkPal = (inputWord) => {
// 	inputWord = inputWord.toLowerCase();
// 	let bool = true;
// 	for (let i = 0; i < inputWord.length; i++) {
// 		if (inputWord[i] !== inputWord[inputWord.length - 1 - i]) {
// 			bool = false;
// 		}
// 	}
// 	return bool;
// };
// console.log(checkPal("racecar"));

// Exercise 4 : Biggest Number
// Instructions
// Create a function called biggestNumberInArray(arrayNumber) that takes an array as a parameter and returns the biggest number.
// Note : This function should work with any array;
// Example:

// const array = [-1,0,3,100, 99, 2, 99] ;// should return 100 
// const array2 = ['a', 3, 4, 2]; // should return 4 
// const array3 = []; // should return 0
// let biggestNumberInArray = (Array)=>
// {
//     let bigNumb=null;
//     for(let x in Array)
//     {
//         if(isNaN(Array[x]))
//         {
//             continue;
//         }
//         else if(bigNumb==null||Array[x]>bigNumb)
//         {
//             bigNumb=Array[x];
//         }
//     }
//     return Number(bigNumb)
// }
// console.log(biggestNumberInArray(['a', 3, 4, 2]));

// Exercise 5: Unique Elements
// Instructions
// Write a JS function that takes an array and returns a new array with only unique elements.

// Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]
// Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]