// let solution = (str) => {
// 	if (str.indexOf("b") == -1) {
// 		return true;
// 	} else {
// 		return str.lastIndexOf("a") < str.indexOf("b") ? true : false;
// 	}
// };
// my solution

// function solution(str) {
// 	let len = str.length;
// 	let foundA = -1;
// 	let foundB = -1;
// 	for (let i = 0; i < len; i++) {
// 		if (str[i] == "a") {
// 			foundA = i;
// 		} else if (str[i] == "b") {
// 			foundB = i;
// 		}
// 		if (foundB < foundA && foundB !== -1 && foundA !== -1) {
// 			return false;
// 		}
// 	}
// 	return true;
// }

//instuctor solution num 1

// function solution(str) {
// 	let foundB = false;
// 	let len = str.length;
// 	for (let i = 0; i < len; i++) {
// 		if (str[i] == "b") {
// 			foundB = true;
// 		} else if (foundB == true) {
// 			return false;
// 		}
// 	}
// 	return true;
// }

// //instructor solution num 2

// function testSolution() {
// 	const testCases = [
// 		{ input: "aabbb", output: true },
// 		{ input: "ba", output: false },
// 		{ input: "aaa", output: true },
// 		{ input: "b", output: true },
// 		{ input: "abba", output: false },
// 		{ input: "a", output: true },
// 		{ input: "bbaa", output: false },
// 		{ input: "bbba", output: false },
// 		{ input: "aabb", output: true },
// 		{ input: "bababab", output: false },
// 		{ input: "babababa", output: false },
// 		{ input: "aabababb", output: false },
// 		{ input: "baaab", output: false },
// 		{ input: "bbabbabbababbab", output: false },
// 		{ input: "babaabaaab", output: false },
// 		{ input: "ab", output: true },
// 	];
// 	for (let i = 0; i < testCases.length; i++) {
// 		const { input, output } = testCases[i];
// 		const result = solution(input);
// 		console.log(
// 			`Input: "${input}", Output: ${result}, Expected Output: ${output}`
// 		);
// 	}
// }

// testSolution();

const population = {
	tokyo: 37833000,
	delhi: 24987657,
	shanghai: 2290076,
	dateTime: {
		time: 1600,
		date: "09052023",
	},
};

let keys = Object.keys(population); // returns an array of the keys
let values = Object.values(population); // returns an array of the values
let arr = Object.entries(population); // returns an array of arrays, each array holding the key and the value assigned to it.

// arr.forEach(([a, b]) => {
// 	console.log(a, b);
// });
// const population2 = [
// 	["tokyo", 37833000],
// 	["delhi", 24987657],
// 	["shanghai", 2290076],
// ];
// const population3 = Object.fromEntries(population2);
// console.log(population3);
// const population2 = { ...population };

// const popDeep = {
// 	tokyo: 37833000,
// 	delhi: 24987657,
// 	shanghai: { people: 2290076 },
// };

// const popDeep2 = JSON.parse(JSON.stringify(popDeep));
//this is the way to clone an object within an object properly.
// const population2 = {
// 	tokyo: 1,
// 	telaviv: 77777,
// 	newyork: 55555,
// };

// let population3 = { ...population, ...population2 };
// console.log(population3);
// population3 = { ...population, tokyo: 0 };
// console.log(population3);
// const {
// 	shanghai,
// 	tokyo,
// 	delhi,
// 	dateTime: { time, date },
// } = population;
//destructuring in a objects work that it searches for the key and assigns the value. if the key is not in the object we compare to, it will return undefined as the value of the key.
// console.log(date, time);

// function x({tokyo, delhi}) {

// 	console.log(tokyo, delhi);
// }
// x(population);

const users = {
	user1: { age: 44, name: "picard" },
	user2: { age: 12, name: "sisko" },
	user3: { age: 109, name: "janeway" },
};
// filter for all users older than 30
// and store their data in an array
// use Array.filter Array.map
// let usersArr = Object.entries(users);
// console.log(usersArr);
// usersArr = usersArr
// 	.filter((item) => item[1].age > 30)
// 	.map((item, i, arr) => {
// 		item[1]["id"] = item[0];
// 		item.shift();
// 		return item[0];
// 	});
// console.log(usersArr);
// // my solution
// let userkeys = Object.keys(users);
// let filtered = userkeys.filter((key) => users[key].age > 30);
// let older = filtered.map((id) => ({ id, ...users[id] }));
// console.log(older);

class Person {
	constructor(name) {
		this.name = name;
	}
	getName() {
		return this.name;
	}

	setName(name) {
		this.name = name;
	}
	greet() {
		console.log(`Hello, my name is ${this.name}`);
	}
}

let personA = new Person("Sarah");
let personB = new Person("John");
// personA.greet();
// personB.setName("Martin");
// personB.greet();

class Animal {
	constructor(name) {
		this.name = name;
	}

	noisemaker() {
		console.log(`${this.name} make a noise`);
	}
}

class Dog extends Animal {
	constructor(name) {
		super(name);
	}
	noisemaker() {
		console.log(`${this.name} barks!`);
	}
}

const dog1 = new Dog("Buddy");
dog1.noisemaker();
const cat = new Animal("Mizi");
cat.noisemaker();
