const readline= require ('readline-sync')
const n1 = readline.questionFloat('Digite o primeiro número: ')
const n2 = readline.questionFloat('Digite o segundo número: ')
const n3 = readline.questionFloat('Digite o terceiro número: ')


let media = (n1 + n2 + n3) / 3
console.log(`A média dos números ${media.toFixed(2)}`)