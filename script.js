function checkPasswordStrength() {
    const password = document.getElementById("password").value;

    fetch('/check-password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ password: password })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById("strength").innerText = `Password Strength: ${data.strength}`;
        const feedbackList = document.getElementById("feedback");
        feedbackList.innerHTML = '';
        data.feedback.forEach(comment => {
            const li = document.createElement("li");
            li.innerText = comment;
            feedbackList.appendChild(li);
        });
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}
