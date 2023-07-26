const Parent= (props)=>{
    console.log(props);
    if(props.user=='admin'){
        return(
            <>
            <h1>Admin dashboard</h1>
            </>
        )
    }
    else{
        return props.children;
    }
}

export default Parent;