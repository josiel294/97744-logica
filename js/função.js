// Função.
function somar(a,b) {
    return a + b
}

// função
function subtrair(a,b) {
    return a - b
}

// Função
function multiplicar (a,b) {
    return a*b
}

// Função 
function dividir (a,b){
    return a/b
}

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