function printNumbers(from, to) {
  let current = from;

  let timerId = setInterval(function() {
    document.getElementById("timer").innerHTML = current;
    if (current == to) {
      clearInterval(timerId);
      window.location.href = 'http://127.0.0.1:8000/';
    }
    current--;
  }, 1000);
}

printNumbers(6, 1)

