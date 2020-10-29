function validar() {
    var nombre, apellido, rut, pass, correo, tipo, expresionrut, expresioncorreo, user;
    nombre = document.getElementById("nombre").value;
    apellido = document.getElementById("apellido").value;
    rut = document.getElementById("rut").value;
    pass = document.getElementById("pass").value;
    correo = document.getElementById("correo").value;
    tipo = document.getElementById("tipo").value;
    user = document.getElementById("user").value;
    expresionrut = /^\d{1,2}\.\d{3}\.\d{3}[-][0-9kK]{1}$/;
    expresioncorreo = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;

    if (nombre === "" || apellido === "" || rut === "" || correo === "" || tipo === "") {
        alert("Todos los campos son obligatorios");
        return false;
    } else if (nombre.length < 3 || nombre.length > 80) {
        alert("Nombre debe estar entre 3 y 80 caracteres");
        return false;
    } else if (!expresionrut.test(rut)) {
        alert("el rut no es valido");
        return false;
    } else if (apellido.length <= 3 || apellido.length >= 80) {
        alert("El apellido debe estaer entre 3 y 80 caracteres")
        return false;
    } else if (!expresioncorreo.test(correo)) {
        alert("el correo no es valido");
        return false;
    } else if (user.length < 8) {
        alert("El usuario debe tener como minimo 8 caracteres");
    } else if (pass.length < 8){
        alert("El pass debe tener como minimo 8 caracteres");

    }



}



