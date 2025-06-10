// 1. Importando o módulo 'readline-sync' corretamente.
// Se você ainda não o instalou, abra o terminal e execute: npm install readline-sync
const readline = require('readline-sync');

// 2. Solicitando o número ao usuário.
// A função questionInt já converte a entrada para um número inteiro.
const numero = readline.questionInt('Digite o número: ');

// 3. Verificando se o número é válido (boa prática)
if (isNaN(numero)) {
    console.log("Entrada inválida. Por favor, digite um número.");
} else {
    console.log(`\nTabuada de multiplicação do ${numero}:`);

    // 4. Corrigindo o loop 'for'
    //    - 'let let i' corrigido para 'let i'
    //    - 'i' inicializado com 1 (para tabuada padrão: numero x 1, numero x 2, ...)
    //    - Condição do loop alterada para 'i <= 10' (para tabuada até 10)
    //    - Incremento corrigido para 'i++'
    //    - Ação dentro do loop: calcular e imprimir cada linha da tabuada
    for (let i = 1; i <= 10; i++) {
        // A variável 'tabuada' no seu código original não estava sendo usada para exibir resultados.
        // Aqui, calculamos e imprimimos cada linha.
        console.log(`${numero} x ${i} = ${numero * i}`);
    }
}