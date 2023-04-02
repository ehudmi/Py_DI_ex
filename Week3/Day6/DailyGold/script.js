const numbers = [5,0,9,1,7,4,2,6,3,8];

// Using the .toString() method convert the array to a string.
// Using the .join()method convert the array to a string. Try passing different values into the join.
// Eg .join(“+”), .join(” “), .join(“”)
// Bonus : To do this Bonus look up how to work with nested for loops
// Sort the numbers array in descending order, do so using for loops (Not using built-in sort methods).
// The output should be: [9,8,7,6,5,4,3,2,1,0]
// Hint: The algorithm is called “Bubble Sort”
// Use a temporary variable to swap values in the array.
// Use 2 “nested” for loops (Nested means one inside the other).
// Add comments and console.log the result for each step, this will help you understand.
// let str= numbers.toString();
// console.log(str);
// let str2= numbers.join("+");
// console.log(str2);
let index=numbers.length;
let sorted=[];
for(let x=0;x<index;x++)
{
    let temp=0;
    if(numbers.length>index/2)
    {
        temp=x;
    }
    else{
        temp=index-1-x;
    }
        sorted[x]=numbers[temp];
        for(let i=0;i<numbers.length;i++)
        {
            if(sorted[x]<numbers[i])
            {
                sorted[x]=numbers[i];
            }
        }
    
    let index1= numbers.indexOf(sorted[x]);
    numbers.splice(index1,1);
}
console.log(sorted);