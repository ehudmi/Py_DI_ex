import { useState, useEffect } from "react";

// class Counter extends Component {
// 	constructor(props) {
// 		super(props);
// 		// console.log(1);
// 		this.state = {
// 			count: 0,
// 			// title: data,
// 		};
// 	}
// 	// componentDidMount = () => {
// 	// 	console.log(3);
// 	// };
// 	add = () => {
// 		this.setState({ count: this.state.count + 1 }, () => {
// 			console.log(this.state.count);
// 		});
// 		console.log(this.state.count);
// 		// this will NOT give us the value presented in the app, because setState is ASYNC!! if we want the current state, we need to add the console
// 		// log in the callback function.
// 	};
// 	subtract = () => {
// 		this.setState({ count: this.state.count - 1 });
// 	};
// 	componentWillUnmount = () => {
// 		alert("Don`t do that");
// 	};
// 	render() {
// 		// console.log(2);
// 		return (
// 			<>
// 				<button onClick={this.add}>+</button>
// 				<h2>Counter Class</h2>
// 				<h2>{this.state.count}</h2>
// 				<h3>{this.props.data}</h3>
// 				<button onClick={this.subtract}>-</button>
// 			</>
// 		);
// 	}
// }

const Counter = (props) => {
	const [count, setCount] = useState(0);

	useEffect(() => {
		console.log(count);
	}, [count]);

	const add = () => {
		setCount(count + 1);
	};
	return (
		<>
			<h2>Counter</h2>
			<button onClick={add}>+</button>
			{count}
			<button
				onClick={() => {
					setCount(count - 1);
				}}
			>
				-
			</button>
		</>
	);
};

export default Counter;

// exercise about hooks in the last lesson folder.
