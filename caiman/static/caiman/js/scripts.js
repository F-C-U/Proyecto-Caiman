function validarGender() {
    var femenino = document.getElementById("femaleGender");
    var masculino = document.getElementById("maleGender");
    var otro = document.getElementById("otherGender");
    var mensajeGender = document.getElementById("mensajeGender");

    if (femenino.checked || masculino.checked || otro.checked) {
        mensajeGender.innerHTML = "";
        return true;
    } else {
        mensajeGender.innerHTML = "Seleccione un género";
        return false;
    }
}

function validarPass() {
    var pass = document.getElementById("pass").value;
    var rePass = document.getElementById("rePass").value;
    var mensajePass = document.getElementById("mensajePass");

    if (pass === rePass) {
        mensajePass.innerHTML = "";
        return true;
    } else {
        mensajePass.innerHTML = "Las contraseñas no coinciden";
        return false;
    }
}

function mostrarPass() {
    var pass = document.getElementById("pass");
    var rePass = document.getElementById("rePass");

    if (pass.type === "password" && rePass.type === "password") {
        pass.type = "text";
        rePass.type = "text";
    } else {
        pass.type = "password";
        rePass.type = "password";
    }
}
