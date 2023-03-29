// Instructions
// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”.
// For example, “The movie is not that bad, I like it”.

// Create a variable called wordNot where it’s value is the first appearance (ie. the position) of the substring “not” (from the sentence variable).

// Create a variable called wordBad where it’s value is the first appearance (ie. the position) of the substring “bad” (from the sentence variable).

// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
// For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.
// Example:

//   Your string is : 'This dinner is not that bad ! You cook well', 
//   --> the result is : 'This dinner is good ! You cook well'

//   Your string is : 'This movie is not so bad !' 
//   --> the result is : 'This movie is good !'

//   Your string is : 'This dinner is bad !' 
//   --> the result is : 'This dinner is bad !'

let sentence= "This is not good, this is bad";
let wordBad= sentence.search("bad");
let wordNot= sentence.search("not");
var part1Sentence= sentence.substring(0, wordNot-1);
var part2Sentence= sentence.substring(wordBad+3);
var checker= sentence.substring(wordNot, wordBad);
if (wordBad>wordNot && wordNot > 0 && checker.search(",")<0)
{
    part1Sentence= part1Sentence.concat(" good");
    console.log(part1Sentence.concat(part2Sentence));
}
else
    console.log(sentence);