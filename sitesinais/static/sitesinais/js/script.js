const getDB = () => {
    fetch("http://localhost:5000/api/getdb")
    .then(resposta => resposta.json())
    .then(data => {
        for (let i = 0; i < 14 + 1; i++) {
            const box = document.querySelector(`#box-${i + 1}`);
            box.style.backgroundColor = data[i].backgroundColor;
        }
    });
};



const getestatics = () => {
    fetch("http://localhost:5000/api/estatics")
    .then(resposta1 => resposta1.json())
    .then(data =>{
        document.querySelector('#valuewhite').innerHTML = data.white + 'x';
        document.querySelector('#valueblack').innerHTML = data.black + 'x';
        document.querySelector('#valuered').innerHTML = data.red + 'x';
    })
}

setInterval(getDB, 4000)
setInterval(getestatics, 5000)