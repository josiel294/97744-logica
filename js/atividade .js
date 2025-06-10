const listaDeNumeros = [1, 2, 3, 4, 5]

impares = []
pares = []


function par (lista) {
    return lista.filter(numero => numero % 2 === 0, pares + 1)
}
function impar (lista) {
    return lista.filter(numero => numero % 2 !== 0, impares + 1)
}








const pares = par (listaDeNumeros)
const impares = impar (listaDeNumeros)


console.log(`Quantidade de números ímpares: ${impares}`)
console.log(`Quantidade de números pares: ${pares}`)
console.log(`Números: ${listaDeNumeros}`)