// const form = document.forms.myForm;
// const select = form.elements.fruit;
// // select.selectedIndex = 2;
// //one way to select before user interaction
// // select.options[3].selected = true;
// //another way
// // select.value = 1;
// //last way

// // const opt = document.createElement("option");
// // opt.value = 4;
// // opt.innerText = "Lemon";
// // select.appendChild(opt);
// //this is one way to add an option
// let opt = new Option("Grapes", 4);
// select.appendChild(opt);

// function handleSubmit(event) {
// 	event.preventDefault();
// 	// const email = document.getElementById("email");
// 	// const password = document.getElementById("password");
// 	// console.log(email.value, password.value);
// 	//this is one way
// 	const frm = document.forms.myForm;
// 	console.log(frm.elements.email.value, frm.elements.password.value);
// 	//this searches for the names of the elements, not their ID!
// 	let allselected = Array.from(select.options)
// 		.filter((option) => option.selected)
// 		.map((option) => option.value);
//this is for if you can select multiple values.
// }

function handleSubmit(event) {
	event.preventDefault();
	const form = event.target;
	if (form.username.value.trim() === "") {
		alert("Please enter a valid username");
		return;
	}
	form.submit();
}
