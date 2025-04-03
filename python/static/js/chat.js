


async function sendMessage() {
    let input = document.getElementById("userInput");
    let message = input.value.trim();
    if (message === "") return;
    let chatBox = document.getElementById("chatBox");

    const user = document.getElementById("userName").firstChild.nodeValue;
    console.log(user);

    console.log(message);
    const msg = {
        "message": message,
        "user": user,
        "time": new Date().getTime(),
    }
    try {
        const response = await fetch("/api/message/send", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(msg)
        })
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        let userMessage = document.createElement("div");
        userMessage.classList.add("chat-message", "user-message");
        userMessage.innerHTML = `<div class="message-header">${user}</div><div class="message-content">${message}</div>`;
        chatBox.appendChild(userMessage);
    } catch (err) {
        console.log(err);
    }
}
async function updateMessages() {
    let input = document.getElementById("userInput");
    let message = input.value.trim();
    if (message === "") return;
    let chatBox = document.getElementById("chatBox");
    const user = document.getElementById("userName").firstChild.nodeValue;
    console.log(user);

}
async function getMessages() {
    const messages = await fetch(`/api/messages`, {
        method: "GET"
    })
    .then((response) => response.json())
}
setInterval(() => {
    fetch("http://your-api-endpoint.com")
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error("Error:", error));
}, 1000);