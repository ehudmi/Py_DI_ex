// 1rst Daily Challenge
// Create two functions. Each function should return a promise.
// The first function called makeAllCaps(), takes an array of words as an argument
// If all the words in the array are strings, resolve the promise. The value of the resolved promise is the array of words uppercased.
// else, reject the promise with a reason.
// The second function called sortWords(), takes an array of words uppercased as an argument
// If the array length is bigger than 4, resolve the promise. The value of the resolved promise is the array of words sorted in alphabetical order.
// else, reject the promise with a reason.
// Test:

// //in this example, the catch method is executed
// makeAllCaps([1, "pear", "banana"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result))
//       .catch(error => console.log(error))

// //in this example, the catch method is executed
// makeAllCaps(["apple", "pear", "banana"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result))
//       .catch(error => console.log(error))

// //in this example, you should see in the console, 
// // the array of words uppercased and sorted
// makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
//       .catch(error => console.log(error))


// Output:
// output
function makeAllCaps(arr){
    return new Promise((resolve, reject) => {
        let output=[];
        let len=arr.length;
        for(let x=0;x<len;x++){
            if(typeof(arr[x])!=="string"){
                reject(`The element at index ${x} is not a string`);
            }
            output.push(arr[x].toUpperCase());
        }
        resolve(output);
    })
}

function sortWords(arr){
    return new Promise((resolve, reject) => {
        if(arr.length<4){
            reject(`The array only has ${arr.length} elements while it needs 4 minimum`);
        }
        resolve(arr.sort());
    })
}
// makeAllCaps(["kiwi", "pear", "banana", "apple"])
//       .then((arr) => sortWords(arr))
//       .then((result) => console.log(result))
//       .catch(error => console.log(error))

// 2nd Daily Challenge
const morse = `{
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}`
// Create three functions. The two first functions should return a promise..

// The first function is named toJs():
// this function converts the morse json string provided above to a morse javascript object.
// if the morse javascript object is empty, throw an error (use reject)
// else return the morse javascript object (use resolve)
function toJs(json){
    return new Promise((resolve, reject) => {
        let obj= JSON.parse(json);
        if(Object.entries(obj).length=0){
            reject("The json is empty!")
        };
        resolve(obj);
    })
}
// The second function called toMorse(morseJS), takes one argument: the new morse javascript object.

// This function asks the user for a word or a sentence.
// if the user entered a character that doesn’t exist in the new morse javascript object, throw an error. (use reject)
// else return an array with the morse translation of the user’s word.
// if the user enters the word "Hello", the promise resolves with this value ["....", ".", ".-..", ".-..","---"]
// if the user entered the word "¡Hola!", the promise rejects because the character "¡" doesn't exist in the morse javascript object
function toMorse(obj){
    let input=prompt("Enter a sentence to translate to morse code");
    let arr=String(input).toLowerCase().replace(/\s/g,"").split("");;
    let output=[];
    return new Promise((resolve, reject) => {
        arr.forEach(item=>{
            if(!Object.keys(obj).includes(item)){
                reject(`The character ${item} doesn't exist in morse!`);
            }
            else{
                output.push(obj[item]);
            }
        })
        resolve(output);
    })
}

// The third function called joinWords(morseTranslation), takes one argument: the morse translation array

// this function joins the morse translation by using line break and display it on the page (ie. On the DOM)

// Chain the three functions.
// Example:
// "Hello" gives you
// ....
// .
// .-..
// .-..
// ---
function joinWords(translation){
    let body=document.body;
    translation.forEach(item=>{
        let div=document.createElement("div");
        div.textContent=item;
        body.appendChild(div);
    })
}

toJs(morse).then(result=>toMorse(result))
.then(result=>joinWords(result))
.catch(error=>console.log(error));