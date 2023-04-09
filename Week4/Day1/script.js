// const pwr = (numb) => {
// 	return numb * numb;
// };
// console.log(pwr(3));

// let a = 5;
// let b = 10;
// a > b ? (a = 8) : (b = 13);
// let countVowel = (string) => {
// 	let result = string.match(/[aeiou]/gi);
// 	return result.length;
// };
// console.log(countVowel("Hello!"));
// let myFamilyAge = (myAge) => {
// 	let momAge = myAge * 2;
// 	let dadAge = momAge * 1.2;
// 	console.log(
// 		"my Age is",
// 		myAge + ", My father's age is",
// 		dadAge + " and my mother's age is",
// 		momAge
// 	);
// };
// myFamilyAge(20);

let checkPal = (inputWord) => {
	inputWord = inputWord.toLowerCase();
	let bool = true;
	for (let i = 0; i < inputWord.length; i++) {
		if (inputWord[i] !== inputWord[inputWord.length - 1 - i]) {
			bool = false;
		}
	}
	return bool;
};
console.log(checkPal("racecar"));
