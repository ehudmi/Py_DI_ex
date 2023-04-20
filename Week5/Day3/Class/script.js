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
// let id;
// let i = 0;
// const box = document.getElementById("box");
// function start() {
// 	id = setInterval(function () {
// 		box.style.left = i + "px";
// 		i == 350 ? stop() : false;
// 		i++;
// 	}, 5);
// }

// function stop() {
// 	clearInterval(id);
// }
// let orangeSquare = document.getElementById("drop-container");
// let pinkSquareContainer = document.getElementsByClassName(
// 	"draggable-container"
// )[0];
// let pinkSquareDrag = document.getElementById("draggable-element");

// pinkSquareDrag.addEventListener("dragstart", function (event) {
// 	event.dataTransfer.setData("pink-square", event.target.id);
// 	event.dataTransfer.effectAllowed = "move";
// 	event.target.style.cursor = "move";
// });

// pinkSquareDrag.addEventListener("drag", function (event) {
// 	event.preventDefault();
// console.log(event.target);
// 	event.target.classList.add("hide");
// });

// orangeSquare.addEventListener("dragover", function (event) {
// 	event.preventDefault();
// });

// orangeSquare.addEventListener("drop", function (event) {
// 	event.preventDefault();
// 	let id = event.dataTransfer.getData("pink-square");
// 	let pink = document.getElementById(id);
// 	orangeSquare.appendChild(pink);
// });

// pinkSquareContainer.addEventListener("dragover", function (event) {
// 	event.preventDefault();
// });

// pinkSquareContainer.addEventListener("drop", function (event) {
// 	event.preventDefault();
// 	let id = event.dataTransfer.getData("pink-square");
// 	let pink = document.getElementById(id);
// 	pinkSquareContainer.appendChild(pink);
// });

let pangrams = (str) => {
	str = str.toLowerCase();
	let letters = "abcdefghijklmnopqrstuvwxyz";
	for (let x = 0; x < letters.length; x++) {
		if (!str.includes(letters[x])) {
			console.log("not a pangram");
			return;
		}
	}
	console.log("its a pangram!");
	return;
};
pangrams("The quick brown fox jumps over the lazy dog");
