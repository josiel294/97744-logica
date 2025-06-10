// Criando um vetor com números
const listaDeNumeros = [1, 2, 3, 4, 5]

console.log('Listando todos os valores da lista')
console.log(listaDeNumeros)

console.log('\nMultiplicando todos os valores por 2')
const dobrados = listaDeNumeros.map(numero=> numero * 2)
console.log(dobrados)

console.log('\nFiltrando os números pares')
const pares = listaDeNumeros.filter(numero => numero % 2 === 0)
console.log(pares)

console.log('\nSomando todos os números')
const soma = listaDeNumeros.reduce((soma, atual)=> soma + atual, 0)
console.log(soma)