document.getElementById("info").onsubmit = function(e){
    e.preventDefault();
    fetch('/set_informacion', {
        method : 'POST',
        body: JSON.stringify({
            'informacion': document.getElementById('tema').value,
            'topico': document.getElementById('topico').value
        }),
        headers : {
            'Content-Type' : 'application/json'
        },
    })
}

