// function yearCheck(input) {
// 	input >= 2000
// 		? console.log("You are in the 21st century")
// 		: console.log("You live in the Middle Age");
// }
// let operator = "/";

// const calc = (a, b) => {
// 	return operator === "+"
// 		? a + b
// 		: operator === "-"
// 		? a - b
// 		: operator === "*"
// 		? a * b
// 		: operator === "/"
// 		? a / b
// 		: null;
// };

// console.log(calc(3, 4));

// const numbers = [10, 11, 12, 15, 20];

// numbers.forEach((item) => (item % 2 == 0 ? console.log(item) : null));

const arr = [2, 5, 7, 7, 9];
// first way
// arr.forEach((item, index) => {
// 	if (item % 2 == 0) {
// 		return true;
// 	}
// 	if (index == arr.length - 1) {
// 		return false;
// 	}
// });

//second way
// console.log(arr.some((item) => item % 2 == 0));

// console.log(arr.every((item) => item % 2 == 0));

// const includes = (para) => {
// 	for (x in arr) {
// 		if (para == x) return true;
// 	}
// 	return false;
// };
// console.log(includes(2));

// console.log(arr.includes(2));

// let creditHide = (number) => {
// 	let str = String(number);
// 	str = str.split("");
// 	str.forEach((num, index, arr) => {
// 		index < arr.length - 4 ? (arr[index] = "*") : null;
// 	});
// 	return str.join("");
// };
// console.log(creditHide(4672180265710943));

// let str = "5";
// let ret = str.padStart(2, "*");
// console.log(ret);

let str = "       Hello       ";
str.trimStart();
