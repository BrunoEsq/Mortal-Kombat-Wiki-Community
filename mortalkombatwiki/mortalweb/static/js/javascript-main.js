function openHouse(clase) {
  // Obtén todos los elementos con la clase proporcionada
  let elementosConClase = document.getElementsByClassName(clase);
  // Verifica si se encontraron elementos con esa clase
  if (elementosConClase.length > 0) {
    // Cambia la imagen del primer elemento encontrado
    elementosConClase[0].setAttribute("src", "../Imagenes/icono-home-abierto.png");
  } else {
    console.error("No se encontraron elementos con la clase especificada");
  }
}

function fightFighter(clase) {
  // Obtén todos los elementos con la clase proporcionada
  let elementosConClase = document.getElementsByClassName(clase);
  // Verifica si se encontraron elementos con esa clase
  if (elementosConClase.length > 0) {
    // Cambia la imagen del primer elemento encontrado
    elementosConClase[0].setAttribute("src", "../Imagenes/muaythai-illustration-icon-free-abierto.png");
  } else {
    console.error("No se encontraron elementos con la clase especificada");
  }
}

function fightFighterBack(clase) {
  // Obtén todos los elementos con la clase proporcionada
  let elementosConClase = document.getElementsByClassName(clase);
  // Verifica si se encontraron elementos con esa clase
  if (elementosConClase.length > 0) {
    // Cambia la imagen del primer elemento encontrado
    elementosConClase[0].setAttribute("src", "../Imagenes/muaythai-illustration-icon-free-png.png");
  } else {
    console.error("No se encontraron elementos con la clase especificada");
  }
}

function closeHouse(clase) {
  // Obtén todos los elementos con la clase proporcionada
  let elementosConClase = document.getElementsByClassName(clase);
  // Verifica si se encontraron elementos con esa clase
  if (elementosConClase.length > 0) {
    // Cambia la imagen del primer elemento encontrado
    elementosConClase[0].setAttribute("src", "../Imagenes/icono-home-cerrado.png");
  } else {
    console.error("No se encontraron elementos con la clase especificada");
  }
}
let contador = 0;

function hideLiu(clase) {
  let elementosConClase = document.getElementsByClassName(clase);

  if (contador == 0) {
    contador = 1;
    if (elementosConClase.length > 0) {
      elementosConClase[0].style.display = "none";
    } else {
      console.error("No se encontraron elementos con la clase especificada");
    }
  } else if (contador == 1) {
    elementosConClase[0].style.display = "flex";
    contador = 0; // Corregir contador a 0 para cambiar entre hide y show
  }
}