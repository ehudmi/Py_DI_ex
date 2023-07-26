import './App.css';
import UserFavoriteColors from './components/UserFavoriteColors';
import Exercise4 from './components/Exercise4';

function App() {
  // const myelement= <h1>I Love JSX!</h1>;
  // const sum=5+5;
  const user = {
    firstName: 'Bob',
    lastName: 'Dylan',
    favAnimals : ['Horse','Turtle','Elephant','Monkey']
  };
  return (
    <div className="App">
     {/* <h1>I don't use JSX</h1>
     {/* <h1>Hello World!</h1> */}
     {/* {alert('Hello World')} */}
     {/* {myelement} */}
    {/* <>React is {sum} times better with JSX</> */}
    {/* <h3>{user.firstName}</h3>
    <h3>{user.lastName}</h3>
    <UserFavoriteColors animals={user.favAnimals}></UserFavoriteColors> */}
    <Exercise4></Exercise4>
    </div>
  );
}

export default App;
