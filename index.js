//CALCULATOR PROGRAM

const display = document.getElementById("display");

function appendToDisplay(input){
    display.value += input;
}

function clearDisplay(){
    display.value = "";
}

function calculate(){
    try {
        display.value = eval(display.value);
    }
    catch(error){
        display.value = "Error";
    }
}

// const expandText = document.getElementById('expandText');

// expandText.addEventListener('mouseenter', function() {
//   this.style.height = '200px'; // Change the height as per your requirement
// });

// expandText.addEventListener('mouseleave', function() {
//   this.style.height = '100px'; // Reset the height
// });

const expandText = document.getElementById('expandText');

expandText.addEventListener('mouseenter', function() {
  this.querySelector('.expanded-content').style.display = 'block';
});

expandText.addEventListener('mouseleave', function() {
  this.querySelector('.expanded-content').style.display = 'none';
});
