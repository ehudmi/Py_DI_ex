import {createContext, useState, useRef} from 'react';
import './App.css';
import Counter from './components/Counter';
import MathCalc from './components/MathCalculator';

export const AppContext = createContext()

function App(props) {
  const [count, setcount]= useState(0);
  const name_input= useRef()
  function handleClick(){
    console.log(name_input.current.value)
  }
  return (
    <div className='App'>
      <header className='App-header'>
    <MathCalc />
      </header>
    {/*<AppContext.Provider value={{count, setcount}}>
    <div className="App">
      <header className="App-header">
        <Counter />
        <input ref={name_input} />
        <button onClick={handleClick}>Click</button>
      </header>
    </div>
  </AppContext.Provider>*/}
  </div>
  );
}

export default App;
