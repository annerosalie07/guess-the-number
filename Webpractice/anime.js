console.log('JavaScript is linked!');
const greetButton = document.getElementById("greetButton");
const nameInput = document.getElementById("nameInput");

if (greetButton && nameInput) {
    greetButton.addEventListener("click", function () {
        const name = nameInput.value.trim(); 
        if (name) {
            alert(`Hello, ${name}!`); 
        } else {
            alert("Please enter your name."); 
        }
    });
} else {
    console.error("Greet Me button not found!");
}

const buttons = document.querySelectorAll("button:not(#greetButton)"); 

buttons.forEach((button) => {
    if (button.id !== "greetButton") {
        button.addEventListener("click", function () {
            alert(`You clicked a button: ${button.textContent}`);
        });
    }
});
