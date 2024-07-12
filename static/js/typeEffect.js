var text = 'Sabari Raj..!'; 
var delay = 200; 
var randomness = 100; 
var i = 0;

function type() {
    if (i < text.length) {
        document.getElementById("typing").innerHTML += text.charAt(i);
        i++;
        setTimeout(type, delay + Math.random() * randomness * 2 - randomness);
    } else {
        setTimeout(reset, 1000); 
    }
}

function reset() {
    document.getElementById("typing").innerHTML = "";
    i = 0;
    type();
}

type();
