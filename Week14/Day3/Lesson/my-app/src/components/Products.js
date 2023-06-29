import {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';

const Products= (props)=>{
    const [products, setProducts]= useState();
    useEffect(()=>{
        allProducts();
    },[])

    const [search, setSearch]= useState();

    const [name, setName]= useState();
    const [price, setPrice]= useState()

    const searchProducts= async ()=>{
        try {
            const res= await fetch(`http://localhost:3030/api/search?name=${search}`);
            const data= await res.json();
            setSearch(data);
        } catch (error) {
            console.log(error);
        } 
    }

    const insertProduct= async (event)=>{
        try {
            event.preventDefault()
            const res= await fetch('http://localhost:3030/api/products', {
                method:"POST",
                headers:{
                    'content-type':'application/json'
                },
                body:JSON.stringify({name, price})
            })
            const data=await res.json();
            setProducts(data);
        } catch (error) {
            console.log(error)
        }
    }
    
    const allProducts=async ()=>{
        try {
            const res= await fetch('http://localhost:3030/api/products');
            const data= await res.json();
            setProducts(data);
        } catch (error) {
            console.log(error);
        }    
    }
    return(
        <div>
            <h1>Shop</h1>
            <div>
            <input onChange={(event)=>setSearch(event.target.value)} />
            <button onClick={()=>searchProducts()}>Search</button>
            </div>
            <div>
                <form onSubmit={insertProduct}>
                    Name: <input onChange={(e)=>setName(e.target.value)} id='name' />
                    Price: <input onChange={(e)=>setPrice(e.target.value)} id='price' />
                    <input type='submit' value={'Add'}></input>
                </form>

            </div>
            {
                products ? products.map(item=>{
                    return(
                        <div key={item.id} style={{
                            display:'inline-block',
                            padding:'20px',
                            margin: '20px',
                            border: '1px solid #ccc',
                        }}> 
                           <h4> {item.name} </h4>
                            {item.price}
                            <Link to={`/product/${item.id}`}>Shop Now</Link>
                        </div>
                    )
                }):null
            }
            
        </div>
    )
}

export default Products;