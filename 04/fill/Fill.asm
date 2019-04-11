// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
    @8192
    D=A 
    @Falta
    M=D //Salva o número de pixels que tem de pintar

    @KBD
    D=M //Verivica se alguma tecla foi clicada

    @12
    D;JGT //Se sim, seu valor será um, então a cor terá de ser convertida para -1

    @Cor
    M=0 //Seta a cor como 0, pois ficara branco

    @14
    0;JMP //Pula para depois de setar a cor preta

    @Cor
    M=-1 //Seta a cor preta

    @SCREEN
    D=A //Salva o valor da tela

    @addr
    M=D //Salva as posições da tela

    @Cor
    D=M //Pegua a cor selecionada

    @addr
    A=M //Salva o valor do registrador addr
    M=D

    @addr
    M=M+1 //Atualiza o registrador

    @Falta
    M=M-1 //Atualiza o número de pixels
    D=M //Usa como base

    @0
    D,JEQ //Se não faltar mais nenhum reinicia o programa

    @18
    0,JMP //Se ainda restar, continua pintando
