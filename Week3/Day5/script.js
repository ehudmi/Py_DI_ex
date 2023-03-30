// let names= ["john", "sarah", 23, "Rudolf",34]
// 1. Write a JavaScript for loop that will go through the variable names.

// if the item is not a string, pass.
// if the item is a string, check if its first letter is in uppercase. If not, change it to uppercase and then display the name.
// 2. Write a JavaScript for loop that will go through the variable names

// if the item is not a string, go out of the loop.
// if the item is a string, display it.
// let names = ["john", "sarah", 23, "Rudolf", 34];
// let str = "a";
// for (let i of names) {
// 	if (typeof i== "string") {
// 		str = i.slice(0, 1);
// 		if (str !== str.toUpperCase()) {
// 			str = str.toUpperCase();
// 			str = str.concat(i.substring(1));
// 			console.log(str);
// 		}
// 	}
// }

// for (let i in names) {
// 	if (typeof names[i] !== "string") {
// 		break;
// 	} else {
// 		console.log(names[i]);
// 	}
// }

// let str = "";
// for (let i = 1; i <= 8; i++) {
// 	str = "";
// 	for (let j = 1; j <= i; j++) {
// 		str = str.concat(j, " ");
// 	}
// 	console.log(str);
// }

// let numb = 5;
// let power = 4;
// let out = 1;
// for (let i = 0; i < power; i++) {
// 	out = out * numb;
// }
// console.log(out);

const users = [
	{
		user_id: 1,
		name: "Leanne Graham",
		username: "Bret",
		contact: {
			email: "Sincere@april.biz",
			phone: "+972505556666",
		},
	},
	{
		user_id: 2,
		name: "Ervin Howell",
		username: "Antonette",
		contact: {
			email: "Shanna@melissa.tv",
			phone: "+972507776666",
		},
	},
	{
		user_id: 3,
		name: "Clementine Bauch",
		username: "Samantha",
		contact: {
			email: "Nathan@yesenia.net",
			phone: "+972501234567",
		},
	},
];
