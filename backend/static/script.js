document.getElementById("predictionForm").addEventListener("submit",function(e){

e.preventDefault();

const randomPrediction = Math.round(Math.random());

localStorage.setItem("prediction",randomPrediction);

window.location.href="result.html";

});