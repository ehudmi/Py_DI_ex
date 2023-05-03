const gameInfo = [
    {
      username: "john",
      team: "red",
      score: 5,
      items: ["ball", "book", "pen"]
    },
    {
      username: "becky",
      team: "blue",
      score: 10,
      items: ["tape", "backpack", "pen"]
    },
    {
      username: "susy",
      team: "red",
      score: 55,
      items: ["ball", "eraser", "pen"]
    },
    {
      username: "tyson",
      team: "green",
      score: 1,
      items: ["book", "pen"]
    },
   ];
//    const usernames=[];

//    gameInfo.forEach(item =>{
//     usernames.push(`${item.username}!`);
//    })
//    console.log(usernames);

// const winners=[];
// gameInfo.forEach(item=> item.score>5?winners.push(item.username):false);
// console.log(winners);

let score=0;
gameInfo.forEach(item=>score=score+item.score);
console.log(score);