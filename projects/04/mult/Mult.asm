// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
@R2
M=0 //Seta a resposta como zero

@R1
D=M //Salva o valor de R1

@contador
M=D //E o coloque em outra variavel

@17
D,JEQ //Verifique se esse valor é maior que zero

@R0
D=M //Se for, salve o valor de R0

@R2
M=M+D //Some o valor de R2 no de R0

@contador
M=M-1 //Reduza o valor de contador 
D=M //Salve o valor de contador

@8
D,JGT //Verifica se o contador chegou em zero, caso não tenha volta para a linha 8

@17
0,JMP //Finaliza o programa
