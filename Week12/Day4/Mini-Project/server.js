const express= require('express');
const body_parser= require("body-parser");
const cors= require('cors');
const rss_parser= require('rss-parser');

const app=express();
app.set('view engine', 'ejs');

let Parser = require('rss-parser');
let parser = new Parser();

(async () => {

  let feed = await parser.parseURL('https://thefactfile.org/feed/');
  console.log(feed.title);

  feed.items.forEach(item => {
    console.log(item.title + ':' + item.link)
  });

})();


app.listen(3000, ()=>{console.log('server listening')});