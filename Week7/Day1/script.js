// let users = ["eli", "adam", "galina", "ziv"];

// let emails = users.map((item) => `${item}@gmail.com`);
// console.log(emails);

// let arr = [1, 2, 3, 4];

// let newArr = arr.map((item) => [item * 2]);
// console.log(newArr);

// let arr3 = newArr.flatMap((item) => item / 2);
// console.log(arr);

// let greatThree = (arr) => {
// 	let newArr = [];
// 	arr.forEach((item) => (item > 3 ? newArr.push(item) : false));
// 	return newArr;
// };
// console.log(greatThree([1, 3, 7, 2, 8]));

// let arr = [0, 1, 1, 2, 4, 5, 8];
// let newArr = arr.filter((item) => item > 3);
// console.log(newArr);

// const dragons = ["Tim", "Jonathan", "Sandy", "Sarah"];

// let SaNames = dragons.filter((item) => item.toLowerCase().startsWith("sa"));
// console.log(SaNames);

// let sum = (arr) => {
// 	let num = 0;
// 	arr.forEach((item) => (num = item + num));
// 	return num;
// };
// console.log(sum([0, -1, 5, 100, -200, 50]));

// let numbers = [0, -1, 5, 100, -200, 50];

// const total = numbers.reduce((total, item) => {
// 	total + item;
// }, 100);

// console.log(total);

// My way
// let digitSum = (num) => {
// 	while (num >= 10) {
// 		num = String(num).split("");
// 		num = num.reduce((total, item) => Number(total) + Number(item));
// 	}
// 	return num;
// };

//Better way
// let digitSum = (num) => {
// 	let arr = String(num).split("");
// 	let newNumber = arr.reduce((total, item) => Number(item) + Number(total));
// 	return newNumber < 10 ? newNumber : digitSum(newNumber);
// };

// console.log(digitSum(128));

// Birthday Cake Candles
// This array are Birthday Cake Candles
// You can blow only the tallest candles
// let arr = [2,4,8,4,8,1,8]
// birthdayCakeCandles function will return
// how many candles you can blow

/*
 * findIntersection function return an array that
 * contain the numbers exist in both strings from the array.
 * ["1,2,5,6,7", "2,5,7,8,15"] => [2,5,7]
 */

// let Arr = ["1,2,5,6,7", "2,5,7,8,15"];
// function findIntersection(arr) {
// 	let arr1 = arr[0].split(",");
// 	let arr2 = arr[1].split(",");
// 	let ret = arr1.filter((value) => arr2.includes(value));
// 	return ret;
// }
// console.log(findIntersection(Arr));

// let arr=[2,5];

// // const a=arr[0];
// // const b=arr[1];

// const [a, b]= arr;
//this is destructuring, it assigns the values in the array in the order we wrote.

let [c, d] = [1, 2];
let arr = [3, 4];
let arr1 = [a, b, ...arr];
//this will output [1,2,3,4];
//three dots at the end is a spread operator
// spread helps with copying a long array.
//three dots at the beginning is a rest operator
let [q, w, e, ...rest] = [1, 2, 3, 4, 5, 6, 7, 8, 9];
//q is 1, w is 2, e is 3, rest is an array that contains the rest of the array.
// we can't put something after the rest operator!!

//we can use destructuring like this:
let [username, email] = [`John`, `jjj@gmail.com`];
