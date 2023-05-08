// Exercise 1 : Calendar
// Instructions
// Create a function called createCalendar(year, month)
// The function should create a calendar for the given year/month.
// The calendar should be a table, where a week is <tr>, and a day is <td>. The table top should be <th> with weekday names: the first day should be Monday, and so on until Sunday.
// For instance, createCalendar(2012, 9) should generate the following calendar:

// Hint: There shouldn’t be any code in the HTML file. The table should be created from the JS file using the DOM.

let months= {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

let days= {
    1:"Mo",
    2:"Tu",
    3:"We",
    4:"Th",
    5:"Fr",
    6:"Sa",
    7:"Su"
}

let checkLeapYear= year=>{
    if(year%400==0)
    {
        months[2]=29;
    }
    else if(year%100==0)
    {
        months[2]=28;
    }
    else if(year%4==0)
    {
        months[2]=29
    }
    else
    {
        months[2]=28;
    }
}

function createCalendar(year,month) 
{
    createTable();
    checkLeapYear(year);
    let start=calcStart(year, month);
    console.log(start);
    let squares=document.getElementsByTagName("td");
    let count=1;
    for(let x=0;x<start;x++)
    {
        squares[x].textContent=".";
    }
    while(count<=months[month])
    {
        squares[count+start-1].textContent=count;
        count++;
    }
}

function createTable()
{
    let table=document.createElement("table");
    let dayHead=document.createElement("thead");
    for(let x=1;x<8;x++)
    {
        let day=document.createElement("th");
        day.textContent=days[x];
        dayHead.appendChild(day);
    }
    table.appendChild(dayHead);
    for(let x=0;x<5;x++)
    {
        let row=document.createElement("tr");
        for(let y=0;y<7;y++)
        {
            let square=document.createElement("td");
            row.appendChild(square);
        }
        table.appendChild(row);
    }
    document.body.appendChild(table);
}

function calcStart(year, month)
{
    let addDays=0;
    let fouhun= Math.floor(year/400);
    year=year-fouhun*400;
    if(Math.floor(year/300)!==0)
    {
        addDays++;
        year=year-300;
    }
    if(Math.floor(year/200)!==0)
    {
        addDays=addDays+3;
        year=year-200;
    }
    if(Math.floor(year/100)!==0)
    {
        addDays=addDays+5;
        year=year-100;
    }
    console.log(addDays)
    let leap=Math.floor((year-1)/4);
    addDays=addDays+2*leap;
    year=year-leap;
    addDays=addDays+year-1;
    addDays=addDays%7;
    console.log(addDays)
    let day=0;
    for(let x=1;x<month;x++)
    {
        day=day+months[x];
    }
    addDays=addDays+day%7;
    addDays=addDays%7;
    console.log(addDays);
    return addDays;
}

createCalendar(2012,9);