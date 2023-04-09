// Exercise 1 : Is_Blank
// Instructions
// Write a program to check whether a string is blank or not.

// console.log(isBlank('')); --> true
// console.log(isBlank('abc')); --> false
let isBlank= (str) =>
{
    str= String(str);
    str= str.replace(/\s/g,"")
   let value= (str ==``? true:false);
   return value
}
console.log(isBlank("  "))


// Exercise 2 : Abbrev_name
// Instructions
// Write a JavaScript function to convert a string into an abbreviated form.
// console.log(abbrevName("Robin Singh")); --> "Robin S."
let abbrevName= (full_name)=>
{
    let space= full_name.search(" ");
    let abbrev=full_name.slice(0, space+2);
    console.log(`${abbrev}.`)
}
abbrevName("Ehud Miron");


// Exercise 3 : SwapCase
// Instructions
// Write a JavaScript function which takes a string as an argument and swaps the case of each character.
// For example :

// if you input 'The Quick Brown Fox' 
// the output should be 'tHE qUICK bROWN fOX'.
let swapCase= (input) =>
{
    output="";
    for(let x=0; x<input.length;x++)
    {
        let char=input[x].toLowerCase();
        char==input[x]? char= char.toUpperCase():char=char;
        output=output+char;
    }
    return output;
}
console.log(swapCase("The Quick Fox"));


// Exercise 4 : Omnipresent Value
// Instructions
// Create a function that determines whether an argument is omnipresent for a given array.
// A value is omnipresent if it exists in every subarray inside the main array.
// To illustrate:

// [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
// // 3 exists in every element inside this array, so is omnipresent.
// Examples

// isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ true
// isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ false
let isOmnipresent= (array, value) =>
{
    for(let index=0;index<array.length;index++)
    {
        if(!array[index].includes(value))
        {
            return false;
        }
    }
    return true;
}
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6));