// Exercise 1 : Animation With The Alphabet
// Instructions
// Create multiple squares/boxes with letters inside. There should be 26 squares/boxes for all the letters (A to Z) next to each other.
// Make all the squares draggable.
// You should be able to drag and drop the letters depending on their coordinates x and y.
let alph=["A", "B", "C", "D", "E", "F", "G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];

let makeDrag= str=>
{
    let letter=document.createElement("div");
    letter.className="Letter";
    letter.textContent=str;
    letter.draggable="true";
    document.body.appendChild(letter);
}

for(let x in alph)
{
    makeDrag(alph[x]);
}