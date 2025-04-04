# Semana 1: Python Básico + Projeto de Automação

## Projeto: Organizador de Arquivos
**Objetivo:**
Escaneia uma pasta (ex: Downloads).
Identifica a extensão dos arquivos (.pdf, .jpg, etc.).
Move cada arquivo para uma pasta correspondente (ex: Documents, Images).
Registra as alterações em um arquivo .log.

### Bibliotecas usada
*os:* Interage com o sistema operacional (pastas, caminhos).
*shutil:* Move/copia arquivos.
*datetime:* Registra data/hora no log.

<hr>

## Anotações importantes

Diferença entre **import** vs **from**

Forma 1: **import biblioteca**
usado para acessar qualquer função/objeto da biblioteca, é preciso escrever o nome da biblioteca antes. 

Forma 2: **from biblioteca import objeto**
usado para importar apenas um objeto especifico

<hr>

**with open()** 
É usado para manipular arquivos e garante que o arquivo será fechado automaticametne após o uso, mesmo que ocorra um erro. 

with open(caminho_arquivo, modo) as arquivo:
    # Operações com o arquivo (leitura/escrita)
    arquivo.write("Texto")

*caminho_arquivo:* Caminho do arquivo (gerado por os.path.join).
*modo:* Define como o arquivo será aberto (no caso, "a" para append).
*arquivo:* Variável que representa o arquivo aberto.

Modos de Abertura de Arquivo
"a"	Append	Adiciona conteúdo ao final do arquivo. Se o arquivo não existe, ele é criado.
"w"	Write	Sobrescreve o arquivo se ele existir. Cria um novo se não existir.
"r"	Read	Abre apenas para leitura (não permite escrita).

**Por Que Usar with?**
Segurança:
O with garante que o arquivo será fechado após o bloco, mesmo se ocorrer um erro.
Sem o with, você precisaria chamar log_file.close() manualmente.

Legibilidade:
O código fica mais organizado, e o escopo do arquivo é claramente delimitado.