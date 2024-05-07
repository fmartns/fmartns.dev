const hamrbuguer = document.querySelector("#toggle-btn");

hamrbuguer.addEventListener("click", function(){
    document.querySelector("#sidebar").classList.toggle("expand");
})