const getMyProducts = async () => {
	try {
		const res = await fetch("/api/products");
		const data = await res.json();
		render(data);
	} catch (error) {
		console.log(error);
	}
};
const render = (arr) => {
	const html = arr.map((item) => {
		return `<div>
        <h2>${item.name}</h2>
        <p>${item.price}</p>
        </div>`;
	});
	document.getElementById("root").innerHTML = html.join("");
};
getMyProducts();
