// Create a HTML file for your calculator and a JS file for the calculator’s functionality.
// You must create 3 functions in the js file:
// number(num)
// operator(operator)
// equal()
// Hint : you can use the eval() method to help with your calculations.
// Before coding, take your time to understand all the parts to the exercise and their process. You can write it down somewhere if it helps (recommended).
// Bonus : create the RESET and CLEAR buttons.
let firstArg="";
// the argument that u put in first/the argument that will stay for the next operation
let tempArg="";
// the arugment that u do the operation with
let index=0;
// count of operations
let operationPick;
// to choose the operation if we call equal.
let number =(num) =>
{
    let string=String(num);
if(index==0)
    {   

        firstArg=firstArg+string;
        if(firstArg.match(/\./g)!==null && firstArg.match(/\./g).length==2)
        {
            firstArg=firstArg.substring(0,firstArg.length-1);
        }
        // can't have 2 decimals in a number;
        console.log(firstArg);
    }
    else{
        // can't have 2 decimals in a number;
        tempArg=tempArg+string;
        if(tempArg.match(/\./g)!==null && tempArg.match(/\./g).length==2)
        {
            tempArg=tempArg.substring(0,tempArg.length-1);
        }
        console.log(tempArg)
    }
}

let operator= (operation) =>
{
    index++;
    if(index>=2)
    {
        equal()
    }
    switch(operation)
    {
        case "+":operationPick=0
        console.log("+");
        break;
        case "-":operationPick=1;
        console.log("-");
        break;
        case "X":operationPick=2;
        console.log("X");
        break;
        case "/":operationPick=3;
        console.log("/");
        break;
    }
}

let equal= () =>
{
    switch(operationPick)
    {
        case undefined:return;
        case 0: firstArg=Number(firstArg)+Number(tempArg);
        break;
        case 1: firstArg=Number(firstArg)-Number(tempArg);
        break;
        case 2: firstArg=Number(firstArg)*Number(tempArg);
        break;
        case 3: firstArg=Number(firstArg)/Number(tempArg);
        break;
    }
    tempArg="";
    firstArg=String(firstArg);
    console.log(firstArg);
    index=0;
}
let clear= () =>
{
    console.clear;
}

let reset= () =>
{
    console.clear();
    firstArg="";
    tempArg="";
    index=0;
    operationPick= undefined;
}