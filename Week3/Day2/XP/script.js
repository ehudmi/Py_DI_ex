// Exercise1

// Store your favorite food into a variable.
// Store your favorite meal of the day into a variable (ie. breakfast, lunch or dinner)
// Console.log I eat <favorite food> at every <favorite meal>

let food="chocolate"
let meal="lunch"
console.log("I eat "+food+" at every "+meal)

// Exercise 2
// Part I
// Using this array : const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

// Create a variable named myWatchedSeriesLength that is equal to the number of series in the myWatchedSeries array.

// Create a variable named myWatchedSeriesSentence, that is equal to a sentence describing the series you watched
// For example : black mirror, money heist, and the big bang theory

// Console.log a sentence using both of the variables created above
// For example : I watched 3 series : black mirror, money heist, and the big bang theory

const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"]
const myWatchedSeriesLength=myWatchedSeries.length
const myWatchedSeriesSentence="black mirror, money heist, and the big bang theory"
console.log("I watched "+myWatchedSeriesLength+" series: "+myWatchedSeriesSentence)

// Part II
// Change the series “the big bang theory” to “friends”. Hint : You will need to use the index of “the big bang theory” series.
// Add, at the end of the array, the name of another series you watched.
// Add, at the beginning of the array, the name of your favorite series.
// Delete the series “black mirror”.
// Console.log the third letter of the series “money heist”.
// Finally, console.log the myWatchedSeries array, to see all the modifications you’ve made.

myWatchedSeries[2]="friends"
myWatchedSeries.push("sherlock holmes")
myWatchedSeries.unshift("ozark")
myWatchedSeries.splice(1,1)
console.log(myWatchedSeries[1].charAt(2))
console.log(myWatchedSeries)

// 🌟 Exercise 3 : The Temperature Converter
// Instructions
// Store a celsius temperature into a variable.

// Convert it to fahrenheit and console.log <temperature>°C is <temperature>°F.
// Hint : Should you create another variable to hold the temperature in fahrenheit? (ie. point 2)
// Hint: To convert a temperature from celsius to fahrenheit : Divide it by 5, then multiply it by 9, then add 32

let temp=36
console.log(temp+"C is "+temp/5*9+32+"F")

// 🌟 Exercise 4 : Guess The Answers #1
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.

let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction:55
// Actual:55
// Explanation: it's a regular addition action - 34+21=55

a = 2;

console.log(a+b) //second expression
// Prediction:23
// Actual:23
// Explanation: it's a regular addition action - a has a new value 2+21=23

console.log(c)
// What is the value of c?
// c is undefined
// Explanation: c is declared but not yet defined

console.log(3 + 4 + '5');
// Prediction:75
// Actual:75
// Explanation: it's a regular addition action for the first 2 variables -3+4=7 and then a concatenation - 7+"5"=75

// Exercise 5 : Guess The Answers #2
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.

typeof(15)
// Prediction:Number
// Actual:Number
// Explanation - 15 is a number

typeof(5.5)
// Prediction:Number
// Actual:Number
// Explanation - even if not an integer it is still a number

typeof(NaN)
// Prediction:NaN
// Actual:Number
// Explanation:A NaN value qualifies as number

typeof("hello")
// Prediction:String
// Actual:String

typeof(true)
// Prediction:Boolean
// Actual:Boolean
// Explanation:true and false are Boolean values

typeof(1 != 2)
// Prediction:Boolean
// Actual:Boolean
// Explanation:true and false are Boolean values. In this case the expression is true

"hamburger" + "s"
// Prediction:hamburgers
// Actual:hamburgers
// Explanation:the + is a concatenation operator in the case of string values

"hamburgers" - "s"
// Prediction:hamburger
// Actual:NaN
//Explanation: the subtraction can't be performed as the values are strings

"1" + "3"
// Prediction:13
// Actual:13
// Explanation:the + is a concatenation operator in the case of string values 

"1" - "3"
// Prediction:NaN
// Actual:-2
// Explanation:the - is magically interpreted as subtraction because the string values can be parse as numbers

"johnny" + 5
// Prediction:johnny5
// Actual:johnny5
// Explanation:the + is a concatenation operator in the case of string values

"johnny" - 5
// Prediction:NaN
// Actual:NaN
//Explanation: the subtraction can't be performed as one of the values is a string


99 * "hello"
// Prediction:NaN
// Actual:NaN
//Explanation: the multiplication can't be performed as as one of the values is a string

1 != 1
// Prediction:False
// Actual:False

1 == "1"
// Prediction:True
// Actual:True
// Explanation:the type of the variable is ignored and only the values are compared

1 === "1"
// Prediction:False
// Actual:False
// Explanation:the type of a number and string are not the same

// Exercise 6 : Guess The Answers #3
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.



// What is the output of each of the expressions below?


5 + "34"
// Prediction:534
// Actual:534
// Explanation:the + is a concatenation operator in the case of string values even if one is a number

5 - "4"
// Prediction:1
// Actual:1
// Explanation:the - is magically interpreted as subtraction because the string values can be parse as numbers

10 % 5
// Prediction:0
// Actual:0
// Explanation:10 can be divided by 5 with no remainder

5 % 10
// Prediction:5
// Actual:5
// Explanation:5 can't be divided by 10 and the remainder is therefore 5

"Java" + "Script"
// Prediction:JavaScript
// Actual:JavaScript
// Explanation:the + is a concatenation operator in the case of string values

" " + " "
// Prediction:   (2 spaces)
// Actual:  (2 blank spaces)
// Explanation:even a concatenation of two spaces is a string

" " + 0
// Prediction: 0 (blank space followed by 0)
// Actual: 0 (blank space followed by 0)
// Explanation:even a concatenation of two spaces is a string

true + true
// Prediction:2
// Actual:2
// Explanation:true evaluates as 1 and false 0 and in conjunction with math operations they are processed as such

true + false
// Prediction:1
// Actual:1
// Explanation:true evaluates as 1 and false 0 and in conjunction with math operations they are processed as such

false + true
// Prediction:1
// Actual:1
// Explanation:true evaluates as 1 and false 0 and in conjunction with math operations they are processed as such

false - true
// Prediction:-1
// Actual:-1
// Explanation:true evaluates as 1 and false 0 and in conjunction with math operations they are processed as such

!true
// Prediction:false
// Actual:false
// Explanation:not true is false

3 - 4
// Prediction:-1
// Actual:-1
// Explanation:math operation can result in negative values

"Bob" - "bill"
// Prediction:NaN
// Actual:NaN
//Explanation: the subtraction can't be performed as the values are strings