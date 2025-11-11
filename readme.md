# Trabalho Prático 1 – Estruturas de Indexação: Hash Extensível e Árvore B+

## Repositório dedicado ao Trabalho 1 da Disciplina de Construção de Sistemas de Gerência de Bancos de Dados do semestre 2025.2

### Dupla: Gabriel Viana Raulino e Kauan Oliveira Perdigão Lopes

## Extensible Hash

O arquivo [`ExtensibleHash.py`](ExtensibleHash/ExtensibleHash.py) possui a implementação do algoritmo Hash e tem como responsabilidade reproduzir o comportamento da estutrura, realizando inserções, remoções, busca, split e merge (quando necessário) e fornece uma visualização em texto de como os dados estão alocados (método display). Também é fornecido uma visualição em texto (semelhante a logs) das ações: em qual bucket cada valor foi inserido ou achado e quando são feito os slits e merges.

O arquivo [`demo.py`](ExtensibleHash/demo.py) é um script com vários operações pré-definidas para testar e retornar as saídas do algoritmo. Evitando retrabalho para reproduzir o fluxo de inserção, remoção e busca na estrutura.

O Arquivo [`main.py`](/ExtensibleHash/main.py) é resposável por fornecer um menu interativo via linha de comando para uma melhor dinâmica e visualização da estrutura funcionando.

- Exemplo de saída de [`demo.py`](/ExtensibleHash/demo.py)

```bash
======================================================================
TEST 1: Basic Operations (Insert and Search)
======================================================================

Inserting keys: 1, 2, 3, 4...
  → Inserido no Bucket #123875199160624 (índice 1, local_depth=1)
  → Inserido no Bucket #123875197415744 (índice 0, local_depth=1)
  → Inserido no Bucket #123875199160624 (índice 1, local_depth=1)
  → Inserido no Bucket #123875197415744 (índice 0, local_depth=1)

============================================================
Extensible Hash Structure
============================================================
Global Depth: 1
Directory Size: 2
Bucket Size: 2
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          0               123875197415744 1               {2: 200, 4: 400} *
1          1               123875199160624 1               {1: 100, 3: 300} *

============================================================
Unique Buckets: 2
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197415744)
  Local Depth: 1
  Capacity: 2/2
  Entries: {2: 200, 4: 400}
  Directory Indices: 0(0)

Bucket #1 (ID: 123875199160624)
  Local Depth: 1
  Capacity: 2/2
  Entries: {1: 100, 3: 300}
  Directory Indices: 1(1)

============================================================


Searching for keys:
  → Encontrado no Bucket #123875199160624 (índice 1, local_depth=1)
  Key 1: 100
  → Encontrado no Bucket #123875197415744 (índice 0, local_depth=1)
  Key 2: 200
  → Encontrado no Bucket #123875199160624 (índice 1, local_depth=1)
  Key 3: 300
  → Encontrado no Bucket #123875197415744 (índice 0, local_depth=1)
  Key 4: 400
  Key 5: Not found
```

Saída completa em [`outputHash`](ExtensibleHash/outputHash.md)
