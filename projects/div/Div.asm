// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
@R1
D=M //Salva o valor do denominador

@80
D,JEQ //Se o denominador for 0, pula para depois do final do programa

@R0
D=M //Salva o valor de R0

@saver0
M=D //Salva o valor de R0

@primeironegativo
M=0 //Guarda o valor do primeiro negativo como sendo falso/0

@16
D,JGE

@primeironegativo
M=1 //Guarda o valor do primeiro negativo como sendo verdadeiro/0

@saver0
M=-M //Remove o valor negativo do numerador

@R1
D=M //Salva o valor de R1

@saver1
M=D //Salva o valor de R1

@segundonegativo
M=0 //Guarda o valor do segundo negativo como sendo falso/0

@28
D,JGE

@segundonegativo
M=1 //Guarda o valor do segundo negativo como sendo verdadeiro/0

@saver1
M=-M //Remove o valor negativo do denominador

@saver0
D=M //Salva o valor de R0

@quociente
M=0 //Prepara o valor do quociente

@resto
M=D //Prepara o valor do resto
D=M //Seta o valor do resto para verificar

@saver1
D=D-M //Subtrai o resto do valor do quociente

@calculo
M=D //Verifica se o resto é menor que o denominador

@52
D,JLT //Pula para o final se o resto é menor que o denominador

@quociente
M=M+1 //Atualiza o valor de quociente

@saver1
D=M //Salva o valor do denominador

@resto
M=M-D //Atualiza o valor do resto

@calculo
M=M-D //Atualiza o valor do resto menos o denominador
D=M //Salva esse valor

@40
D,JGE //Volta ao início da operação se o resto menos o denominador é maior ou igual a 0

@primeironegativo
D=M //Salva se o numerador é negativo

@64
D,JEQ //Se o numerador for negativo, ou seja seu valor for 1/true, executa a próxima instrução, caso contrario pula ela

@resto
D=M //Salva o valor de resto

@62
D,JEQ //Pula a proxima operacao, caso resto seja zero

@quociente
M=M+1 //Soma 1 ao valor do quociente

@quociente
M=-M //Transforma o valor do quociente em negativo

@segundonegativo
D=M //Salva se o denominador é negativo

@70
D,JEQ //Se o denominador for negativo, ou seja seu valor for 1/true, executa a próxima instrução, caso contrario pula ela

@quociente
M=-M //Transforma o valor do quociente em negativo

@quociente
D=M //Salva o valor do quociente

@R2
M=D //Passa o valor do quociente na variavel de saída

@resto
D=M //Salva o valor do resto

@R3
M=D //Passa o valor do resto na variavel de saída

@78
0,JMP //Finaliza o programa

@R2
M=0 //O quociente deve ser 0 em caso do denominador ser zero

@32767
D=A //Prepara o valor do resto

@R3
M=D //O resto deve ser 32767 em caso do denominador ser zero

@78
0,JMP //Finaliza o programa
