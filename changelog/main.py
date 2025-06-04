import argparse
import subprocess
from datetime import date, timedelta
import os
import sys

def obter_commits_dia_anterior(repo_path: str, autor: str) -> str:
    """
    Retorna uma string contendo o log de commits de 'autor'
    no repositório em 'repo_path' para o dia anterior (00:00 a 23:59:59).
    """

    # Verifica se o caminho existe e contém um repositório Git
    if not os.path.isdir(repo_path):
        print(f"Erro: caminho '{repo_path}' não é uma pasta válida.", file=sys.stderr)
        sys.exit(1)

    # (Opcional) verifica se existe pasta .git dentro de repo_path
    git_dir = os.path.join(repo_path, ".git")
    if not os.path.isdir(git_dir):
        print(f"Erro: '{repo_path}' não parece ser um repositório Git (faltando .git).", file=sys.stderr)
        sys.exit(1)

    # Calcula as datas de início e fim para "ontem"
    hoje = date.today()
    ontem = hoje - timedelta(days=1)

    # Formata no padrão YYYY-MM-DD
    data_str = ontem.isoformat()  # ex.: '2025-06-02'

    # Intervalo completo do dia anterior
    since = f"{data_str} 00:00:00"
    until = f"{data_str} 23:59:59"

    # Monta o comando git log
    # --author filtra pelo nome do autor
    # --since e --until definem o intervalo de datas
    # --pretty=format define o formato de saída
    cmd = [
        "git",
        "-C", repo_path,
        "log",
        f"--author={autor}",
        f"--since={since}",
        f"--until={until}",
        "--date=iso",
        "--pretty=format:%h  |  %an  |  %ad  |  %s"
    ]

    try:
        resultado = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return resultado.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Erro ao executar git log:", e.stderr, file=sys.stderr)
        sys.exit(1)

def salvar_em_arquivo(texto: str, nome_arquivo: str):
    """
    Salva o conteúdo de 'texto' em um arquivo de texto com nome 'nome_arquivo'.
    Se 'texto' estiver vazio, cria o arquivo mas avisa que não houve commits.
    """
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        if texto:
            f.write(texto + "\n")
        else:
            f.write("Nenhum commit encontrado para esse período.\n")

def montar_parser():
    parser = argparse.ArgumentParser(
        description="Extrai os commits do dia anterior de um autor específico em um repositório Git."
    )
    parser.add_argument(
        "--repo-path",
        required=True,
        help="Caminho para a pasta do repositório Git."
    )
    parser.add_argument(
        "--username",
        required=True,
        help="Nome do autor (usuário) cujos commits serão extraídos."
    )
    parser.add_argument(
        "--output",
        default=None,
        help="(Opcional) Nome do arquivo de saída. Se não informado, será 'commits_YYYY-MM-DD.txt'."
    )
    return parser

def main():
    parser = montar_parser()
    args = parser.parse_args()

    repo_path = args.repo_path
    autor = args.username

    # Obtém a data de ontem (string) para nomeação do arquivo, caso não tenha sido passado --output
    ontem = (date.today() - timedelta(days=1)).isoformat()

    #nome_arquivo = args.output if args.output else f"commits_{ontem}.txt"
    nome_arquivo = f"{args.output}_commits_{ontem}.txt"
    # Executa a extração dos commits
    log_commits = obter_commits_dia_anterior(repo_path, autor)

    # Salva em arquivo
    salvar_em_arquivo(log_commits, nome_arquivo)

    print(f"\n ✔️ Arquivo gerado: {nome_arquivo}")
    if log_commits:
        print(f"{len(log_commits.splitlines())} commit(s) encontrados e salvos.")
    else:
        print("Nenhum commit encontrado para o dia anterior.")

if __name__ == "__main__":
    main()
