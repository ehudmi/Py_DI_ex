const UserFavoriteColors= (props)=>{
    console.log(props);
    const animals=props.animals;
    return(
    animals.map((item, index)=>{
        return <li id={index}>{item}</li>
    }))
}

export default UserFavoriteColors;