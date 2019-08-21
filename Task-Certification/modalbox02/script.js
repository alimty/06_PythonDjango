
// import "./styles.css";


// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("goGoogle");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// Get the Cancel button that closes the modal
var cancel = document.getElementById("btnCancel");

// Get the YES button that closes the modal
var clickYes = document.getElementById("btnYes");

// When the user clicks the button, open the modal 
btn.onclick = function(e) {
  e.preventDefault();
  modal.style.display = "block";
}
// When the user clicks on <YES>, close the modal
clickYes.onclick = function() {
  // modal.style.display = "none";
  //window.location = "http://www.google.com";
  //document.location.replace('http://www.google.com');
 

}
// When the user clicks on <cancel>, close the modal
cancel.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target === modal) {
    modal.style.display = "none";
  }
}

// function openModal() {
//  document.getElementsById("myModal").style.display = "block";
// }

// function closeModal (){
//  document.getElementById("myModal").style.display = "none";
// }



