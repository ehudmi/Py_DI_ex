// 1. create a module users.js
// 2. create a function that get the json user file
// https://jsonplaceholder.typicode.com/users
// 3. return the arr of users from the function
// 4. console log the arr of user in
// the file that you require it (not in the module)

const {getUsers}=require('./users.js');

getUsers('https://jsonplaceholder.typicode.com/users').then(result=>console.log(result));