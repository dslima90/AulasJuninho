
# definicoes das variáveis de entrada
peso_kg = float (input ("qual o seu peso (em kg):")) # digitar o peso
altura_m = float (input ("qual a sua altura (em m):")) # digitar a altura

# calculo do quadrado da altura
quadrado_altura_m = altura_m*altura_m

# calculo do IMC pela formula
imc = peso_kg / quadrado_altura_m 

# escreve na tela o valor calculado
print("seu imc e:", imc)

#verificar se o imc é o correto

imc_max = 24.9 # imc ideal máximo

imc_min = 18.6 # imc ideal mínimo

if (imc > 24.9): # acima do peso 

	perder_peso = imc_max*quadrado_altura_m # quanto deve perder de peso
	peso_kg_emagrecer = peso_kg-perder_peso
	print("voce esta gordo! precisa emagrecer (kg):", peso_kg_emagrecer)


if (imc  < 18.6): # abaixo do peso
	
	ganhar_peso = imc_min*quadrado_altura_m # quanto deve perder de peso
	peso_kg_engordar = ganhar_peso-peso_kg
	print("voce esta magro! precisa engordar (kg):", peso_kg_engordar)


if (imc >= 18.6) and (imc <= 24.9): # peso ideal

	print("parabens! voce esta em forma!")
