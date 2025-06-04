import pandas as pd
import os
import pdfplumber
from print_color import print

#region Receita Bruta
def get_NF_total_value(file_name):
    file = f"receita_bruta/{file_name}"
    df = pd.read_csv(file, sep=';', encoding='latin-1')
    df.columns = df.columns.str.strip()
    values = df['Valor dos Serviços'].str.replace('.', '').str.replace(',', '.').astype(float).tolist()
    return values[-1]

def get_gross_revenue_total(): 
    folder = 'receita_bruta/' 
    content = os.listdir(folder)
    files = [arq for arq in content if os.path.isfile(os.path.join(folder, arq))]
    total = 0; 
    for arquivo in files:
        if arquivo.endswith('.csv'):
            try:
                valor = get_NF_total_value(arquivo)
                total += valor
            except Exception as e:
                print(f"Erro ao processar o arquivo {arquivo}: {e}")
    return total
#end 

#region Folha de Pagamento
def get_payroll_total_value(file_name):
    file = f"folha_pagamento/{file_name}"
    value = 0
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            value = page.extract_tables()[0][3][3]
            value = float(value.replace('Total dos vencimentos\n', '').replace('.', '').replace(',', '.'))
    return value

def get_payroll_total():
    folder = 'folha_pagamento/' 
    content = os.listdir(folder)
    files = [arq for arq in content if os.path.isfile(os.path.join(folder, arq))]
    total = 0; 
    for arquivo in files:
        if arquivo.endswith('.pdf'):
            try:
                valor = get_payroll_total_value(arquivo)
                total += valor
            except Exception as e:
                print(f"Erro ao processar o arquivo {arquivo}: {e}")
    return total
#end

def format_to_real(value):
    return f"R${value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def factor_r(gross_total,payrol_total):
    value = payrol_total / gross_total
    return value

def necessary_adjustment(gross_total,payrol_total,months): 
    X = (0.28 * gross_total) - payrol_total
    print(f"\t\tValor total a aumentar na folha: R$ {format_to_real(X)}", color='yellow', format='underline', background='grey')
    months_adjustment = X / months
    print(f"\t\tAumento mensal necessário no seu pró labore: R$ {format_to_real(months_adjustment)}", color='yellow', format='underline', background='grey')

payroll_total = get_payroll_total()
print(f"Total de folha de pagamento: {format_to_real(payroll_total)}", color='blue', format='underline', background='grey')

gross_total = get_gross_revenue_total()
print(f"Total de receita bruta: {format_to_real(gross_total)}",color='blue', format='underline', background='grey')

factor = factor_r(gross_total, payroll_total)
factor_formatted = f"{factor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
print(f"\t Fator R é {factor_formatted}% você se enquadra",color='magenta', format='underline', background='grey')
if(factor >= 0.28):
    print("\t\t Anexo III (alíquotas de 6% a 18%, dependendo do faturamento).",color='green', format='underline', background='grey')
else:
    print("\t\t Anexo V (alíquotas de 15,5% a 30,5%).",color='red', format='underline', background='grey')

necessary_adjustment(gross_total, payroll_total, 7)