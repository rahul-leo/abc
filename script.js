async function showMessage() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        document.getElementById("message").innerText = data.message;
        document.getElementById("message").classList.add("fade-in");
    } catch (error) {
        console.error('Error fetching data:', error);
        document.getElementById("message").innerText = "Error connecting to backend!";
    }
}

