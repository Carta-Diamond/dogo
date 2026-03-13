document.getElementById('btn-register').addEventListener("click", register);

function register(){
    var password = document.getElementById('user-password').value
    var repeat_password = document.getElementById('user-confirm-password').value
    
    if(password != repeat_password){
        alert("Las contraseñas no coinciden")
        return;

        // sweetalert2
    }

    const data = {
        name: document.getElementById('user-name').value,
        email: document.getElementById('user-email').value,
        password: document.getElementById('user-password').value,   
    };

            //endpoint
    fetch('api/users', {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify(data)
    }).then(response => response.json())
    .then(result => {
        if(result.success){
            alert("Usuario guardo correctamente")
        }else{
            alert("Error al guardar el usuario")
        }
    })
    .catch(error => {
        console.error(error);
    });



}