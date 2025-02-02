const backendUrl = "http://127.0.0.1:5000";

function scanURL() {
    const url = document.getElementById("url-input").value;
    fetch(`${backendUrl}/scan`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("scan-result").innerHTML = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error("Error:", error));
}

function submitReport() {
    const description = document.getElementById("description").value;
    const userContact = document.getElementById("user-contact").value;
    fetch(`${backendUrl}/report`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ description, user_contact: userContact })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("report-message").innerText = data.message;
    })
    .catch(error => console.error("Error:", error));
}

function fetchReports() {
    fetch(`${backendUrl}/reports`)
    .then(response => response.json())
    .then(data => {
        document.getElementById("reports-list").innerHTML = JSON.stringify(data, null, 2);
    })
    .catch(error => console.error("Error:", error));
}
