const readline = require ('readline-sync')
const dia =readline.questionInt('Digite o dia: ')

switch (dia) {
    case 1:
        console.log('Domingo')
        console.log('Final de semana')
        break
    case 2:
        console.log('Segunda-feira')
        console.log('Dia util')
        break
    case 3:
        console.log('Terça-feira')
        console.log('Dia util')
        break
    case 4:
        console.log('Quarta-feira')
        console.log('Qdia util')
        break
    case 5:
        console.log('Quinta-feira')
        console.log('Dia util')
        break
    case 6:
        console.log('Sexta-feira')
        console.log('Dia util')
        break
    case 7:
        console.log('Sábado')
        console.log('final de semana')
        break
    default:
        console.log('Dia inválido')
}