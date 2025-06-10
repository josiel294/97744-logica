const readline = require ('readline-sync')
const numero = readline.questionInt('Digite um número: ')
if (numero < 0) {
    console.log('numero negativo')
} else if (numero > 0) {
    console.log('numero positivo')
}
else {
    console.log('numero zero')
}