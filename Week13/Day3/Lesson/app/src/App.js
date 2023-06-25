import Counter from "./components/Counter.js";
import "./App.css";
import React, { Component } from "react";

// 1. convert this component to a class
// 2. add a title state
// 3. send this title to counter via props
// set the title of counter as the props title
// add a button on click you will change the title to something else

class App extends Component {
	constructor() {
		super();
		this.state = {
			title: "Hi",
			show: true,
		};
	}
	change = () => {
		this.setState({ title: "Hello", show: false });
	};

	render() {
		return (
			<div className="App">
				<header className="App-header">
					<button onClick={this.change}>Change</button>
					{this.state.show ? <Counter data={this.state.title} /> : null}
					{}
				</header>
			</div>
		);
	}
}

export default App;
