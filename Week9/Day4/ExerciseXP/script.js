// 🌟 Exercise 1: Conversion
// Instructions
// Convert the below promise into async await:

// fetch("https://www.swapi.tech/api/starships/9/")
//     .then(response => response.json())
//     .then(objectStarWars => console.log(objectStarWars.result));

const exe= async ()=>{
    try {
        const response=await fetch("https://www.swapi.tech/api/starships/9/");
        if(response.status=="400"){
            throw new Error("Something went wrong");
        }
        else{
        const data= await response.json();
        console.log(data.result.properties);
        }
    } 
    catch (error) {
        console.log("Caught", error);
    }
}
// exe();


// function resolveAfter2Seconds() {
//     return new Promise(resolve => {
//         setTimeout(() => {
//             resolve('resolved');
//         }, 2000);
//     });
// }

// async function asyncCall() {
//     console.log('calling');
//     let result = await resolveAfter2Seconds();
//     console.log(result);
// }

// asyncCall();
//it will log calling, then wait for the 2 seconds to pass, then log resolved.