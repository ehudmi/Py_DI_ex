// Create a function that:

// takes in two strings as two parameters
// and returns a boolean that indicates whether or not the first string is an anagram of the second string.
// Some Help

// What is an anagram?
// An anagram is another word or phrase formed by rearranging letters of the first word or phrase.


// Example of anagrams

// "Astronomer" is an anagram of "Moon starer"
// "School master" is an anagram of "The classroom"
// "The Morse Code" is an anagram of "Here come dots"


// Do we need to consider whitespace?
// Trim whitespace prior to comparison.
function anaChecker(str1,str2){
    str1=str1.toLowerCase().replace(/\s/g,"").split("").sort().join("");
    str2=str2.toLowerCase().replace(/\s/g,"").split("").sort().join("");
    return str1==str2
}

console.log(anaChecker("Astronomer","Moon starer"))