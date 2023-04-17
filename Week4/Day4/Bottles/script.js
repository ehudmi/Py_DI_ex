// Have you heard the infamous song “99 Bottles of Beer?”
// In this exercise you need to console.log the lyrics of our own 99 Bottles of Beer song.

// ==============================
// Example
// ==============================

// 99 bottles of beer on the wall
// 99 bottles of beer
// Take 1 down, pass it around
// 98 bottles of beer on the wall

// 98 bottles of beer on the wall
// 98 bottles of beer
// Take 2 down, pass them around
// 96 bottles of beer on the wall

// 96 bottles of beer on the wall
// 96 bottles of beer
// Take 3 down, pass them around
// 93 bottles of beer on the wall

// ect …

// ==============================



// Prompt the user for a number to begin counting down bottles.

// In the song, everytime a bottle drops,
// the subtracted number should go up by 1.
let bottlegame= (bottlenum) =>
{
    let subtracted=0;
    while(bottleNum>0)
    {
        subtracted++;
        if(subtracted==1)
        {
            console.log(`Take ${subtracted} down, pass it around`);
        }
        else if(subtracted>bottleNum)
        {
        console.log(`then, take ${bottleNum} down, pass them around`);
        }
        else
        {
            console.log(`then, take ${subtracted} down, pass them around`);
        }
        bottleNum=bottleNum-subtracted;
        if(bottleNum==1)
        {
        console.log(`${bottleNum} bottle of beer on the wall`);
        }
        else if(bottleNum<=0)
        {
        console.log(`no bottles of beer on the wall`);
        }
        else
        {
        console.log(`${bottleNum} bottles of beer on the wall`);
        }
    }
}

let bottleNum= prompt("How many bottles are there?");
bottleNum=Number(bottleNum);
if(bottleNum==NaN)
{
    alert("Not a number, try again!");
}
else
{
    bottlegame(bottleNum);
}