

const readline = require('readline-sync')
const numero1 = readline.questionInt('Digite o primeiro número: ')
const numero2 = readline.questionInt('Digite o primeiro número: ')
const numero3 = readline.questionInt('Digite o primeiro número: ')
let soma = numero1 + numero2

if (soma > numero3){
    console.log('A soma dos dois primeiros números é maior que o terceiro.')
} else if (soma < numero3) {
    console.log('A soma dos dois primeiros números é menor que o terceiro.')
} else {
    console.log('A soma dos dois primeiros números é igual ao terceiro.')
}