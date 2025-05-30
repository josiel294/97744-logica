const alunos =['marta', 'jose', 'maria']
console.log('\nExibindo os elementos')
console.log(alunos)

console.log('\nExibindo o primeiro elemento')
console.log(alunos[0])
console.log('\nExibindo o último')
console.log(alunos[2])

console.log('\nAdicionando um elemento no final do vetor')
alunos.push('ana')
console.log(alunos)

console.log('\nAdicionando um elemento no início do vetor.')
alunos.unshift('Marilia')
console.log(alunos)

console.log('\nRemovendo um elemento no final do vetor.')
alunos.pop()
console.log(alunos)

console.log('\nRemovendo apenas um elemento do vetor.')
alunos.pop(2) // Removendo o terceiro elemento do vetor.
console.log(alunos)