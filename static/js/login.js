document.getElementById("login").onsubmit = function(e){
    e.preventDefault();
    fetch('/authenticate', {
        method : 'POST',
        body: JSON.stringify({
            'username': document.getElementById('username').value,
            'password': document.getElementById('password').value,
            'tipo' : document.getElementById('selector').value
        }),
        headers : {
            'Content-Type' : 'application/json'
        },
    })
}

