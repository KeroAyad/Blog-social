const alert = document.getElementById("alert");
if (alert.textContent.includes('incorrect')){
alert.classList += " alert-danger"
}
else
alert.classList += " alert-success";
