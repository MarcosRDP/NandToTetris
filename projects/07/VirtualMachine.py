import sys

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

def remove_comments_and_whitespace(line):
	without_comments = line.split('/')[0]
	return without_comments

def divideInLine(texto):
	comands = []
	for line in texto.split('\r\n'):
		stripped = remove_comments_and_whitespace(line)
		if stripped:
			comands.append(stripped)
	return comands

numbereq = 0
numbergt = 0
numberlt = 0

try:
	receber = sys.argv[1].split('/')
	number = len(receber)
	nome = receber[number-1].split('.')
	if nome[1] != "vm":
		print("O arquivo passado nao e valido, por favor insira um arquivo .vm")
	else:
		code_nome = "./" + nome[0] + ".asm"
		arq = open(sys.argv[1])
		texto = arq.read()
		arq.close()
		result = ""
		comands = divideInLine(texto)
		i = 0
		lenght = len(comands)
		while i < lenght:
			code = ""
			line = comands[i]
			words = line.split(' ')
			if (words[0] == 'push'):
				if (words[1] == 'constant'):
					code = "@" + words[2] + "\nD=A\n"
					code = code + "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
				elif(words[1] == 'argument'): #Pegar variavel do registrador 2
					code = "@" + words[2] + "\nD=A\n"
					code = code + "@ARG\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
				elif(words[1] == 'pointer'):
					if(words[2] == '0'):
						code = code + "@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
					if(words[2] == '1'):
						code = code + "@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
				elif(words[1] == 'this'): #Pegar variavel do registrador 3
					code = "@" + words[2] + "\nD=A\n"
					code = code + "@THIS\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
				elif(words[1] == 'that'): #Pegar variavel do registrador 4
					code = "@" + words[2] + "\nD=A\n"
					code = code + "@THAT\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
				elif(words[1] == 'temp'):
					numero = 5 + int(words[2])
					code = "@" + str(numero) + "\nD=M\n"
					code = code + "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
				elif(words[1] == 'static'):
					numero = 16 + int(words[2])
					code = "@" + str(numero) + "\nD=M\n"
					code = code + "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
				elif(words[1] == 'local'): #Pegar variavel do registrador 1
					code = "@" + words[2] + "\nD=A\n"
					code = code + "@LCL\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
			elif(words[0] == 'pop'):
				numero = 0
				code = "@SP\nA=M-1\nD=M\n@SP\nM=M-1\n"
				if(words[1] == 'argument'): #Pegar variavel do registrador 2
					code = "@" + words[2] + "\nD=A\n"
					code = code + "@ARG\nM=M+D\n@SP\nA=M-1\nD=M\n@SP\nM=M-1\n@ARG\nA=M\nM=D\n"
					code = code + "@" + words[2] + "\nD=A\n"
					code = code + "@ARG\nM=M-D\n"
				elif(words[1] == 'pointer'):
					if(words[2] == '0'):
						code = "@SP\nA=M-1\nD=M\n@SP\nM=M-1\n@THIS\nM=D\n"
					if(words[2] == '1'):
						code = "@SP\nA=M-1\nD=M\n@SP\nM=M-1\n@THAT\nM=D\n"
				elif(words[1] == 'this'): #Pegar variavel do registrador 3
					code = "@" + words[2] + "\nD=A\n"
					code = code + "@THIS\nM=M+D\n@SP\nA=M-1\nD=M\n@SP\nM=M-1\n@THIS\nA=M\nM=D\n"
					code = code + "@" + words[2] + "\nD=A\n"
					code = code + "@THIS\nM=M-D\n"
				elif(words[1] == 'that'): #Pegar variavel do registrador 4
					code = "@" + words[2] + "\nD=A\n"
					code = code + "@THAT\nM=M+D\n@SP\nA=M-1\nD=M\n@SP\nM=M-1\n@THAT\nA=M\nM=D\n"
					code = code + "@" + words[2] + "\nD=A\n"
					code = code + "@THAT\nM=M-D\n"
				elif(words[1] == 'temp'):
					numero = 5 + int(words[2])
					code = code + "@" + str(numero) + "\nM=D\n"
				elif(words[1] == 'static'):
					numero = 16 + int(words[2])
					code = code + "@" + str(numero) + "\nM=D\n"
				elif(words[1] == 'local'): #Pegar variavel do registrador 1
					code = "@" + words[2] + "\nD=A\n"
					code = code + "@LCL\nM=M+D\n@SP\nA=M-1\nD=M\n@SP\nM=M-1\n@LCL\nA=M\nM=D\n"
					code = code + "@" + words[2] + "\nD=A\n"
					code = code + "@LCL\nM=M-D\n"
			elif(words[0] == 'add'):
				code = "@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nM=M+D\n"
			elif(words[0] == 'sub'):
				code = "@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nM=M-D\n"
			elif(words[0] == 'neg'):
				code = "@SP\nA=M-1\nM=-M\n"
			elif(words[0] == 'eq'):
				code = "@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nM=M-D\n"
				code = code + "@SP\nA=M-1\nD=M\n@JUMPEQ1" + str(numbereq) + "\nD,JEQ\n@SP\nA=M-1\nM=0\n"
				code = code + "@JUMPEQ2" + str(numbereq) + "\n0,JMP\n(JUMPEQ1" + str(numbereq) + ")\n"
				code = code + "@SP\nA=M-1\nM=-1\n(JUMPEQ2" + str(numbereq) + ")\n"
				numbereq = numbereq + 1
			elif(words[0] == 'gt'):
				code = "@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nM=M-D\n"
				code = code + "@SP\nA=M-1\nD=M\n@JUMPGT1" + str(numbergt) + "\nD,JGT\n@SP\nA=M-1\nM=0\n"
				code = code + "@JUMPGT2" + str(numbergt) + "\n0,JMP\n(JUMPGT1" + str(numbergt) + ")\n"
				code = code + "@SP\nA=M-1\nM=-1\n(JUMPGT2" + str(numbergt) + ")\n"
				numbergt = numbergt + 1
			elif(words[0] == 'lt'):
				code = "@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nM=M-D\n"
				code = code + "@SP\nA=M-1\nD=M\n@JUMPLT1" + str(numberlt) + "\nD,JLT\n@SP\nA=M-1\nM=0\n"
				code = code + "@JUMPLT2" + str(numberlt) + "\n0,JMP\n(JUMPLT1" + str(numberlt) + ")\n"
				code = code + "@SP\nA=M-1\nM=-1\n(JUMPLT2" + str(numberlt) + ")\n"
				numberlt = numberlt + 1
			elif(words[0] == 'and'):
				code = "@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nM=D&M\n"
			elif(words[0] == 'or'):
				code = "@SP\nA=M-1\nD=M\n@SP\nM=M-1\nA=M-1\nM=D|M\n"
			elif(words[0] == 'not'):
				code = "@SP\nA=M-1\nM=!M\n"
			result = result + code
			i = i+1
		result = result + "(END)\n@END\n0,JMP"
		try:
			arquivo = open(code_nome, 'r+')
			arquivo.writelines(result)
			mensagemsucesso = "Arquivo " + nome[0] + ".asm atualizado com sucesso!"
			print(mensagemsucesso)
		except:
    			arquivo = open(code_nome, 'w+')
			arquivo.writelines(result)
			mensagemsucesso = "Arquivo " + nome[0] + ".asm criado com sucesso!"
			print(mensagemsucesso)
		arquivo.close()
except IndexError:
	print("Adicione um arquivo .vm")
