# Trabalho Prático 1 – Estruturas de Indexação: Hash Extensível e Árvore B+

## Repositório dedicado ao Trabalho 1 da Disciplina de Construção de Sistemas de Gerência de Bancos de Dados do semestre 2025.2

### Dupla: Gabriel Viana Raulino e Kauan Oliveira Perdigão Lopes

## BPlusTree

O diretório `BPlusTree/` contém uma implementação didática de uma Árvore B+ (B+ Tree) utilizada no trabalho. A implementação disponibiliza operações básicas e scripts auxiliares para demonstrar o comportamento da estrutura.

Arquivos principais:

- `BPlusTree/BPlusTree.py` — implementação da estrutura (`BPlusTree`), com operações: `insert`, `search`, `remove` e reequilíbrio básico.
- `BPlusTree/demo.py` — script com cenários automatizados de teste (inserções, buscas, splits, remoções e atualizações) e funções de visualização; serve como fonte para gerar saídas de exemplo em Markdown.
- `BPlusTree/main.py` — utilitário interativo (linha de comando) para criar uma árvore com uma ordem definida e executar comandos `insert`, `remove`, `search`, `display`, `help` e `exit`.
- `BPlusTree/outputBPlusTree.md` — exemplo de saída gerada pelo `demo.py` (registro humano das execuções). Nem sempre está presente — pode ser gerado executando o `demo.py`.

Como rodar o demo e gravar a saída em Markdown (exemplos):

```bash
# Linux / WSL (UTF-8 por padrão):
python3 BPlusTree/demo.py > BPlusTree/outputBPlusTree.md

# Windows PowerShell (forçar UTF-8 só para este processo):
$env:PYTHONIOENCODING = 'utf-8'; python .\BPlusTree\demo.py > .\BPlusTree\outputBPlusTree.md 2>&1
```

Exemplo de trecho de saída do `demo.py`:

```bash
======================================================================
TEST 1: Basic Operations (Insert and Search)
======================================================================

Inserting keys: 1, 2, 3, 4...
  -> Inserted (1, 100)
  -> Inserted (2, 200)
  -> Inserted (3, 300)
  -> Inserted (4, 400)

============================================================
B+ TREE STRUCTURE
============================================================

Level 0: Node(keys=[4])

Level 1: Leaf(keys=[1, 2, 3]) Leaf(keys=[4])

Leaf chain:
  Leaf #0 keys: [1, 2, 3], values: [100, 200, 300]
  Leaf #1 keys: [4], values: [400]
```

Saída completa de exemplo: `BPlusTree/outputBPlusTree.md`.
