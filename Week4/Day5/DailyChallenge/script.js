// Create an array which value is the planets of the solar system.
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
// Each planet should have a different background color. (Hint: you could add a new class to each planet - each class containing a different background-color).
// Finally append each div to the <section> in the HTML (presented below).
// Bonus: Do the same process to create the moons.
// Be careful, each planet has a certain amount of moons. How should you display them?
// Should you still use an array for the planets ? Or an array of objects ?
let planets= [
    {
        name:"Mercury",
        moonNumber:0,
    },
    {
        name:"Venus",
        moonNumber:0,
    },
    {
        name:"Earth",
        moonNumber:1,
    },
    {
        name:"Mars",
        moonNumber:2,
    },
    {
        name:"Jupiter",
        moonNumber:95
    },
    {
        name:"Saturn",
        moonNumber:83
    },
    {
        name:"Uranus",
        moonNumber:27
    },
    {
        name:"Neptune",
        moonNumber:14
    }
]
let section= document.getElementsByClassName("listPlanets")[0];
let randomColor= () =>
{
    let rand= Math.round(Math.random()*255);
    return rand;
}
for(let x=0;x<planets.length;x++)
{
    let div=document.createElement("div");
    div.classList.add("planet");
    div.style.backgroundColor= `rgb(${randomColor()} ${randomColor()} ${randomColor()})`;
    div.innerText= planets[x].name;
    let moon= document.createElement("span");
    moon.classList.add("moon");
    moon.textContent= planets[x].moonNumber;
    div.appendChild(moon);
    section.appendChild(div);
}