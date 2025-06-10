const listaDeNumeros = [1, 2, 3, 4, 5, 6]



function par (lista) {
    return lista.filter(numero => numero % 2 === 0)
}
function impar (lista) {
    return lista.filter(numero => numero % 2 !== 0)
}




// Filtrando os números pares

const pares = par (listaDeNumeros)
const impares = impar (listaDeNumeros)


console.log(`Ímpares: ${impares}`)
console.log(`Pares: ${pares}`)
console.log(`Números: ${listaDeNumeros}`)