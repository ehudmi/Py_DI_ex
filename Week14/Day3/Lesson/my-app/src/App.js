import Products from './components/Products.js';
import Home from './components/Home.js';
import './App.css';
import {Routes, Route, Link} from 'react-router-dom';
import Product from './components/Product.js';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <nav>
          <Link to='/'>Home</Link>
          <Link to='/shop'>Shop</Link>
          <Link to='/product/'></Link>
        </nav>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/zivuch' element={ <Home />} />
          <Route path='/shop' element={<Products />} />
          <Route path='/product/:id' element={<Product />} />
        </Routes>
      </header>
    </div>
  );
}

export default App;
