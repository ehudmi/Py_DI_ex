// 1st Challenge
// Instructions
// Use Promise.all
// This function should accept an array of promises and return an array of resolved values.
// If any of the promises are rejected, the function should catch them.

// Explain in a comment how Promise.all work and why you receive this output.

// Example

// const promise1 = Promise.resolve(3);
// const promise2 = 42;
// const promise3 = new Promise((resolve, reject) => {
//   setTimeout(resolve, 3000, 'foo');
// });
// // expected output: Array [3, 42, "foo"]
// let allprom= async (promArr)=>
// {

//    return await Promise.all(promArr).then(result=>arr=result);

// }

// allprom([Promise.resolve(3), 42, new Promise((resolve, reject) => {
//     setTimeout(resolve, 3000, 'foo')
// })]).then(result=>console.log(result)).catch(err=>console.log("Something went wrong"));
//promise.all returns the list of resolved values if all promises inputed were resolved, and if one of them rejects then it catches it.

// 2nd Challenge
// Instructions
// You will find the hour of sunrise of two cities, using the API https://sunrise-sunset.org/api.

// In the HTML file, create a form with 4 inputs:
// the latitude and longitude of the first city
// the latitude and longitude of the second city

// Retrieve the input’s value and display the hour of the sunrise for both city ONLY when both promises are resolved
// Hint : Use Promise.all()

// Try with Paris and New York

// Paris
// Latitude: 48.864716
// Longitude: 2.349014

// New York
// Latitude: 40.730610
// Longitude: -73.935242

async function prm() 
{
    let frm= document.forms[0];
    const [firstCity, secondCity]= await Promise.all([
        fetch(`https://api.sunrise-sunset.org/json?lat=${frm.firstLat.value}&lng=${frm.firstLng.value}`).then(response=>response.json()),
        fetch(`https://api.sunrise-sunset.org/json?lat=${frm.secondLat.value}&lng=${frm.secondLng.value}`).then(response=>response.json())]);
        if(!firstCity.status=="OK" || !secondCity.status=="OK"){
            throw new Error("Something went wrong!");
        }
        return [firstCity, secondCity];
}

const showSun= (event)=>
{
    event.preventDefault();
    try {
        prm().then(arr=>{
            arr.forEach((city, index)=>{
                let info=document.createElement("p");
                info.textContent= `The sunrise in city number ${index+1} is at ${city.results.sunrise}`
                document.getElementsByClassName("info")[0].appendChild(info);
            })

        }).catch(err=>console.log(err))
    } catch (error) {
        console.log(error);
    }

}