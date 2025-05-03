// script.js

// Adds a submit event listener to the form with the id 'expense-form'
// It runs when the user submits the form
document
  .getElementById("expense-form")
  .addEventListener("submit", async function (e) {
    e.preventDefault(); //Prevents the default behavior of form submission (reloading the page)

    // ------------------------------------------------------------------
    // EXPENSE FUNCTION
    // ------------------------------------------------------------------

    // Gets value from input field with ids "month" and "expense"
    const month = document.getElementById("month").value;
    const expense = parseFloat(document.getElementById("expense").value);

    // Sends a POST request to your flask server at the root URL "/"
    // The request body contains the month and expense in JSON format
    const response = await fetch("http://127.0.0.1:5000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ month, expense }),
    });
    // This converts the server's response into a JSON object
    const result = await response.json();
    // Displays either the error or success message from the backend
    document.getElementById("message").innerText =
      result.message || result.error;

    document.getElementById("month").value = "";
    document.getElementById("expense").value = "";
  });

// ------------------------------------------------------------------
// EXPENSE SUMMARY FUNCTION
// ------------------------------------------------------------------

// Adds a click event listener to the button with id "load-summary"
document
  .getElementById("load-summary")
  .addEventListener("click", async function () {
    //Sends a GET request to the  route "/summary"
    const response = await fetch("http://127.0.0.1:5000/summary");
    //Converts the response to JSON format
    const result = await response.json();
    //Displays the returned summary in an indented format inside the "summary"
    document.getElementById("summary-output").innerText = JSON.stringify(
      result,
      null,
      2
    );
  });
