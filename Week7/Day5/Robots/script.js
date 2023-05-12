const robots = [
	{
		id: 1,
		name: "Leanne Graham",
		username: "Bret",
		email: "Sincere@april.biz",
		image: "https://robohash.org/1?200x200",
	},
	{
		id: 2,
		name: "Ervin Howell",
		username: "Antonette",
		email: "Shanna@melissa.tv",
		image: "https://robohash.org/2?200x200",
	},
	{
		id: 3,
		name: "Clementine Bauch",
		username: "Samantha",
		email: "Nathan@yesenia.net",
		image: "https://robohash.org/3?200x200",
	},
	{
		id: 4,
		name: "Patricia Lebsack",
		username: "Karianne",
		email: "Julianne.OConner@kory.org",
		image: "https://robohash.org/4?200x200",
	},
	{
		id: 5,
		name: "Chelsey Dietrich",
		username: "Kamren",
		email: "Lucio_Hettinger@annie.ca",
		image: "https://robohash.org/5?200x200",
	},
	{
		id: 6,
		name: "Mrs. Dennis Schulist",
		username: "Leopoldo_Corkery",
		email: "Karley_Dach@jasper.info",
		image: "https://robohash.org/6?200x200",
	},
	{
		id: 7,
		name: "Kurtis Weissnat",
		username: "Elwyn.Skiles",
		email: "Telly.Hoeger@billy.biz",
		image: "https://robohash.org/7?200x200",
	},
	{
		id: 8,
		name: "Nicholas Runolfsdottir V",
		username: "Maxime_Nienow",
		email: "Sherwood@rosamond.me",
		image: "https://robohash.org/8?200x200",
	},
	{
		id: 9,
		name: "Glenna Reichert",
		username: "Delphine",
		email: "Chaim_McDermott@dana.io",
		image: "https://robohash.org/9?200x200",
	},
	{
		id: 10,
		name: "Clementina DuBuque",
		username: "Moriah.Stanton",
		email: "Rey.Padberg@karina.biz",
		image: "https://robohash.org/10?200x200",
	},
];
let grid = document.getElementById("robotGrid");
let search = document.getElementById("search");
for (let x = 0; x < robots.length; x++) {
	let robot = document.createElement("div");
	robot.className = `gridCard ${robots[x].username}`;
	let robotImg = document.createElement("img");
	robotImg.src = robots[x].image;
	robotImg.className = "roboImg";
	let imgDiv = document.createElement("div");
	imgDiv.className = "Imgdiv";
	imgDiv.appendChild(robotImg);
	let robotInfo = document.createElement("div");
	let robotName = document.createElement("h4");
	robotName.textContent = robots[x].name;
	robotInfo.appendChild(robotName);
	let robotEmail = document.createElement("h6");
	robotEmail.textContent = robots[x].email;
	robotInfo.appendChild(robotEmail);
	robotInfo.className = "roboInfo";
	robot.appendChild(imgDiv);
	robot.appendChild(document.createElement("br"));
	robot.appendChild(robotInfo);
	grid.appendChild(robot);
}

search.addEventListener("change", function (event) {
	let input = search.value.toLowerCase();
	console.log(input);
	let filtered = robots.filter((item) => {
		let name = item.name.toLowerCase();
		return name.includes(input);
	});
	filtered.forEach((item) => {
		let result = document.getElementsByClassName(item.username)[0];
		result.style.display = "block";
	});
	let notResults = robots.filter((item) => {
		let name = item.name.toLowerCase();
		return !name.includes(input);
	});
	notResults.forEach((item) => {
		let notResult = document.getElementsByClassName(item.username)[0];
		notResult.style.display = "none";
	});
});
