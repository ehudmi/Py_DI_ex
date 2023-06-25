import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(document.getElementById("root"));
// const name = "John";
// const arr = [
// 	{ name: "aaa", email: "aaa@gmail.com" },
// 	{ name: "aaa", email: "aaa@gmail.com" },
// 	{ name: "aaa", email: "aaa@gmail.com" },
// 	{ name: "aaa", email: "aaa@gmail.com" },
// ];
// const element = (
// 	<div>
// 		<h1>Hi JSX</h1>
// 		<h2>Nice!</h2>
// 		{arr.map((item, index) => {
// 			return (
// 				<>
// 					{item.name} {item.email}
// 				</>
// 			);
// 		})}
// 	</div>
// we need to always close all JSX tags. if we say use <br>, then we need to write >br/>.
// we can also use a react fragment instead of a div, it's syntax is: <>Hi!</>
// );
// root.render(element);
root.render(
	<React.StrictMode>
		<App />
	</React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
