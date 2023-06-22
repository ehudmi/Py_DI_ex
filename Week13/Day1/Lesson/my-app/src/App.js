import User from "./components/User";
import { useState, useEffect } from "react";
import "./App.css";
// import users from "./users.json";
import "tachyons";

// add a state of users- useState
// add a button- onClick- fetch the users from teh API
// render the page with the users from the api

function App() {
	const [users, setUser] = useState([]);
	const [key, setKey] = useState("");
	const get_users = () => {
		fetch(`https://jsonplaceholder.typicode.com/users`, {
			method: "GET",
		})
			.then((res) => res.json())
			.then((data) => {
				setUser(data);
			});
	};
	useEffect(() => {
		if (key) {
			console.log(key);
		}
	}, [key]);
	return (
		<div className="App">
			<div>
				<h1>Users</h1>
				<input
					id="str"
					onChange={(e) => {
						setKey(e.target.value);
					}}
				></input>
			</div>
			<button onClick={get_users}>Click Me!</button>
			<div>
				{users.map((item, indx) => {
					return <User info={item} key={indx} />;
				})}
			</div>
		</div>
	);
}

export default App;

// import logo from "./logo.svg";
// import "./App.css";
// import Hello from "./Hello";
// import User from "./components/User";
// import users from "./users.json";
// // const users = [
// // 	{
// // 		name: "Mary",
// // 		email: "mary@gmail.com",
// // 	},
// // 	{
// // 		name: "John",
// // 		email: "john@gmail.com",
// // 	},
// // 	{
// // 		name: "David",
// // 		email: "david@gmail.com",
// // 	},
// // ];
// function App() {
// 	return (
// 		<div className="App">
// 			{
// 				/* <header className="App-header">
// 				<Hello />
// 				<img src={logo} className="App-logo" alt="logo" />
// 				<p>
// 					Edit <code>src/App.js</code> and save to reload.
// 				</p>
// 				<a
// 					className="App-link"
// 					href="https://reactjs.org"
// 					target="_blank"
// 					rel="noopener noreferrer"
// 				>
// 					Learn React
// 				</a>
// 			</header> */
// 				users.map((item, index) => {
// 					return (
// 						<User
// 							// name={item.name}
// 							// email={item.email}
// 							// username={item.username}
// 							info={item}
// 							key={index}
// 						/>
// 					);
// 				})
// 			}
// 		</div>
// 	);
// }

// export default App;
