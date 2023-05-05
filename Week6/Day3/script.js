let checkBasket = (key) =>
	basket.key !== undefined ? basket[key] : "not Exist";
const basket = {
	glasses: 1,
	books: 2,
	floss: 100,
};

//Arrays and Objects are Pass by Reference!!! they have a pointer to the same location in the memory!!!

arr = [1, 2, 3];
arr2 = arr;
arr[0] = 15;
//both arrays will change!!

// let obj = {
// 	name: "aaa",
// 	email: "bbb",
// };

// let obj2 = { ...obj };
// let obj3 = Object.assign({}, obj);
// obj2.email = "ccc";

// console.log(obj);
// console.log(obj2);
// console.log(obj3);

let user = {
	name: "Mark",
	address: {
		city: "Tel Aviv",
		country: "Israel",
		zipcode: {
			start: "567",
			end: "78945",
		},
	},
};
console.log(user);

let str = JSON.stringify(user);
console.log(str);
console.log(JSON.parse(str));
