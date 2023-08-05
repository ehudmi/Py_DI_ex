import { useContext, createContext, useState } from "react";
import { AppContext } from "../App";
import SubCounter from "./SubCounter";

export const CounterContext= createContext();

function Counter(props){
    const [title, setTitle]=useState('Hello User');
    const {count}= useContext(AppContext);
    return(
        <>
        <h3>{count}</h3>
        <CounterContext.Provider value={{title}}>  
        <SubCounter />
        </CounterContext.Provider>
        </>
    )
}

export default Counter;