function addGif(event){
    event.preventDefault();
    let search= document.forms[0]["search"].value;
    let xhr= new XMLHttpRequest();
    xhr.open("GET",`https://api.giphy.com/v1/gifs/random?tag=${search}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&rating=g`);
    xhr.send();
    xhr.responseType="json";
    let gif= document.createElement("div");
    let img=document.createElement("img");
    let delbut=document.createElement("button");
    delbut.textContent= "DELETE";
    xhr.onload= function(){
        img.src=xhr.response["data"]["images"]["downsized"]["url"];
        console.log(xhr.response);;
        img.style.width="100px";
        img.style.height="100px";
        gif.appendChild(img);
        gif.appendChild(delbut);
        delbut.addEventListener("click", function(event){
            document.body.removeChild(gif);
        })
        document.body.appendChild(gif);
    }
}

function delAll(){
    let gifs=document.getElementsByTagName("div");
    let len=gifs.length;
    for(let x=0; x<len;x++){
        document.body.removeChild(gifs[0]);
    }
}