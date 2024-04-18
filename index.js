//CALCULATOR PROGRAM
let isClearAll = true;

const display = document.getElementById("display");
const clearButton = document.getElementById("clearButton");

function appendToDisplay(input){
    if (isClearAll) {
        display.value = "";
        isClearAll = false;  
        clearButton.textContent = "C";
    } 
    display.value += input;
}

function toggleClear(){   
    if (isClearAll){
        clearDisplay();  
    } else {
        isClearAll = true;
        clearButton.textContent = "C";
        
    }
}

function clearDisplay() {
    display.value = "";
    isClearAll = true;
    clearButton.textContent = "AC";
}

function calculate(){
    try {
        let result;
        result = evaluateResult(display.value);
        display.value = result;
    }
    catch(error){
        display.value = "Error";
    }
}

function evaluateResult(input){
    input = input.replace(/sin/g, 'Math.sin');
    input = input.replace(/cos/g, 'Math.cos');
    input = input.replace(/tan/g, 'Math.tan');
    input = input.replace(/log₁₀/g, 'Math.log10');
    input = input.replace(/π/g, 'Math.PI');
    input = input.replace(/e/g,'Math.E');
    input = input.replace(/EE/g, 'Math.EE');

    const result = new Function('return ' + input)();

    return result;
}

const expandText = document.getElementById('expandText');

expandText.addEventListener('mouseenter', function() {
  this.querySelector('.expanded-content').style.display = 'block';
});

expandText.addEventListener('mouseleave', function() {
  this.querySelector('.expanded-content').style.display = 'none';
});

