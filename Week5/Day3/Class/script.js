// reverse a given string;

// let reverse = (string) => {
// 	let arr = string.split(" ");
// 	let reversed = "";
// 	for (let i = 0; i < arr.length; i++) {
// 		let word = arr[i].split("");
// 		let flippedWord = "";
// 		for (let x = 0; x < word.length; x++) {
// 			flippedWord = flippedWord + word[word.length - x - 1];
// 		}
// 		reversed = reversed + flippedWord + " ";
// 	}
// 	return reversed;
// };
// console.log(reverse("hi!"));
// console.log("before");
// setTimeout(function () {
// 	console.log("hi");
// }, 3000);
// console.log("after");
let id;
let i = 0;
const box = document.getElementById("box");
function start() {
	id = setInterval(function () {
		box.style.left = i + "px";
		i == 350 ? stop() : false;
		i++;
	}, 5);
}

function stop() {
	clearInterval(id);
}
