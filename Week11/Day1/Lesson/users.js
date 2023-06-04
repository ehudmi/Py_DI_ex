async function getUsers(url){
    try {
        const data=await fetch(url).then(response=> response.json());
        return data;
    } catch (error) {
        console.log(error);
    }
    
}

module.exports= {
    getUsers
}