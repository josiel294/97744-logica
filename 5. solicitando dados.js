// Instalar : npm install readline-sync
const readline = require('readline-sync')

const idade = readline.questionInt('Qual a sua idade? ')

if (idade < 18) {
    console.log('Você é menor de idade.')
}   else {
    console.log('Você é maior de idade.')
}