import { useReducer } from "react";

const initState= {
    result: 0
}

function reducer(state, action){

    switch(action.type) {
        case "ADD":
            return {...state, result:state.result + action.payload}
        case "MINUS":
            return {...state, result:state.result-action.payload}
        default:
            return {...state};
    }
}

function MathCalc(props){
    const [state,dispatch ]= useReducer(reducer, initState)
    return(
        <>
            <h2>Simple Calculator</h2>
            Result: ...
            <button onClick={()=>dispatch({type:"ADD", payload:5})}>Add 1</button>
            <button onClick={()=>dispatch({type: "MINUS", payload:10})}>Minus 1</button>
            <button>Divide by 2</button>
            <button>Multiply by 2</button>
        </>
    )
}

export default MathCalc;