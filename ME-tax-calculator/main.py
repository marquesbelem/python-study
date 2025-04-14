from print_color import print

print("\n")
print("Vamos calcular o valor de imposto de ME a ser pago!", color='green', format='underline', background='grey')
print(f"Como funciona: \n \t Sem pró-labore: O faturamento é tributado no Anexo III (15,5%), resultando em um imposto maior. \n \t Com pró-labore: Parte do faturamento é convertida em salário (pró-labore), reduzindo a base de cálculo do Simples Nacional e permitindo o enquadramento no Anexo V (6%).", color="yellow")
print("\nPara começar digite o valor do faturamento mensal:", color='blue')

monthly_billing = input("R$")
monthly_billing = float(monthly_billing.replace(",", "."))

print("\nCálculo para Enquadrar no Anexo V (6%): \n\t O Anexo V é destinado a serviços, e para que sua empresa se enquadre nele, o pró-labore deve ser suficiente para reduzir a Receita Bruta (RBT12) dentro dos limites do anexo.", color="yellow")
annual_billing = float(monthly_billing) * 12
print(f"\nPara faturamento mensal de R${monthly_billing:.2f}, o seu faturamento anual é de R${annual_billing:.2f}", color='magenta', format='bold')

if annual_billing > 180000:
    print("\tO faturamento anual ultrapassa o limite de R$180.000,00 para o Anexo V.", color='red', format='bold')
else:
    print("\tO faturamento anual está dentro do limite de R$180.000,00 para o Anexo V.", color='green', format='bold')

print("\n ✅ Pró-Labore Mínimo Sugerido = 28% a 35% do Faturamento Bruto", color='yellow', format='bold')
min_prolabore = monthly_billing * 0.28
max_prolabore = monthly_billing * 0.35
print(f"\tMínimo Sugerido: R${min_prolabore:.2f} a R${max_prolabore:.2f}", color='magenta', format='bold')

print("\n Total de impostos a pagar:", color='green', format='underline', background='grey')
print("\t1. Sem pró-labore (Anexo III - 15,5%):", color='yellow', format='bold')
tax_without_prolabore = monthly_billing * 0.155
print(f"\t\tSimples(15,5%): R${tax_without_prolabore:.2f}", color='red', format='bold')

print("\t2. Com pró-labore (Anexo V - 6%):", color='yellow', format='bold')
print(f"\t\t Mínimo Sugerido: R${min_prolabore:.2f}",color='magenta', format='bold')
tax_with_prolabore = monthly_billing * 0.06	
inss = min_prolabore * 0.11
total_tax_with_prolabore = tax_with_prolabore + inss
print(f"\t\t\tSimples(6%): R${tax_with_prolabore:.2f}", color='green', format='bold')
print(f"\t\t\tINSS(11%): R${inss:.2f}", color='green', format='bold')
print(f"\t\t\tTotal: R${total_tax_with_prolabore:.2f}", color='green', format='bold')

print(f"\t\t Maxuimo Sugerido: R${max_prolabore:.2f}",color='magenta', format='bold')
inss = max_prolabore * 0.11
total_tax_with_prolabore = tax_with_prolabore + inss
print(f"\t\t\tSimples(6%): R${tax_with_prolabore:.2f}", color='green', format='bold')
print(f"\t\t\tINSS(11%): R${inss:.2f}", color='green', format='bold')
print(f"\t\t\tTotal: R${total_tax_with_prolabore:.2f}", color='green', format='bold')
input('Aperte a tecla Enter para sair ...')