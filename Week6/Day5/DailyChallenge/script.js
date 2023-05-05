let checkTrue =(item) =>item?true:false

let allTruth= (...args) => args.every(checkTrue)
console.log(allTruth(true, true, "a"))