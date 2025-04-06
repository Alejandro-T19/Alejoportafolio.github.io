document.getElementById("contact-form").addEventListener("submit", function(e) {
    e.preventDefault();
  
    const nombre = document.getElementById("nombre").value.trim();
    const email = document.getElementById("email").value.trim();
    const mensaje = document.getElementById("mensaje").value.trim();
    const msg = document.getElementById("mensaje-validacion");
  
    if (nombre && email && mensaje) {
      msg.textContent = "✅ ¡Formulario enviado con éxito!";
      msg.style.color = "green";
      this.reset(); // Limpia los campos
    } else {
      msg.textContent = "⚠️ Por favor completa todos los campos.";
      msg.style.color = "red";
    }
  });
  