function handleClick() {
	let inputDiv = document.getElementsByClassName("input")[0];
	fetch("https://zivuch.github.io/yogaapi.json")
		.then((res) => {
			return res.json();
		})
		.then((data) => {
			data.forEach((item) => {
				let mufa = document.createElement("div");
				let name = document.createElement("div");
				let img = document.createElement("img");
				name.textContent = item.sanskrit_name;
				img.src = item.img_url;
				mufa.appendChild(name);
				mufa.appendChild(img);
				inputDiv.appendChild(mufa);
			});
		})
		.catch((err) => {
			console.log(err);
		});
}
