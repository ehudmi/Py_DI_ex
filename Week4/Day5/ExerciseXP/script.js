// 🌟 Exercise 1 : Users
// Instructions
// <div id="container">Users:</div>
// <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
// </ul>
// <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
// </ul>


// Add the code above, to your HTML file

// Using Javascript:
// Retrieve the div and console.log it
// Change the name “Pete” to “Richard”.
// Delete the <li> that contains the text node “Sarah”. (It’s the second <li> of the second <ul>)
// Change each first name of the two <ul>'s to your name. (Hint : use a loop)

// Bonus - Using Javascript:
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.
// let contain=document.getElementById("container");
// console.log(contain)
// let list=document.getElementsByClassName("list");
// list[0].lastElementChild.textContent="Richard";
// list[1].children[1].remove();
// list[0].classList.add("university", "attendence");
// for(let x=0;x<2;x++)
// {
//     list[x].firstElementChild.textContent="Ehud";
//     list[x].classList.add("student_list");
//     console.log(list[x]);
// }



// 🌟 Exercise 2 : Users And Style
// Instructions
// <div>Users:</div>
// <ul>
//     <li>John</li>
//     <li>Pete</li>
// </ul>


// Add the code above, to your HTML file

// Using Javascript:
// Add a “light blue” background color and some padding to the <div>.
// Do not display the <li> that contains the text node “John”. (the first <li> of the <ul>)
// Add a border to the <li> that contains the text node “Pete”. (the second <li> of the <ul>)
// Change the font size of the whole body.

// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).
// let div= document.getElementsByTagName("div")[0];
// console.log(div);
// div.style.backgroundColor= "lightblue";
// div.style.padding= "10px";
// let list=document.getElementsByTagName("ul")[0];
// list.firstElementChild.remove();
// list.style.borderColor= "black";
// list.style.borderStyle= "double";
// document.body.style.fontSize= "24px";
// div.style.backgroundColor=="lightblue"? alert(`Hello ${list.firstElementChild.textContent} and ${list.lastElementChild.textContent}`):false;

// 🌟 Exercise 3 : Change The Navbar
// Instructions
// <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>


// Add the code above, to your HTML file

// Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (<li>).
// Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.

// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). Display the text of each link. (Hint: use the textContent property).
// let bar=document.getElementById("navBar");
// bar.setAttribute("id","socialNetworkNavigation");
// let ele=document.createElement("li");
// let text=document.createTextNode("Logout");
// let link=document.createElement("a");
// link.setAttribute("href", "#");
// link.append(text);
// ele.append(link);
// bar.firstElementChild.appendChild(ele);
// console.log(bar.firstElementChild.firstElementChild.textContent);
// console.log(bar.firstElementChild.lastElementChild.textContent);

// Exercise 4 : My Book List
// Instructions
// Take a look at this link for help.

// The point of this challenge is to display a list of two books on your browser.

// In the body of the HTML page, create an empty div:
// <div class="listBooks"></div>
// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).
let allBooks=[
    {
        title:"Lord Of The Rings",
        author:"JRR Tolkien",
        image:"https://m.media-amazon.com/images/I/51kfFS5-fnL._SX332_BO1,204,203,200_.jpg",
        alreadyRead: true
    },
    {
        title:"Lord Of The Flies",
        author:"William Golding",
        image:"https://www.pluggedin.com/wp-content/uploads/2020/01/lord-of-the-flies-cover-image.jpeg",
        alreadyRead: true
    }
]
// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)
// Requirements : All the instructions below need to be coded in the js file:
// Using the DOM, render the books inside an HTML table (the HTML table must be added to the <div> created in part 1).
// For each book :
// You have to display the book’s title and the book’s author.
// Example: HarryPotter written by JKRolling.
// The width of the image has to be set to 100px.
// If the book is already read. Set the color of the book’s details to red.
let bookTable=document.createElement("table");
let tableHead= document.createElement("tr");
bookTable.appendChild(tableHead);
for(let x=0;x<3;x++)
{
    let title=Object.keys(allBooks[0])[x];
    let ele=document.createElement("th");
    ele.textContent=title;
    tableHead.appendChild(ele);
}
for(let i=0;i<allBooks.length;i++)
{
    let infoRow=document.createElement("tr");
    let bookTitle=document.createElement("td");
    bookTitle.textContent=allBooks[i]["title"];
    infoRow.appendChild(bookTitle);
    let authorName=document.createElement("td");
    authorName.textContent=allBooks[i]["author"];
    infoRow.appendChild(authorName);
    let bookImg=document.createElement("td");
    let imgLink= document.createElement("img");
    imgLink.src= allBooks[i]["image"];
    imgLink.width= "100";
    bookImg.appendChild(imgLink);
    infoRow.appendChild(bookImg);
    allBooks[i]["alreadyRead"]==true?infoRow.style.color="red":false;
    bookTable.appendChild(infoRow);
}
document.getElementsByClassName("listBooks")[0].appendChild(bookTable);