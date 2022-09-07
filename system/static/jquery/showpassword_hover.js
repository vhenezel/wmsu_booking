function password_show_hides() {
  var x = document.getElementById("passwordw");
  var y = document.getElementById("confirm_pass");
  var show_eye = document.getElementById("show_eye");
  var hide_eye = document.getElementById("hide_eye");

  hide_eye.classList.remove("d-none");
  if (x.type === "password" && y.type === "password") {
    x.type = "text";
    y.type = "text";
    show_eye.style.display = "none";
    hide_eye.style.display = "block";
  } else {
    x.type = "password";
    y.type = "password";
    show_eye.style.display = "block";
    hide_eye.style.display = "none";
  }
}

function password_show_hides1() {
  var x = document.getElementById("password");
  var show_eye = document.getElementById("show_eye");
  var hide_eye = document.getElementById("hide_eye");

  hide_eye.classList.remove("d-none");
  if (x.type === "password") {
    x.type = "text";
    show_eye.style.display = "none";
    hide_eye.style.display = "block";
  } else {
    x.type = "password";
    show_eye.style.display = "block";
    hide_eye.style.display = "none";
  }
}