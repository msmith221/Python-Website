const messages = [
        "Welcome to my site!",
        "Welcome, I hope you enjoy your stay!",
        "Hello and welcome to my website!",
        "Welcome to my Python website!"
    ];

    document.getElementById('welcomeMessage').value = messages[Math.floor(Math.random()*messages.length)];