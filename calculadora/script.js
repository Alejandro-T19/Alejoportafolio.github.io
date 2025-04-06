function calcular() {
  let n1 = parseFloat(document.getElementById("n1").value);
  let n2 = parseFloat(document.getElementById("n2").value);
  let n3 = parseFloat(document.getElementById("n3").value);

  let resultado = document.getElementById("resultado");

  if (isNaN(n1) || isNaN(n2) || isNaN(n3)) {
    resultado.innerText = "Por favor ingresa todas las notas.";
    resultado.classList.add("resultado-visible");
    return;
  }

  let promedio = (n1 + n2 + n3) / 3;
  resultado.innerText = "Tu promedio es: " + promedio.toFixed(2);
  resultado.classList.add("resultado-visible");
}
