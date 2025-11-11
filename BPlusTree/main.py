"""
Author: Kauan Perdigão

Desenvolvido com ajuda de LLM (copilot)
"""

from BPlusTree import BPlusTree
import sys


def print_help():
    print("\nComandos disponíveis:")
    print("  insert <key> <value>  - Inserir par chave-valor")
    print("  remove <key>          - Remover chave")
    print("  search <key>          - Buscar valor por chave")
    print("  display               - Mostrar estrutura da árvore")
    print("  help                  - Mostrar este menu")
    print("  exit                  - Sair do programa")


def _display(tree: BPlusTree):
    level = [tree.root]
    depth = 0
    print("\nB+ Tree structure:")
    while level:
        print(f"Level {depth}:", end=" ")
        next_level = []
        for node in level:
            if node.is_leaf:
                print(f"Leaf(keys={node.keys})", end=" ")
            else:
                print(f"Node(keys={node.keys})", end=" ")
                next_level.extend(node.children)
        print("")
        level = next_level
        depth += 1


def main():
    while True:
        try:
            order = int(input("Order (min 3): "))
            if order < 3:
                print("Erro: order deve ser >= 3")
                continue
            break
        except ValueError:
            print("Erro: digite um número válido")
        except (EOFError, KeyboardInterrupt):
            print("\nSaindo...")
            sys.exit(0)

    tree = BPlusTree(order=order)
    print(f"B+ Tree criada (order={order})\n")
    print_help()

    while True:
        try:
            command = input("\n> ").strip()
            if not command:
                continue
            parts = command.split()
            cmd = parts[0].lower()

            if cmd == "insert":
                if len(parts) != 3:
                    print("Uso: insert <key> <value>")
                    continue
                try:
                    key = int(parts[1])
                    value = int(parts[2])
                    tree.insert(key, value)
                    print(f"Inserido: ({key}, {value})")
                except ValueError:
                    print("Erro: key e value devem ser inteiros")

            elif cmd == "remove":
                if len(parts) != 2:
                    print("Uso: remove <key>")
                    continue
                try:
                    key = int(parts[1])
                    result = tree.remove(key)
                    if result:
                        print(f"Removido: {key}")
                    else:
                        print(f"Chave {key} não encontrada")
                except ValueError:
                    print("Erro: key deve ser inteiro")

            elif cmd == "search":
                if len(parts) != 2:
                    print("Uso: search <key>")
                    continue
                try:
                    key = int(parts[1])
                    result = tree.search(key)
                    if result is not None:
                        print(f"Encontrado: {key} -> {result}")
                    else:
                        print(f"Chave {key} não encontrada")
                except ValueError:
                    print("Erro: key deve ser inteiro")

            elif cmd == "display":
                _display(tree)

            elif cmd == "help":
                print_help()

            elif cmd in ("exit", "quit"):
                print("Saindo...")
                break

            else:
                print(f"Comando desconhecido: {cmd}")
                print("Digite 'help' para ver os comandos disponíveis")

        except (EOFError, KeyboardInterrupt):
            print("\nSaindo...")
            break
        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
