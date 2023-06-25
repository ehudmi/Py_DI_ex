import "./Hello.css";
const users = [
	{
		name: "Mary",
		email: "mary@gmail.com",
	},
	{
		name: "John",
		email: "john@gmail.com",
	},
	{
		name: "David",
		email: "david@gmail.com",
	},
];

const styling = {
	color: "red",
	backgroundColor: "yellow",
};

// const Hello = () => {
// 	const html_users = users.map((item) => {
// 		return (
// 			<div>
// 				<h2>{item.name}</h2>
// 				<p className="textemail">{item.email}</p>
// 			</div>
// 		);
// 	});
// 	return (
// 		<div>
// 			<h1 style={styling}>Hello users:</h1>
// 			{html_users}
// 		</div>
// 	);
// };
// export default Hello;
