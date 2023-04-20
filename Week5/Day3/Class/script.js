let arr = [
	{ id: 1, user: "John", email: "john@gmail.com" },
	{ id: 2, user: "Sara", email: "sara@gmail.com" },
	{ id: 3, user: "Yasaar", email: "yasaar@gmail.com" },
	{ id: 10, user: "Yeshna", email: "yeshna@gmail.com" },
	{ id: 5, user: "Varshana", email: "varshana@gmail.com" },
];

const root = document.getElementById("root");
function createUsers() {
	root.innerHTML = "";
	for (let i = 0; i < arr.length; i++) {
		let div = document.createElement("div");
		div.classList.add("inner-div");
		let image = document.createElement("img");
		image.setAttribute("src", `https://robohash.org/${arr[i].id}`);
		div.appendChild(image);
		root.appendChild(div);
		let name = document.createElement("h2");
		name.innerText = `${arr[i].user}`;
		div.appendChild(name);
		let email = document.createElement("p");
		email.innerText = `${arr[i].email}`;
		div.appendChild(email);
	}
}
