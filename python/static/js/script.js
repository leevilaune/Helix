console.log("Hello World!");

async function submitForm() {
    let backendUrl = document.getElementById('backend-url');
    console.log(backendUrl.dataset.url);
    const url = backendUrl.dataset.url;
    const data = {
        name: document.getElementById('username').value,
        password:document.getElementById('password').value,
    }
    console.log(data)
    try {
        const response = await fetch('http://80.220.204.247:3000/auth', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({data})
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const status = await response.json();  // Parse the JSON data
        console.log(status);  // Do something with the data
        console.log(status.username);
        window.location.href = `/user/${status.username}`;  // Redirect to the specified URL`
    } catch (error) {
        console.error('Error during fetch operation:', error);
    }
}
