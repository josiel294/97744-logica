// Função.
const somar = (a,b) => {
    return a + b
}

// função
const subtrair = (a,b) => a - b

// Função 
const multiplicar = (a,b) =>{
    return a*b
}

// Função
const dividir = (a,b) => a/b
// chamando a função
const soma = somar (2,3)
const subtracao = subtrair (2,3)
const multiplicacao = multiplicar (2,3)
const divisao = dividir (2,3)
// Exibindo o resultado

console.log(`A Soma: ${soma}`)
console.log(`A Subtração: ${subtracao}`)
console.log(`A Multiplicação: ${multiplicacao}`)
console.log(`A Divisão: ${divisao.toFixed(2)}`)