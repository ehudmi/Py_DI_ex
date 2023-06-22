import logo from "./logo.svg";
import "./App.css";
import Hello from "./Hello";
import User from "./components/User";
import users from "./users.json";
// const users = [
// 	{
// 		name: "Mary",
// 		email: "mary@gmail.com",
// 	},
// 	{
// 		name: "John",
// 		email: "john@gmail.com",
// 	},
// 	{
// 		name: "David",
// 		email: "david@gmail.com",
// 	},
// ];
function App() {
	return (
		<div className="App">
			{
				/* <header className="App-header">
				<Hello />
				<img src={logo} className="App-logo" alt="logo" />
				<p>
					Edit <code>src/App.js</code> and save to reload.
				</p>
				<a
					className="App-link"
					href="https://reactjs.org"
					target="_blank"
					rel="noopener noreferrer"
				>
					Learn React
				</a>
			</header> */
				users.map((item, index) => {
					return (
						<User
							// name={item.name}
							// email={item.email}
							// username={item.username}
							info={item}
							key={index}
						/>
					);
				})
			}
		</div>
	);
}

export default App;
