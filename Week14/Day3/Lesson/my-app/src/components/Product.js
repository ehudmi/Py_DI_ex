import { useState, useEffect } from "react";
import { useParams,Link } from "react-router-dom";

const Product= (props)=>{
    const [product, setProduct]= useState();
    const params=useParams();

    useEffect(()=>{
        getProductInfo()
    },[])

    const getProductInfo= async ()=>{
        try {
            const res= await fetch(`http://localhost:3030/api/products/${params.id}`);
            const data= await res.json();
            console.log(data);
            setProduct(data);
        } catch (error) {
            console.log(error);
        }
    }
    return(
        <div>
            <h1>Product</h1>
            {
                product? product.map(item=>{
                    return(
                        <div key={item.id}> 
                        <h2>{item.name}</h2>
                        <p>{item.price}</p>
                        </div>
                    )
                }):<h1>Not found</h1>
            }
        </div>
    )
}

export default Product;