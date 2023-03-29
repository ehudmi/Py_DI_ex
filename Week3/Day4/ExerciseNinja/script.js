// Exercise 1 : Age Difference
// Instruction
// Given the years two people were born, find the date when the younger one is exactly half the age of the older.
// Notes: The dates are given in the format YYYY
let firstAge= prompt("Give me the first year of birth!");
firstAge = Number(firstAge);
let seconedAge= prompt("Give me the seconed year of birth!");
seconedAge= Number(seconedAge);
let num = 0;
if(firstAge>seconedAge)
{
    num= (firstAge-seconedAge)+firstAge;
    num= String(num);
    num="The age difference will be exactly half in ".concat(num); 
    alert(num);
}
else if(seconedAge>firstAge)
 {
    num= (seconedAge-firstAge)+seconedAge;
    num= String(num);
    num="The age difference will be exactly half in ".concat(num); 
    alert(num);
}
else{
    alert("They were born on the same year!");
}

// Exercise 2 : Zip Codes
// Instruction
// Harder exercise
// Hint : This exercise has 2 parts. First, do this exercise without Regular Expressions, then do it using Regular Expressions

// While working in a Post Office you must have the clients’ zip code in order to send them their letters.
// Ask the client for their zip code and console.log “success” or “error” based on the following rules.
// Zip codes consists of 5 numbers
// Must only contain numbers
// Must not contain any whitespace (spaces)
// Must not be greater than 5 digits in length
// let zipCode= prompt("Enter your zip code");
// Without RegEx
if(zipCode.length == 5 && !isNaN(Number(zipCode)))
{
    console.log("Success!");
}
else{
    console.log("Error");
}
// With RegEx
let pattern= /[^0-9]/;
if(zipCode.length==5 && !zipCode.match(pattern))
{
        console.log("Success!");
}
else{
    console.log("Error");
}

// Exercise 3 : Secret Word
// Instruction
// Harder exercise
// Hint : Use Regular Expressions

// Prompt the user for a word and save it to a variable.
// Delete all the vowels of the word and console.log the result.
// Bonus: Replace the vowels with another character and console.log the result
// a = 1
// e = 2
// i = 3
// o = 4
// u = 5
let inputWord= prompt("Give me a word, any word");
inputWord= inputWord.replace(/a/g,"1");
inputWord= inputWord.replace(/e/g, "2");
inputWord= inputWord.replace(/i/g, "3");
inputWord= inputWord.replace(/o/g, "4");
inputWord= inputWord.replace(/u/g, "5");
console.log(inputWord);