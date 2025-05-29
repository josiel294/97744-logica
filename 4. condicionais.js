const idade = 2
if (idade < 18) {
    console.log('Você é maior de idade:')
}
else if (idade >= 18 && idade < 60) {
    console.log('Você é adulto:')
}
else if (idade >= 60) {
    console.log('Você é idoso:')
}
else {
    console.log('Você é menor de idade:')
}