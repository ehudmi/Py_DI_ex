import { useContext } from "react";
import { AppContext } from "../App";
import { CounterContext } from "./Counter";

function SubCounter(props){
    const {count, setcount}= useContext(AppContext);
    const {title}= useContext(CounterContext);
    return(
        <>
        <h2>{title}</h2>
        <h3>{count}</h3>
        <button onClick={()=>setcount(count+1)}>Add</button>
        </>
    )
}

export default SubCounter;