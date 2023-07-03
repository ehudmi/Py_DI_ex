const Child=(props)=>{
    return(
        <>
        <h1>Child</h1>
        <input onChange={(e)=>props.setText(e.target.value)}/>
        </>
    )
}

export default Child;