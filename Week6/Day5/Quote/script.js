const quotes = [
	{
		id: 0,
		author: "Nelson Mandela",
		quote:
			"The greatest glory in living lies not in never falling, but in rising every time we fall. ",
		likes: 0,
	},
	{
		id: 1,
		author: "Aristotle",
		quote:
			"It is during our darkest moments that we must focus to see the light. ",
		likes: 0,
	},
	{
		id: 2,
		author: "Nietzsche",
		quote: "Stare into the abyss, and the abyss stares back at you.",
		likes: 0,
	},
	{
		id: 3,
		author: "Shaun Hick",
		quote:
			"You need to spend time crawling alone through shadows to truly appreciate what it is to stand in the sun.",
		likes: 0,
	},
];

let butt = document.getElementById("quoteGen");
let quoteSpace = document.getElementById("quoteSpace");
let ranIndex;
let checkIndex;
let smallButts = document.getElementsByClassName("smallButtons");
let answer = document.getElementById("answer");
let quotesSearch = document.getElementById("authorQuotes");
let quote;
//needed to communicate between functions
let icon;
//needed to communicate between functions
let auth;
//needed to communicate between functions

let randIndex = () => {
	ran = Math.round(Math.random() * (quotes.length - 1));
	while (ran == check) {
		ran = Math.round(Math.random() * (quotes.length - 1));
	}
	check = ran;
};

let createQuote = () => {
	quoteSpace.replaceChildren("");
	quote = document.createElement("p");
	icon = document.createElement("i");
	icon.className = "fa-solid fa-quote-left";
	auth = document.createElement("div");
	auth.id = "author";
	quote.appendChild(icon);
};

let showQuote = () => {
	randIndex();
	createQuote();
	quote.append(quotes[ran].quote);
	auth.textContent = quotes[ran].author;
	quoteSpace.appendChild(quote);
	quoteSpace.appendChild(auth);
	for (let x = 0; x < smallButts.length; x++) {
		smallButts[x].style.visibility = "visible";
	}
};

butt.addEventListener("click", showQuote);
let sub = document.getElementById("add");
sub.addEventListener("click", function (event) {
	event.preventDefault();
	quotes.push({
		id: index,
		author: document.getElementById("newAuthor").value,
		quote: document.getElementById("newQuote").value,
		likes: 0,
	});

	document.getElementById("newAuthor").value = "";
	document.getElementById("newQuote").value = "";
	index = index + 1;
});

let bar = document.getElementById("buttonBar");
bar.children[0].addEventListener("click", function (event) {
	answer.textContent = `The amount of characters is ${quotes[ran].quote.length}`;
});

bar.children[1].addEventListener("click", function (event) {
	answer.textContent = `The amount of non-whitespace characters is ${
		quotes[ran].quote.replace(/\s/g, "").length
	}`;
});

bar.children[2].addEventListener("click", function (event) {
	answer.textContent = `The amount of words is ${
		quotes[ran].quote.split(" ").length
	}`;
});

bar.children[3].addEventListener("click", function (event) {
	quotes[ran].likes++;
	answer.textContent = `Liked! This quote has ${quotes[ran].likes} likes!`;
});

let searchButt = document.getElementById("searchButt");
// all quotes by the same author
// searchButt.addEventListener("click", function (event) {
// 	event.preventDefault();
// 	let authorName = document.getElementById("searchBar").value;
// 	quotes.forEach((item) => {
// 		if (item.author == authorName) {
// 			let text = document.createElement("span");
// 			text.textContent = item.quote;
// 			quotesSearch.append(text);
// 			quotesSearch.append(document.createElement("br"));
// 		}
// 	});
// 	document.getElementById("searchBar").value = "";
// });

searchButt.addEventListener("click", function (event) {
	event.preventDefault();
	let target;
	quotes.forEach((item, index) =>
		item.author == document.getElementById("searchBar").value
			? (target = index)
			: false
	);
	if (target == undefined) {
		return;
	}
	createQuote();
	quote.append(quotes[target].quote);
	auth.textContent = quotes[target].author;
	ran = target;
	quoteSpace.appendChild(quote);
	quoteSpace.appendChild(auth);
});

let prevButt = document.getElementById("pre");
prevButt.addEventListener("click", function (event) {
	if ((ran = 0)) {
		return;
	} else {
		createQuote();
		quote.append(quotes[ran - 1].quote);
		auth.textContent = quotes[ran - 1].author;
		quoteSpace.appendChild(quote);
		quoteSpace.appendChild(auth);
		ran--;
		console.log(ran);
	}
});
let nextButt = document.getElementById("next");
nextButt.addEventListener("click", function (event) {
	if (ran >= quotes.length - 1) {
		return;
	} else {
		createQuote();
		quote.append(quotes[ran + 1].quote);
		auth.textContent = quotes[ran + 1].author;
		quoteSpace.appendChild(quote);
		quoteSpace.appendChild(auth);
		ran++;
		console.log(ran);
	}
});
