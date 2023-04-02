// Exercise 1 : Checking The BMI
// Instructions
// Hint:
// - You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.

// Create two objects, each object should hold a person’s details. Here are the details:
// FullName
// Mass
// Height
const personA= {
    FullName: "John",
    Mass: 80,
    Height: 170,
    BMI: function calcBMI1(){
        let a=80;
        let b=170/100;
        return a/(b*b);
    },
}

const personB= {
    FullName:"Sarah",
    Mass: 60,
    Height: 150,
    BMI: function calcBMI2(){
        let a=60;
        let b=150/100;
        return a/(b*b);
    }
}

function compareBMI(a,b)
{
    if(a.BMI()>b.BMI()){
        console.log(a.FullName);
    }
    else {
        console.log(b.FullName);
    }
}
compareBMI(personA, personB)

// Each object should also have a key which value is a function (ie. A method), that calculates the Body Mass Index (BMI) of each person

// Outside of the objects, create a JS function that compares the BMI of both objects.

// Display the name of the person who has the largest BMI.


// Exercise 2 : Grade Average
// Instructions
// Hint:
// - This Exercise is trickier then the others. You have to think about its structure before you start coding.
// - You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.

// In this exercise we will be creating a function which takes an array of grades as an argument and will console.log the average.
const grades= [85, 55, 100, 100, 30, 75, 60, 25, 80, 87, 92, 77, 93, 84, 68]
// Create a function called findAvg(gradesList) that takes an argument called gradesList.
function findAVG(gradesList)
{
    let sum=0;
    for(let x=0; x<gradesList.length;x++)
    {
        sum=sum+gradesList[x];
    }
    console.log(sum/gradesList.length)
    Pass(sum/gradesList.length)
}
function Pass(avg)
{
    if(avg>=65)
    {
        console.log("You passed the course!")
    }
    else{
        console.log("You failed! you must take the course again!")
    }
}

findAVG(grades)
// Your function must calculate and console.log the average.

// If the average is above 65 let the user know they passed

// If the average is below 65 let the user know they failed and must repeat the course.
// Bonus Try and split parts 1,2 and 3,4 of this exercise to two separate functions.
// Hint One function must call the other.