import sys

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

def remove_comments_and_whitespace(line):
	without_comments = line.split('/')[0]
	return without_comments.replace(' ', '')

def divideInLine(texto):
	comands = []
	for line in texto.split('\r\n'):
		stripped = remove_comments_and_whitespace(line)
		if stripped:
			comands.append(stripped)
	return comands

simbolos = {
	'R0': 0,
	'R1': 1,
	'R2': 2,
	'R3': 3,
	'R4': 4,
	'R5': 5,
	'R6': 6,
	'R7': 7,
	'R8': 8,
	'R9': 9,
	'R10': 10,
	'R11': 11,
	'R12': 12,
	'R13': 13,
	'R14': 14,
	'R15': 15,
	'SCREEN': 16384,
	'KBD': 24576,
	'SP': 0,
	'LCL': 1,
	'ARG': 2,
	'THIS': 3,
	'THAT': 4
}

destino = {
	'': '000',
	'M': '001',
	'D': '010',
	'MD': '011',
	'A': '100',
	'AM': '101',
	'AD': '110',
	'AMD': '111'
}

jump = {
	'': '000',
	'JGT': '001',
	'JEQ': '010',
	'JGE': '011',
	'JLT': '100',
	'JNE': '101',
	'JLE': '110',
	'JMP': '111'
}

opcoes = {
	'0': '0101010',
	'1': '0111111',
	'-1': '0111010',
	'D': '0001100',
	'A': '0110000',
	'!D': '0001101',
	'!A': '0110001',
	'-D': '0001111',
	'-A': '0110011',
	'D+1': '0011111',
	'A+1': '0110111',
	'D-1': '0001110',
	'A-1': '0110010',
	'D+A': '0000010',
	'D-A': '0110011',
	'A-D': '0000111',
	'D&A': '0000000',
	'D|A': '0110101',
	'M': '1110000',
	'!M': '1110001',
	'-M': '1110011',
	'M+1': '1110111',
	'M-1': '1110010',
	'D+M': '1000010',
	'D-M': '1010011',
	'M-D': '1000111',
	'D&M': '1000000',
	'D|M': '1010101'
}

posicao_atual = 16

try:
	receber = sys.argv[1].split('/')
	number = len(receber)
	nome = receber[number-1].split('.')
	if nome[1] != "asm":
		print("O arquivo passado nao e valido, por favor insira um arquivo .asm")
	else:
		code_nome = "./" + nome[0] + ".hack"
		arq = open(sys.argv[1])
		texto = arq.read()
		arq.close()
		result = ""
		comands = divideInLine(texto)
		j = 0
		i = 0
		lenght = len(comands)
		while j < lenght:
			line = comands[j]
			if (line[0] == '('):
				a = line.replace('(', '')
				symbol = a.replace(')','')
				simbolos[symbol] = j
				comands.pop(j) 
				j = j-1
				lenght = lenght-1
			j = j+1
		while i < lenght:
			code = ""
			line = comands[i]
			if (line[0] == '@'):
				symbol = line.replace('@', '')
				if isnumber(symbol):
					code = bin(int(symbol))[2:].zfill(16) + "\n"
				else:
					if symbol not in simbolos:
						simbolos[symbol] = posicao_atual
						posicao_atual = posicao_atual + 1
					code = bin(simbolos[symbol])[2:].zfill(16) + "\n"
			else:
				code = "111"
				base = line.split('=')
				if(len(base) == 2):
					dest = destino[base[0]]
					symbol = base[1]
					points = symbol.split(';')
					if(len(points) == 2):
						codigo = opcoes[points[0]]
						jumper = jump[points[1]]
					else:
						codigo = opcoes[points[0]]
						jumper = "000"
				else:
					dest = "000"
					symbol = base[0]
					points = symbol.split(';')
					if(len(points) == 2):
						codigo = opcoes[points[0]]
						jumper = jump[points[1]]
					else:
						codigo = opcoes[points[0]]
						jumper = "000"
				code = code + codigo + dest + jumper + "\n"
			result = result + code
			i = i+1
		try:
			arquivo = open(code_nome, 'r+')
			arquivo.writelines(result)
			mensagemsucesso = "Arquivo " + nome[0] + ".hack atualizado com sucesso!"
			print(mensagemsucesso)
		except:
    			arquivo = open(code_nome, 'w+')
			arquivo.writelines(result)
			mensagemsucesso = "Arquivo " + nome[0] + ".hack criado com sucesso!"
			print(mensagemsucesso)
		arquivo.close()
except IndexError:
	print("Adicione um arquivo .asm")
