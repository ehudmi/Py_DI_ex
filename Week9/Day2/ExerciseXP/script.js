// 🌟 Exercise 1 : Comparison
// Instructions
// Create a function called compareToTen(num) that takes a number as an argument.
// The function should return a Promise:
// the promise resolves if the argument is less than 10
// the promise rejects if argument is greater than 10.
// Test:

// //In the example, the promise should reject
// compareToTen(15)
//   .then(result => console.log(result))
//   .catch(error => console.log(error))

// //In the example, the promise should resolve
// compareToTen(8)
//   .then(result => console.log(result))
//   .catch(error => console.log(error))
function compareToTen(arg){
    return new Promise((resolve, reject) => {
        if(arg<=10){
            resolve("Resolved");
        }
        else{
            reject("Error");
        }
    })
}

// compareToTen(8).then(result=> console.log(result)).catch(error=>console.log(error));
// 🌟 Exercise 2 : Promises
// Instructions
// Create a promise that resolves itself in 4 seconds and returns a “success” string.
// How can you make your promise from part 1 shorter using Promise.resolve() and console.log “success”?
// Add code to catch errors and console.log ‘Ooops something went wrong’.
// let sucProm= new Promise((resolve) => {
//     setTimeout(function(){resolve("success!")},4000);
// })
// sucProm.then(result=> console.log(result));
// setTimeout(function(){
//     try{Promise.resolve(console.log("success!"))}
//     catch(error){console.log("Ooops something went wrong")}},4000);



// 🌟 Exercise 3 : Resolve & Reject
// Instructions
// Use Promise.resolve(value) to create a promise that will resolve itself with a value of 3.
// Use Promise.reject(error) to create a promise that will reject itself with the string “Boo!”
Promise.resolve(3).then(result=>console.log(result));
Promise.reject("Boo!").catch(error=>console.log(error));