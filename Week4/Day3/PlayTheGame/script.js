let playTheGame= ()=>
{
    let bool=confirm("Are you sure you want to play the game?");
    if(!bool)
    {
        alert("No problem, Goodbye");
        return
    }
    else
    {
        let userNum=-1;
        while(isNaN(userNum)||0>Number(userNum)||Number(userNum)>10)
        {
            userNum=prompt("Pick a number between 0 and 10");
            userNum=Number(userNum);
        }
        let computerNum= Math.round((Math.random() * 10));
        console.log(computerNum);
        compareNumbers(userNum,computerNum)
    }
}

let compareNumbers= (userNumber,computerNumber)=>
{
    for(let x=0;x<2;x++)
    {
        if(userNumber>computerNumber)
        {
            userNumber=prompt("Your number is bigger than the computer's, guess again");
            userNumber=Number(userNumber);
        }
        else if(userNumber<computerNumber)
        {
            userNumber=prompt("Your number is smaller than the computer's, guess again");
            userNumber=Number(userNumber);
        }
        else if(userNumber==computerNumber)
        {
            alert("WINNER");
            return
        }
    }
    alert("out of chances")
    return
}