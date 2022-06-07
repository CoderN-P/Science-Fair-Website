function waterPlant(ip) {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", `http://${ip}:5000/webhook`, true);
    xhttp.setRequestHeader('Content-type', 'application/json');
    xhttp.addEventListener('load', reqListener);


    xhttp.send(JSON.stringify({
        ip: document.querySelector('#ipin').value,
        password: document.querySelector('#psw').value
    }));
}

function reqListener() {
    let text = document.querySelector('#result');

    text.innerHTML = 'Your plant was successfully watered!';
    text.style.color = 'green';

}
