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
argumentos = 0
static = 0
staticount = 0

try:
	count = 2
	leng = 0
	receber0 = sys.argv[count].split('/')
	number0 = len(receber0)
	nome0 = receber0[number0-1].split('.')
	if nome0[1] != "vm":
		print("Um dos arquivos passados nao e valido, por favor insira apenas arquivos .vm")
		sys.exit()
	else:
		count = count + 1
		leng = leng + 1
		verificar = 0
		while verificar == 0:
			try:
				receber = sys.argv[count].split('/')
				number = len(receber)
				nome = receber[number-1].split('.')
				if nome[1] != "vm":
					print("Um dos arquivos passados nao e valido, por favor insira um arquivo .vm")
					sys.exit()
				else:
					count = count + 1
					leng = leng + 1
			except:
				verificar = 1
		code_nome = "./" + sys.argv[1] + ".asm"
		result = "@261\nD=A\n@0\nM=D\n@Sys.init\n0,JMP\n"
		if(leng == 1):
			result = ""
		count = count-1
		while count >= 2:
			receber = sys.argv[count].split('/')
			number = len(receber)
			nome = receber[number-1].split('.')
			arq = open(sys.argv[count])
			texto = arq.read()
			arq.close()
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
						numero = 16 + int(words[2]) + static
						code = "@" + str(numero) + "\nD=M\n"
						code = code + "@SP\nA=M\nM=D\n@SP\nM=M+1\n"
						staticount = staticount + 1
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
						numero = 16 + int(words[2]) + static
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
				elif(words[0] == 'label'):
					code = "(" + words[1] + ")\n"
					if(words[1] == "Sys.init"):
						result = "@Sys.init\n0,JMP\n" + result
				elif(words[0] == 'goto'):
					code = "@" + words[1] + "\n0,JMP\n"
				elif(words[0] == 'if-goto'):
					code = "@SP\nA=M-1\nD=M\n@SP\nM=M-1\n@" + words[1] + "\nD,JNE\n"
				elif(words[0] == 'function'):
					code = "(" + words[1] + ")\n"
					guardar = int(words[2])
					while guardar > 0:
						code = code + "D=0\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
						guardar = guardar-1
				elif(words[0] == 'return'):
					code = "@LCL\nD=M\n@R13\nM=D\n"
					code = code + "@R13\nD=M\n@5\nD=D-A\nA=D\nD=M\n@R14\nM=D\n"
					code = code + "@SP\nA=M-1\nD=M\n@ARG\nA=M\nM=D\n@ARG\nD=M\n@SP\nM=D+1\n"
					code = code + "@R13\nD=M\n@1\nD=D-A\nA=D\nD=M\n@THAT\nM=D\n"
					code = code + "@R13\nD=M\n@2\nD=D-A\nA=D\nD=M\n@THIS\nM=D\n"
					code = code + "@R13\nD=M\n@3\nD=D-A\nA=D\nD=M\n@ARG\nM=D\n"
					code = code + "@R13\nD=M\n@4\nD=D-A\nA=D\nD=M\n@LCL\nM=D\n"
					code = code + "@R14\nA=M\n0;JMP\n"
					static = staticount
				elif(words[0] == 'call'):
					name = "Return" + words[1] + str(argumentos)
					argumentos = argumentos + 1
					code = "@" + name + "\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
					code = code + "@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
					code = code + "@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
					code = code + "@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
					code = code + "@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
					code = code + "@SP\nD=M\n@LCL\nM=D\n"
					baseSP = 5 + int(words[2])
					code = code + "@" + str(baseSP) + "\nD=D-A\n@ARG\nM=D\n"
					code = code + "@" + words[1] + "\n0;JMP\n"
					code = code + "(" + name + ")\n"
				result = result + code
				i = i+1
			count = count-1
		result = result + "(END2)\n@END2\n0,JMP"
		try:
			arquivo = open(code_nome, 'r+')
			arquivo.writelines(result)
			mensagemsucesso = "Arquivo " + sys.argv[1] + ".asm atualizado com sucesso!"
			print(mensagemsucesso)
		except:
    			arquivo = open(code_nome, 'w+')
			arquivo.writelines(result)
			mensagemsucesso = "Arquivo " + sys.argv[1] + ".asm criado com sucesso!"
			print(mensagemsucesso)
		arquivo.close()
except IndexError:
	print("Adicione um arquivo .vm")
