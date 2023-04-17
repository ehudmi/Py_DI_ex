// Prompt the user for several words (separated by commas).
// Put the words into an array.
// Console.log the words one per line, in a rectangular frame as seen below.
// Check out the Hints and Requirements below.
// For example, if the user gives you:
// Hello, World, in, a, frame
// you will transform it to : ["Hello", "World", "in", "a", "frame"]
// that will get displayed as:

// stars and words


// Hint
// The number of stars that wraps the sentence, must depend on the length of the longest word.
let starBorder= () =>
{
    let input= prompt("Enter a sentence, each word seperated with a comma from the next one");
    let array=input.split(", ");
    let wordNum=array.length;
    let wordLength=0;
    let output=[""];
    for(let x in array)
    {
        array[x].length>wordLength?wordLength=array[x].length:false
        output=output.concat("* "+array[x]);
    }

    output=output.concat("");
    let outLength=output.length;
    while(output[0].length<wordLength+4)
    {
        output[0]=output[0]+"*";
        output[outLength-1]=output[outLength-1]+"*";
    }
    for(let i=1;i<outLength-1;i++)
    {
        while(output[i].length<wordLength+2)
        {
            output[i]=output[i]+" ";
        }
        output[i]=output[i]+" *";
    }
    for(let x in output)
    {
        console.log(output[x]);
    }
}
starBorder()