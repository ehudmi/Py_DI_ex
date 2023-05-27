// Create a function that takes a date object and return string in the following format: YYYYMMDDHHmmSS.

// The format should contain a 4 digit year, 2 digit month, 2 digit day, 2 digit hour(00-23), 2 digit minute and 2 digit second.
// If any of the value has only single digit, you must use zero prefix, so that the result string length is always the same.

// Examples

// formatDate(new Date(2020, 6, 4, 8, 0, 0)) ➞ "20200704080000"

// formatDate(new Date(2019, 11, 31, 23, 59, 59)) ➞ "20191231235959"

// formatDate(new Date(2020, 6, 4)) ➞ "20200704000000"


// Notes
// Assume Date year input will always be greater than 1970.

// Try not to rely on the default Date.toString() output in your implementation.

// Be aware that the Date's month field is zero based (0 is January and 11 is December).

class Date{
    constructor(year=1970, month=0, day=1, hour=0, min=0, sec=0){
        this.year= year;
        this.month=month;
        this.day= day;
        this.hour= hour;
        this.min= min;
        this.sec= sec;
    }

}

function formatDate(date){
    console.log(date);
    let arr= Object.values(date).map((item,index)=>{
        if(index==1){
            item=item+1;
        }
        let stred=String(item);
        if(stred.length<2){
            stred=`0${stred}`;
        }
        return stred;
    })
    console.log(arr.join(""));
}

formatDate(new Date(2020, 6, 4));