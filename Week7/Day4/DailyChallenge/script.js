let saved=[];

class Video {
    constructor(title, uploader,time){
        this.title= title;
        this.uploader=uploader;
        this.time=time;
        if(saved.length<5){
            saved.push(this)
        }
        else{
            saved.splice(0,1);
            saved.push(this)
        }
    }
    watch(){
        console.log(`${this.uploader} watched all ${this.time} of ${this.title}!`);
    }
    
}

let Lesson1= new Video("HTML Basics", "DI", "3 hours");
console.log(Lesson1);
let Lesson2= new Video("CSS Basics", "Developers Institute", "3 hours and 30 minutes");
let Lesson3=new Video("CSS Advanced", "Developers Institute", "2 hours and 30 minutes");
let Lesson4=new Video("HTML Advanced", "Developers Institute", "4 hours");
let Lesson5=new Video("JS Basics", "Developers Institute", "3 hours");
saved.forEach(item=> item.watch())