let placementArray = [];
let grid = document.getElementById("game_grid");
let shipList = {
	destroyer: 2,
	submarine: 3,
	cruiser: 3,
	battleship: 4,
	carrier: 5,
};
let shipAlign;
let shotNum = 15;

let charPlacer = () => {
	let charArray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"];
	for (let i = 0; i < charArray.length; i++) {
		let charDiv = document.createElement("div");
		let numDiv = document.createElement("div");
		charDiv.innerText = `${charArray[i]}`;
		numDiv.innerText = `${i + 1}`;
		grid.appendChild(charDiv);
		grid.appendChild(numDiv);
		charDiv.style.gridArea = `1 / ${i + 2}`;
		numDiv.style.gridArea = `${i + 2}/ 1`;
		charDiv.className = "grid_letters";
		numDiv.className = "grid_letters";
	}
};

let gridMaker = () => {
	charPlacer();
	for (let y = 0; y < 10; y++) {
		for (let x = 0; x < 10; x++) {
			let item = document.createElement("div");
			item.className = "grid_square";
			grid.appendChild(item);
			item.style.gridArea = `${x + 2}/${y + 2}`;
			let placement = [x + 2, y + 2];
			placementArray.push([placement, 0]);
		}
	}
};

let gameStart = () => {
	gridMaker();
	let gameScreen = document.getElementById("game");
	gameScreen.style.display = "block";
	let startScreen = document.getElementById("game_start");
	startScreen.style.display = "none";
	shipPlacer();
	// shooter();
};
let shipCheckerY = (item, length) => {
	let tempArray = [];
	for (let i = 0; i < length; i++) {
		if (placementArray[item + i] == undefined) {
			return false;
		}
		tempArray.push(placementArray[item + i]);
		if (tempArray[i][1] == 1) {
			return false;
		}
	}
	let yIndex = tempArray[0][0][1];
	for (let x = 1; x < tempArray.length; x++) {
		if (tempArray[x][0][1] !== yIndex) {
			return false;
		}
	}
	shipAlign = 1;
	return true;
};

let shipCheckerX = (item, length) => {
	let tempArray = [];
	for (let i = 0; i < length; i++) {
		if (placementArray[item + i * 10] == undefined) {
			return false;
		}
		tempArray.push(placementArray[item + i * 10]);
		if (tempArray[i][1] == 1) {
			return false;
		}
	}
	let xIndex = tempArray[0][0][0];
	for (let x = 1; x < tempArray.length; x++) {
		if (tempArray[x][0][0] !== xIndex) {
			console.log(xIndex);
			console.log(tempArray);
			return false;
		}
	}
	shipAlign = 0;
	return true;
};

let shipAlignX = (item, length) => {
	for (let x = 0; x < length; x++) {
		placementArray[item + x * 10][1] = 1;
	}
};

let shipAlignY = (item, length) => {
	for (let y = 0; y < length; y++) {
		placementArray[item + y][1] = 1;
	}
};

let shipPlacer = () => {
	for (let x in shipList) {
		let done = 0;
		let shipLength = shipList[x];
		while (done == 0) {
			let itemIndex = Math.floor(Math.random() * placementArray.length);
			if (
				shipCheckerX(itemIndex, shipLength) == true ||
				shipCheckerY(itemIndex, shipLength) == true
			) {
				if (
					shipCheckerX(itemIndex, shipLength) == true &&
					shipCheckerY(itemIndex, shipLength) == true
				) {
					shipAlign = Math.round(Math.random());
				}
				if (shipAlign == 0) {
					shipAlignX(itemIndex, shipLength);
				} else {
					shipAlignY(itemIndex, shipLength);
				}
				done = 1;
			}
		}
	}
	console.log(placementArray);
};

let shooter = () => {
	// let squares = document.getElementsByClassName["grid_square"];
	let shotCount = 0;
	let userShot = prompt("select where to shoot");
	let columnShot = userShot.charAt(0).toLowerCase();
	let rowShot = Number(userShot.slice(1, userShot.length));
	columnShot > 106 || columnShot < 97
		? alert("you did not input column within range")
		: null;
	rowShot < 1 || rowShot > 10
		? alert("you did not input row within range")
		: null;
	console.log(columnShot, rowShot);
};

let gameEnd = () => {};

let start_button = document.getElementById("start");
start_button.addEventListener("click", gameStart);
let shoot_button = document.getElementById("shoot");
shoot_button.addEventListener("click", shooter);
