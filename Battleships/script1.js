// const grid = {
// 	A: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
// 	B: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
// 	C: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
// 	D: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
// 	E: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
// 	F: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
// 	G: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
// 	H: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
// 	I: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
// 	J: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
// };

let grid = [];

const ships = [
	{ type: "destroyer", size: 2 },
	{ type: "submarine", size: 3 },
	{ type: "cruiser", size: 3 },
	{ type: "battleship", size: 4 },
	{ type: "carrier", size: 5 },
];

const populate = () => {
	let rowsArray = [];
	let columnArray = [];
	const batTab = document.createElement("table");
	document.body.appendChild(batTab);
	let tabHeader = document.createElement("tr");
	let blankHead = document.createElement("td");
	tabHeader.appendChild(blankHead);
	batTab.appendChild(tabHeader);
	for (let i = 0; i < 10; i++) {
		rowsArray.push(`row${i + 1}`);
		let tabHead = document.createElement("th");
		tabHead.innerText = String.fromCharCode("A".charCodeAt(0) + i);
		tabHeader.appendChild(tabHead);
		let tabRow = document.createElement("tr");
		batTab.appendChild(tabRow);
		let rowHead = document.createElement("th");
		rowHead.innerText = `${i + 1}`;
		tabRow.appendChild(rowHead);
		columnArray.push(0);
		grid.push({ rowName: rowsArray[i], rowContent: [columnArray] });
		for (let j = 0; j < 10; j++) {
			let gridSquare = document.createElement("td");
			gridSquare.innerText = 0;
			gridSquare.className = `column${String.fromCharCode(
				"A".charCodeAt(0) + j
			)} row${rowHead.innerText}`;
			tabRow.appendChild(gridSquare);
		}
	}
};

const placeShips = () => {
	for (i in ships) {
		let positionX;
		let positionY;
		let positionType = Math.floor(Math.random() * 2);
		let positionName = "";
		switch (positionType) {
			case 0:
				positionName = "horizontal";
				positionX = Math.floor(Math.random() * 11);
				positionY = Math.floor(Math.random() * ships[i].size);
				console.log(positionX, positionY, positionType);
				let positionTest = grid[positionY].rowContent[0].slice(
					positionY,
					ships[i].size
				);
				console.log(i, positionName, positionTest);

				// console.log(grid[positionX]);
				// console.log(positionX);
				break;
			case 1:
				positionName = "vertical";
				positionY = Math.floor(Math.random() * 11);
				positionX = Math.floor(Math.random() * ships[i].size);
				console.log(positionX, positionY, positionType);
				// console.log(grid[i]);
				// console.log(positionY);
				break;
		}
		// positionX + ships[i].size > 10 ? (positionType = 1) : null;
		// console.log(i);
		// console.log(positionX, positionY, positionType);
		// console.log(ships[i].size);
	}
};

populate();
console.log(grid);
placeShips();
// console.log(grid);
