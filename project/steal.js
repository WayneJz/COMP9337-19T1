const button = document.getElementById('login');

button.onclick = function() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (!username || !password){
        window.alert('Empty username or password! Try again.');
        return false;
    }

    window.alert('You are hacked!');
    const content = JSON.stringify({
        "username": username,
        "password": password
    });


}