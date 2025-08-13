import math

# montando o display estilo cartesiano na base de altura cx e cy
cy, cx = 20, 20
screen = [[" " for _ in range(cx)] for _ in range(cy)]
#  screen[x][y] = "#" <-- substituiomos o conteudo das cordenadas x e y do plano cx, cy, por "#"

def bresenham(x0, y0, x1, y1):
	# Variáveis absolutas no algoritimo de Bresenham.

	#  Iremos passar as cordenas do ponto 1, e do ponto 2 para o traçamento da linha
	# Apos isso calculamos a diferença das cordenadas 1 e 2.
	# Δy = |y1 - y0| # Cauculamos a diferença de y
	# Δx = |x1 - x0| # Cauculamos a diferença de x
	dy = abs(y1 - y0)
	dx = abs(x1 - x0)

	#  Com base no x e y repassado acrecentamos ou diminuimos mais 1 dependendo da direção da linha
	# depois de tratar a X/Y evitamos erros de logica para a adaptação em diferentes contextos e formato de linhas
	# horizontais e verticais.
	yi = 1
	if y1 < y0:
		yi = -1

	xi = 1
	if x1 < x0:
		xi = - 1

	#  Com os dados de cordenadas ja tratados, iremos passar para formula do parâmetro de tomada de decição
	# de Bresenham.

	#  Essa formula e usada para caucular o traço de erro, meio que o acumulo dele,
	# evitando numeros quebrados e nos dando um norte para a proxima tomada de desição e uma cordenada de um numero inteiro.
	# Δp = 2.Δy - Δx

	# Com esse valor em mãos nossa formula final ficaria assim
	#
	# dp+1 = { Dp += 2.(dy − dx)     se Dp > 0,
	#	 { Dp += (2 . dy)  	 Caso contrario.

	# Iremos utilizar o x como ponto de partida para a aplicação da fomula.
	result = []
	x, y = x0, y0
	if dx > dy:					        # Aplicação da formula para linhas mais horizontais
		dp = 2 * dy - dx
		for _ in range(dx + 1): 		# dp + 1 = {
			result.append((x, y)) 		# Armazenamento dos resultados das tomadas de desições
			if dp > 0:   			    # Se Pn > 0
				y += yi			          # aumentamos o Y
				dp += 2 * (dy - dx)	      # e calculamos o acumulo de erro
			else: 				        # Caso o contrario
				dp += (2 * dy)	    	  # somente calculamos o acumulo do erro.
			x += xi
		return result


	else: 						        # Para linhas menos horizontais e mais verticas
		dp = 2 * dx - dy
		for _ in range(dy + 1):         # dp + 1 = {
			result.append((x, y))       # Armazenamento dos resultados das tomadas de desições
			if dp > 0:                  # Se Pn > 0
				x += xi                   # aumentamos o X
				dp += 2 * (dx - dy)       # e calculamos o acumulo de erro
			else:                       # Caso o contrario
				dp += 2 * dx              # somente calculamos o acumulo do erro.
			y += yi
		return result


#  Chamando a função Bresenham no p1=(10,3) e no p2 = (20, 20)
# certifiquese de não ultrapassar as cordenadas do tamanho real do display

# linha =  bresenham(10, 3, 20, 20)
# print(linha)
# [(10, 3), (11, 4), (11, 5), (12, 6), (12, 7), (13, 8), (14, 9), (14, 10), (15, 11), (15, 12), (16, 13), (16, 14), (17, 15), (18, 16), (18, 17), (19, 18), (19, 19), (20, 20)]

# Iremos aplicar conteudos nessas cordenadas no display substituindo por "#"
for x, y in bresenham(10, 3, 20, 20):
	if 0 <= x < cx and 0 <= y < cy:		# Evitando que as cordenadas repassadas saiam do display
		screen[x][y] = "#" 				# <-- aplicando o conteudo nas cordenadas repassadas.

# Renderizando o conteudo display na tela.
for row in screen:
	print(" ".join(row))
