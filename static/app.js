function getSummary() {
    const reportData = document.getElementById('reportData').value;

    fetch('/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `reportData=${reportData}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('summaryOutput').innerText = data.summary;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
