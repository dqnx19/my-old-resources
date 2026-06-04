const day = new Date().getDate();

document.body.style.backgroundImage = `url("https://nether.click/img/wallpapers/${day}.jpg")`;

const style = document.createElement("style");

style.innerHTML = `
body {
            background-image: url("https://nether.click/img/wallpapers/1.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
`;

document.head.appendChild(style);