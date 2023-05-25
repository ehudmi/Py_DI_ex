function gifData(event){
    let xhr= new XMLHttpRequest();
    xhr.open("GET","https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My");
    xhr.send();
    xhr.responseType="json";
    xhr.onload=function (){
        console.log(xhr.response);
    }
}

function sunData(event){
    let xhr= new XMLHttpRequest();
    xhr.open("GET", "https://api.giphy.com/v1/gifs/search?q=sun&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&limit=10&offset=2");
    xhr.send();
    xhr.responseType="json";
    xhr.onload= function(){
        console.log(xhr.response);
    }
}