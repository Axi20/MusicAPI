function sendPost(){
    const data = JSON.stringify({
        title: document.getElementById("title").value,
        singer: document.getElementById("singer").value,
        genre:document.getElementById("genre").value,
        timeline:document.getElementById("timeline").value
      
      });
      
      navigator.sendBeacon('http://127.0.0.1:5000/savedetails/', data);
      console.log(data);
    }
