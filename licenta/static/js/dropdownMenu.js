 // Clicking dropdown button will toggle display
function btnToggle() {
    document.getElementById("mySidenav").classList.toggle("show");
}

// Prevents menu from closing when clicked inside
document.getElementById("mySidenav").addEventListener('click', function (event) {
    alert("click outside");
    event.stopPropagation();
});

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

//side-nav
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

//Homepage redirect
function pageRedirect() {
      window.location.href = "/type";
}

//Login message
 function MyAlert(){
    alert("You are logged in!");
 }
document.getElementById("alertMessage").innerHTML = MyAlert();
