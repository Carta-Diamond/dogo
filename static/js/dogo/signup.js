document.getElementById('btn-register').addEventListener("click", register());

function register(){
    password = document.getElementById('user-password').value
    repeat_password = document.getElementById('user-repeat-password').value
    
    if(password != repeat_password){
        alert("Las contraseñas no coinciden")
        return;

        // sweetalert2
    }

    const data = {
        name: document.getElementById('user-name').value,
        email: document.getElementById('user-email').value,
        password: document.getElementById('user-password').value,
        
    }
}