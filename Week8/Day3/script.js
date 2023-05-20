// function first(){
//     console.log("first");
// }
// function second(){
//     first();
//     console.log("second");
// }
// // second();
// //this is synchronized code, each component waits until the one before is complete.

// setTimeout(()=>{
//     first()
// },1000)
// second();
//this is a-synchronized code because it executes second while we wait for first to be executed.
//XML Http Request:
// let xhr = new XMLHttpRequest();
// //open(method, url, [async, user, password]) [these brackets mean optional]
// //example:
// xhr.open("GET", "https://jsonplaceholder.typicode.com/users");

// xhr.send();
// //this initiates the request.

// xhr.onload = function () {
// 	console.log(JSON.parse(xhr.response));
// };

// xhr.onerror = function () {
// 	console.log("something wrong");
// };

// xhr.onprogress = function (event) {
// 	console.log(event.loaded, event.total, event.lengthComputable);
// };
// const xhr = new XMLHttpRequest();
// xhr.withCredentials = true;
// const joke = document.getElementById("joke");
// const form = document.forms[0];
// const data = null;
// function categorySelect() {
// 	event.preventDefault();
// 	xhr.open(
// 		"GET",
// 		`https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random?category=${form.category.value}`
// 	);
// 	xhr.setRequestHeader("accept", "application/json");
// 	xhr.setRequestHeader(
// 		"X-RapidAPI-Key",
// 		"128d3d310amsh36037474704409ep1231c4jsnc5fe4f50719e"
// 	);
// 	xhr.setRequestHeader(
// 		"X-RapidAPI-Host",
// 		"matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
// 	);

// 	xhr.send(data);
// 	xhr.timeout = 10000;
// 	//this sets the time when the response closes, and we stop waiting for the api to respond.
// 	xhr.responseType = "json";
// 	//this sets the type of the response, if we set it to JSON we won't need to parse it afterwards. these are the types:
// 	//text- the default
// 	//json- switching the text to json
// 	//document- for xml files
// 	//arraybuffer- for binary data and for images, recordings, videos...
// 	//blob- for binary data and for images, recordings, videos...
// 	xhr.onload = function () {
// 		joke.innerText = xhr.response.value;
// 	};
// }

//part 2- XML
const xhr = new XMLHttpRequest();
// xhr.open("GET", "https://zivuch.github.io/emails.xml");
// xhr.send();
// xhr.responseType = "document";
// xhr.onload = function () {
// 	console.log(this.response);
// };

xhr.open("POST", "https://jsonplaceholder.typicode.com/posts");
xhr.setRequestHeader(`Content-type`, `application/json`);
let article = {
	title: "new article",
	body: "bla bla bla",
};

xhr.send(JSON.stringify(article));

xhr.onload = function () {
	console.log("response =>", this.response);
};
