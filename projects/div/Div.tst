// Projeto ESC 2019-1: Divisão em ASM 

load Div.hack,
output-file Div.out,
compare-to Div.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2 RAM[3]%D2.6.2;

// Caso 1
set PC 0,
set RAM[0] 42, // Argumento: dividendo
set RAM[1] 7;  // Argumento: divisor
repeat 150 {
  ticktock;
}
output;

// Caso 2
set PC 0,
set RAM[0] 3,  // Argumento: dividendo
set RAM[1] 4;  // Argumento: divisor
repeat 150 {
  ticktock;
}
output;

// Caso 3
set PC 0,
set RAM[0] 26, // Argumento: dividendo
set RAM[1] 7;  // Argumento: divisor
repeat 150 {
  ticktock;
}
output;

// Caso 4
set PC 0,
set RAM[0] 0,  // Argumento: dividendo
set RAM[1] 0;  // Argumento: divisor
repeat 150 {
  ticktock;
}
output;

// Caso 5
set PC 0,
set RAM[0] 1,  // Argumento: dividendo
set RAM[1] 0;  // Argumento: divisor
repeat 150 {
  ticktock;
}
output;

// Caso 6
set PC 0,
set RAM[0] 0,  // Argumento: dividendo
set RAM[1] 3;  // Argumento: divisor
repeat 150 {
  ticktock;
}
output;

// Caso 7
set PC 0,
set RAM[0] -42,  // Argumento: dividendo
set RAM[1] 7;  // Argumento: divisor
repeat 150 {
  ticktock;
}
output;

// Caso 8
set PC 0,
set RAM[0] -7, // Argumento: dividendo
set RAM[1] 2;  // Argumento: divisor
repeat 150 {
  ticktock;
}
output;

// Caso 9
set PC 0,
set RAM[0] 7,   // Argumento: dividendo
set RAM[1] -2;  // Argumento: divisor
repeat 150 {
  ticktock;
}
output;

// Caso 10
set PC 0,
set RAM[0] -7,  // Argumento: dividendo
set RAM[1] -2;  // Argumento: divisor
repeat 150 {
  ticktock;
}
output;
