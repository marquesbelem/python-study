# Semana 1: Python Básico + Projeto de Automação

### Projeto: Analisador de Arquivos de Texto
**Objetivo:**
Escaneia uma pasta e filtra apenas arquivos .txt.
Conta palavras, linhas e caracteres em cada arquivo.
Gera um relatório consolidado (em .csv ou .txt).
Modifica arquivos (ex: remove linhas vazias, padroniza espaços).

### Bibliotecas usada
*os:* Interage com o sistema operacional (pastas, caminhos).
*re:* Trabalha com expressões regulares (padrões de texto avançados).
*datetime:* Registra data/hora no log.

<hr>

## Anotações importantes

**O encoding='utf-8'**
Define a codificação de caracteres usada ao abrir o arquivo. Ele garante que:

Caracteres especiais (como ç, ã, á, ü, emojis) sejam lidos corretamente.
Evita erros como UnicodeDecodeError quando o arquivo contém textos não-ASCII.

Por que é importante?
O UTF-8 é o padrão universal para textos modernos (suporta +1 milhão de caracteres).

Sem ele, o Python pode tentar usar codificações locais (como latin-1 ou cp1252), o que pode:
Quebrar caracteres acentuados (ex: "ação" vira "a��o").
Causar erros em arquivos com símbolos especiais.

**O que significa if __name__ == "__main__":?**
É um padrão comum que verifica se o script está sendo executado diretamento (como programa principal) ou se está sendo importado como um módulo em outro script.