// Promises
// const getX = () => {
// 	setTimeout(() => {
// 		return 2;
// 	}, 1000);
// };

// const getY = () => {
// 	return 3;
// };

// const getXY = () => {
// 	let x = getX();
// 	let y = getY();
// 	return x + y;
// };

// console.log(getXY());
//here, we can see that because the timeout, x is undefined when we try to call getXY. this is the problem with a-sync code.
//one way to deal with it is adding a timer to getXY aswell, ie. waiting until x is defined and then executing the function.
//the seconed way is trying to use callbacks, which is inefficient since you need to chain all the callbacks.
//the third way is using promises.

//new Promise
//async/await function

//promises have 3 statuses- pending, fulfilled- resolved, fulfilled- rejected
// const p = new Promise((resolve, reject) => {
// 	reject("reject");
// });
// console.log(p);
//we need to deal with promises inside try and catch to catch the errors.

// const flip = () => {
// 	const coin = Math.floor(Math.random() * 3);
// 	return coin < 2 ? (coin == 0 ? "head" : "tail") : "side";
// };

// const flipCoin = new Promise((res, rej) => {
// 	const flipResult = flip();
// 	if (flipResult == "head" || flipResult == "tail") {
// 		let obj = {
// 			result: flipResult,
// 		};
// 		res(JSON.stringify(obj));
// 	} else {
// 		rej(JSON.stringify(obj));
// 	}
// });

// console.log("before");
// console.log(flipCoin);
// flipCoin
// 	.then((result) => JSON.parse(result))
// 	.then((result) => {
// 		console.log(result);
// 	})
// 	.catch((err) => {
// 		console.log("rejected=>", err);
// 	});
// console.log("after");

// const testNum = (num) => {
// 	let testProm = new Promise((resolve, reject) => {
// 		num < 10
// 			? resolve(`${num}, number is less then 10, success!`)
// 			: reject(`${num}, number is greater or equal to 10, error!`);
// 	});
// 	return testProm;
// };
// console.log(testNum(3));

// const getX = () => {
// setTimeout(() => {
// 	return 2;
// }, 2000);
// 	return new Promise((resolve, reject) => {
// 		setTimeout(() => {
// 			resolve(2);
// 		});
// 	});
// };

// const getY = () => {
// 	return 3;
// };

// const getXY = () => {
// 	let y = getY();
// 	getX().then((result) => {
// 		console.log(y + result);
// 	});
// };
// getXY();

let result = fetch("https://jsonplaceholder.typicode.com/users");
result
	.then((res) => {
		return res.json();
	})
	.then((data) => console.log(data))
	.catch((err) => {
		console.log(err);
	});
