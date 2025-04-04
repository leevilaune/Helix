console.log("Hello World!");
let token = ""

let user = "";
const userid = 0;

async function submitForm() {
    const data = {
        name: document.getElementById('username').value,
        password:document.getElementById('password').value,
    }
    console.log(data)
    try {
        const response = await fetch('/auth', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({data})
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const status = await response.json();
        console.log(status);
        console.log(status.username);
        if(status.status===true){
            token = status.token;
            user = status.user;

            const auth = {
                user: status.user,
                token: status.token
            }
            window.location.href = `/user/${status.username}?token=${token}`;
        }
    } catch (error) {
        console.error('Error during fetch operation:', error);
    }
}
