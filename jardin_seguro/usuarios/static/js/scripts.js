document.addEventListener('DOMContentLoaded', function () {
    const alerta = document.getElementById('alerta');
    if (alerta) {
        setTimeout(function () {
            alerta.style.display = 'none'; 
        }, 3000);
    }

    const loginButton = document.getElementById("loginBtn");
    if (loginButton) {
        loginButton.addEventListener("click", function () {
            var loginUrl = loginButton.getAttribute("data-login-url");
            window.location.href = loginUrl;   
        });
    }

    const deleteButtons = document.querySelectorAll('.btn-delete');
        deleteButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                const cameraId = button.getAttribute('data-camera-id');
                if (confirm('¿Seguro que deseas eliminar esta cámara?')) {
                    window.location.href = `/eliminar-camara/${cameraId}/`;
                }
            });
        });
});