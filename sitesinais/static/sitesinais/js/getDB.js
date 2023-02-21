const getDB = () => {
    fetch("http://localhost:5000/api/getDB/")
    .then(resposta => resposta.json())
    .then(data => {
        for (let i = 0; i < 14 + 1; i++) {
            const box = document.querySelector(`#box-${i + 1}`);
            box.style.backgroundColor = data[i].backgroundColor;
        }
    });
};

setInterval(getDB, 3000)