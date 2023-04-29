//needed to check if a ship can be placed in a certain spot
let placementArray = [];
let grid = document.getElementById("game_grid");
let shipList = {
	destroyer: 2,
	submarine: 3,
	cruiser: 3,
	battleship: 4,
	carrier: 5,
};
let shipNum = 5;
//variable to see if the ship will be horizontal or vertical
let shipAlign;
let shotNum = 15;
//variable to communicate between functions, stores the ship we are currently placing
let shipName;
//the grid where ships can be placed
let squares;
let log = document.getElementById("log");

//function to place the characters and numbers on the board
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
//function to make the game board
let gridMaker = () => {
	charPlacer();
	for (let y = 0; y < 10; y++) {
		for (let x = 0; x < 10; x++) {
			let item = document.createElement("div");
			item.classList.add("grid_square");
			grid.appendChild(item);
			item.style.gridArea = `${x + 2}/${y + 2}`;
			let placement = [x + 2, y + 2];
			placementArray.push([placement, 0]);
		}
	}
	squares = document.getElementsByClassName("grid_square");
};

let gameStart = () => {
	gridMaker();
	let gameScreen = document.getElementById("game");
	gameScreen.style.display = "block";
	let startScreen = document.getElementById("game_start");
	startScreen.style.display = "none";
	shipPlacer();
	shooter();
};
//function to see if we can place a ship verticaly
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

//function to see if we can place a ship horizontaly
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
			return false;
		}
	}
	shipAlign = 0;
	return true;
};

//places a ship horizontaly
let shipAlignX = (item, length) => {
	for (let x = 0; x < length; x++) {
		placementArray[item + x * 10][1] = 1;
		squares[item + x * 10].classList.add(`${shipName}`);
	}
};
//places a ship verticaly
let shipAlignY = (item, length) => {
	for (let y = 0; y < length; y++) {
		squares[item + y].classList.add(`${shipName}`);
		placementArray[item + y][1] = 1;
	}
};
//the main ship placing method
let shipPlacer = () => {
	for (let x in shipList) {
		let done = 0;
		shipName = x;
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
};
//this function gives the grid squares the shoot ability and writes the battle log
let shooter = () => {
	let squares = document.getElementsByClassName("grid_square");
	for (let i = 0; i < squares.length; i++) {
		squares[i].addEventListener("click", function (event) {
			let msg = document.createElement("div");
			if (squares[i].classList.contains("destroyed")) {
				msg.textContent = "You already Shot here!";
			} else if (squares[i].classList.length == 1) {
				shotNum = shotNum - 1;
				msg.textContent = `Missed!!! You have ${shotNum} shots left!`;
				squares[i].classList.add("destroyed");
				squares[i].textContent = "X";
			} else {
				squares[i].textContent = "X";
				for (let x in shipList) {
					if (squares[i].classList.contains(x)) {
						msg.textContent = "Hit!!!";
						squares[i].classList.add("destroyed");
					}
					if (
						document.getElementsByClassName(`${x} destroyed`).length ==
						shipList[x]
					) {
						msg.textContent = msg.textContent + `You destroyed a ${x}!`;
						let tempStyle = document.getElementsByClassName(x);
						delete shipList[x];
						for (let i = 0; i < tempStyle.length; i++) {
							tempStyle[i].style.backgroundColor = "black";
						}
						shipNum = shipNum - 1;
					}
				}
			}
			if (log.children.length >= 15) {
				log.firstElementChild.remove();
				log.firstElementChild.remove();
				log.firstElementChild.remove();
			}
			log.appendChild(msg);
			if (shotNum == 0 || shipNum == 0) {
				gameEnd();
			}
		});
	}
};
//game end function to see if the player won or lost
let gameEnd = () => {
	let msg = document.createElement("div");
	if (shipNum != 0) {
		msg.textContent = "Defeat!!";
	} else {
		msg.textContent = "Victory!!";
	}
	log.appendChild(msg);
	document.addEventListener("click", function (event) {
		event.preventDefault();
	});
};

let start_button = document.getElementById("start");
start_button.addEventListener("click", gameStart);
let endButt = document.getElementById("forfit");
endButt.addEventListener("click", gameEnd);
