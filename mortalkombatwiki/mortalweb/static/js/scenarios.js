function toggleSwitch() {
    var switchElement = document.getElementById("flexSwitchCheckDefault");
    let navbar = document.getElementById("navbar")
    if (switchElement.checked) {
        navbar.setAttribute("style", "display:none")
    } else {
        navbar.setAttribute("style", "display:inline-block")
    }
  }