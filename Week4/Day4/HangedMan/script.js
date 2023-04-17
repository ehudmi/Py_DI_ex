// Prompt player 1 for a word. The word must have a minimum of 8 letters. Present the word in the console with stars (********).
// At this point continuously prompt player 2 for a letter.
// If the letter is in the word chosen by player 1, display the word in stars again but with the correct letter (*****t**).
// If the letter appears in the word multiple times, make sure it is seen in all the correct places when showing the stars with the correct guesses (***t**t*).
// If player 2 guesses incorrectly 10 times display a message in the console saying YOU LOSE.
// Show a list of all the guesses after each turn. In your code prevent player 2 from guessing the same letter twice.
// If player 1 wins, display a message that says CONGRATS YOU WIN.
let word="";
let index=0;
let tempWord="";
let guessList=[];
let player2= () =>
{

    let searchLetter=prompt("enter a letter to search for!");
    searchLetter=searchLetter.toLowerCase();
    if(guessList.includes(searchLetter))
    {
        alert("You already guessed that one!");
        return
    }
    guessList.push(searchLetter);
    let indices=[];
    for(let i=0;i<word.length;i++)
    {
        if(word[i]==searchLetter)
        {
            indices.push(i);
        }
    }
    let textlist=tempWord.split("");
    tempWord="";
    for(let x=0;x<textlist.length;x++)
    {
        if(indices.includes(x))
        {
            textlist[x]=searchLetter;
        }
        tempWord=tempWord+textlist[x];
    }
    console.log(guessList);
    console.log(tempWord);
    index++;
}

while(word.length<8)
{
    word= prompt("player 1, enter a word with a minimum of 8 characters");
    word=word.toLowerCase();
    tempWord=word;
    tempWord= tempWord.replace(/\S/g,"*");
}
console.log(tempWord);
while(index<10)
{
    alert("guess a letter!");
    player2();
    if(tempWord==word)
    {
        alert("Player 2 wins!!");
        break;
    }
}
if(tempWord!==word)
{
    alert("Player 1 wins!!");
}