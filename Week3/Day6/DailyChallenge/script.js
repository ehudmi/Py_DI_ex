// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.

for(let i=1;i<7;i++)
{
    let star="* "
    star=star.repeat(i);
    console.log(star);
}

for(let x=1;x<7;x++)
{
    let star=""
    for(let i=0;i<x;i++)
    {
        star=star+"* ";
    }
    console.log(star);
}