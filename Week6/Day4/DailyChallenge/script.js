// Instructions
// Using this object :

let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        payed : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}
// Hint: To do this daily challenge, take a look at today’s lesson Pass By Value & Pass By Reference

// Create an arrow function named displayGroceries, that console.logs the 3 fruits from the groceries object. Use the forEach method.
let displayGroceries= ()=> {
    groceries.fruits.forEach(item =>console.log(item))
}
displayGroceries();
// Create another arrow function named cloneGroceries.
// In the function, create a variable named user that is a copy of the client variable. (Tip : make the user variable equal to the client variable)
let cloneGroceries= ()=>
{
    let user=client;
    user="Betty";
    //this wont change client because they are saved differently in the local storage.
    let shopping=groceries;
    groceries.totalPrice="35$";
    //we will see it because objects are pass by reference, shopping and groceries are saved in the same place
    groceries.other.payed=false;
    //the same again, objects are by refernce, therefore it will change groceries too.
}
cloneGroceries();
// Change the client variable to “Betty”. Will we also see this modification in the user variable ? Why ?
// In the function, create a variable named shopping that is equal to the groceries variable.
// Change the value of the totalPrice key to 35$. Will we also see this modification in the shopping object ? Why ?
// Change the value of the payed key to false. Will we also see this modification in the shopping object ? Why ?

// Invoke the cloneGroceries function.