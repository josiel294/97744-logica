function verificar(numero) {
    if (numero < 0) {
        return 'numero negativo';
    } else if (numero > 0) {
        return 'numero positivo';
    } else {
        return 'numero zero';
    }
}

const readline = require('readline-sync')
const numero = readline.questionInt('Digite um número: ');


const verificado = verificar(numero)


console.log(`O número é: ${verificado}`);
