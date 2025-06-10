const readline = require('readline-sync')

const idade = readline.questionInt('Qual a sua idade? ')


if (idade > 18){
    console.log('Obrigatório votar.')
} if (idade > 65){
    console.log('Não são obrigados votar.')
} else if (idade > 16 && idade < 17 ){
    console.log('Voto opcional')
} else if(idade < 16){
    console.log('Não pode votar.')
}
// else {
//     console.log('Você é menor de idade.')


