function contagemRegresso (){
    const numeroInput = document.getElementById('numeroInput')
    let numero = parseInt(numeroInput.value)

    const resultadoDiv = document.getElementById('resultadoContagem')
    resultadoDiv.innerHTML = '' // Limpa o conteúdo anterior
   
    resultadoDiv.innerHTML += `<h2>Tabuada do ${numero}:</h2>`

    for (let contagemRegresso = numero) {
        contagemRegresso = numero;
        contagemRegresso >= 0;
        contagemRegresso--
        let resultado = contagemRegresso


    }
}

const gerarBotao = document.getElementById('geradorBotao')
gerarBotao.addEventListener('click', gerarTabuada)
}