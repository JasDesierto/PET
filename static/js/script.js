// script.js

document.getElementById("expense-form").addEventListener("submit", async function(e) {
    e.preventDefault();
  
    const month = document.getElementById("month").value;
    const expense = parseFloat(document.getElementById("expense").value);
  
    const response = await fetch("http://127.0.0.1:5000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ month, expense })
    });
  
    const result = await response.json();
    document.getElementById("message").innerText = result.message || result.error;
  });
  
  document.getElementById("load-summary").addEventListener("click", async function() {
    const response = await fetch("http://127.0.0.1:5000/summary");
    const result = await response.json();
  
    document.getElementById("summary-output").innerText = JSON.stringify(result, null, 2);
  });
  