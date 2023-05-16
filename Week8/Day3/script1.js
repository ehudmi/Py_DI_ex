const page = new XMLHttpRequest();
let users;
page.open("GET", `https://jsonplaceholder.typicode.com/users`);

page.send();
page.responseType = "json";

page.onload = function () {
	users = this.response;
	for (let x = 0; x < users.length; x++) {
		let info = document.createElement("div");
		info.style.display = "inline-block";
		info.style.border = "1px solid #000";
		let img = document.createElement("img");
		img.src = `https://robohash.org/${x}?size=150x150`;
		info.append(img);
		let p = document.createElement("p");
		p.textContent = `Name= ${users[x].name} Email=${users[x].email} username= ${users[x].username}`;
		info.appendChild(p);
		document.body.append(info);
	}
};
