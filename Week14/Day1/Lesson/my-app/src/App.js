import {useState} from 'react';
import './App.css';
import Counter from './components/Counter';
import ErrorBoundry from './components/ErrorBoundry';

function App(props) {
  return (
    <div className="App">
      <header className="App-header">
        <ErrorBoundry>
        <Counter />
        </ErrorBoundry>
        <Counter />
      </header>
    </div>
  );
}

export default App;
