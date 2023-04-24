let button= document.getElementById("clear");
let grid=document.getElementsByClassName("coloringBrick");
let color= document.getElementsByClassName("color");
let currentColor= "white";
let toggler;
//how to check whether we are still holding the mouse button or not

//clearing
let clearFunction =() =>
{
    for(let x=0;x<grid.length;x++)
    {
        grid[x].style.backgroundColor = "white";
    }
    toggler=0;
}

//how to get the color we will dye with
for(let x=0;x<color.length;x++)
{
    color[x].addEventListener("click",function(event) {
        currentColor=color[x].style.backgroundColor;
    })
}



button.addEventListener("click",clearFunction);
for(let x=0;x<grid.length;x++)
{   grid[x].addEventListener("click",function(event)
{
    event.preventDefault();
})
    grid[x].addEventListener("mousedown", function(event) {
        grid[x].style.backgroundColor=currentColor;
        toggler=1;
    })
    grid[x].addEventListener("mouseup",function(event) {
        toggler=0;
    })
    grid[x].addEventListener("mouseover",function(event) {
        if(toggler==1)
        {
        grid[x].style.backgroundColor=currentColor;
        }
    })
}