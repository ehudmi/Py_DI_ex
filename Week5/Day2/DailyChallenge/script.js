// In todays exercise we will be creating a Mad Libs game.
// If you’ve never played this game, a mad lib is a game where you fill in a bunch of blank inputs with different word types (ie : noun, adjective, verb), and then a story is generated based on the words you chose, and sometimes the story is surprisingly funny.

// In this exercise you work with the HTML code presented below.

// Follow these steps :

// Get the value of each of the inputs in the HTML file when the form is submitted. Remember the event.preventDefault()
// Make sure the values are not empty
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user). The user could click the button at least three times and get a new story. Display the stories randomly.
let storyForm=document.forms[0];
let wordList=[];
let randomWord= (array)=>
{

    let randIndex=Math.round(Math.random()*(array.length-1));
    let randWord=array[randIndex];
    array.splice(randIndex,1);
    return randWord;
}

let createStory= ()=> {
    for(let x=0;x< storyForm.getElementsByTagName("input").length;x++)
    {
        if(storyForm.elements[x].value=="")
        {
            console.log(storyForm.ele)
            alert("Please fill the whole form");
            return;
        }
        wordList.push(storyForm.elements[x].value);
    }
    event.preventDefault();
    document.querySelector("span").innerText=`${wordList[1]} ${wordList[0]} is ${wordList[3]} to ${wordList[2]}'s ${wordList[4]}`;
}
let randStory= ()=>
{
    const length=wordList.length;
    let randList=[];
    for(let x=0;x<length;x++)
    {
        randList.push(randomWord(wordList));
    }
    wordList=randList;
    event.preventDefault();
    document.querySelector("span").innerText=`${randList[0]} ${randList[1]} is ${randList[2]} to ${randList[3]}'s ${randList[4]}`;
}
let lib=document.getElementById("lib-button");
lib.addEventListener("click",createStory);
let shuffle= document.getElementById("shuffle");
shuffle.addEventListener("click",randStory);