import os 
import re 
from datetime import datetime

origin_folder = "D:\TesteOrganizador"
report_path = os.path.join(origin_folder, "report.txt")

def generate_report(file_path,word_to_find):
    with open(file_path, 'r', encoding='latin-1') as file:
        text = file.read()        
        lines = text.split('\n')
        words = re.findall(r'\w+', text)
        characters = len(text)
        find_word = word_find(file_path, word_to_find)
        return {
            "file": os.path.basename(file_path),
            "lines": len(lines),
            "words": len(words),
            "characters": characters,
            "find_word": find_word
        }

def clean_file(file_path):
    with open(file_path, "r", encoding='latin-1') as file:
        lines = file.readlines()
        
    clean_lines = [line.strip() + '\n' for line in lines if line.strip()]
    
    with open(file_path, "w", encoding='utf-8') as file:
        file.writelines(clean_lines)

def process_folder(folder, word_to_find):
    data = []
    
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        
        report = generate_report(file_path, word_to_find)
        data.append(report) 
        
        clean_file(file_path)
        print(f"Processed file: {file_path}")
    
    return data

def write_report(data, report_path, word_to_find):
    with open(report_path, "w", encoding='utf-8') as report_file:
        report_file.write("Relatorio de arquivos \n")
        report_file.write(f"Gerado em: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        report_file.write("===============================================================================\n")
        report_file.write(f"Arquivo | Linhas | Palavras | Caracteres | Existe a palavra '{word_to_find}'\n")
        report_file.write("=============================================================================\n")
        report_file.write("-" * 50 + "\n")

        for item in data:
            line = f"{item['file']} | {item['lines']} | {item['words']} | {item['characters']} | {item['find_word']}\n"
            report_file.write(line)

def word_find(file_path, word):
    with open(file_path, "r", encoding='latin-1') as file:
        text = file.read().lower()
        return word.lower() in text 
    
    
if __name__ == "__main__":
    print("Iniciando o processamento dos arquivos...")
    word_to_find = "Python"
    data = process_folder(origin_folder, word_to_find)
    write_report(data, report_path, word_to_find)
    print(f"Relatório gerado em: {report_path}")