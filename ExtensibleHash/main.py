"""
Author: Gabriel Viana
Desenvolvido com ajuda de LLM (copilot)
"""

from ExtensibleHash import ExtensibleHash
import sys


def print_help():
    """Display available commands."""
    print("\nComandos disponíveis:")
    print("  insert <key> <value>  - Inserir par chave-valor")
    print("  remove <key>          - Remover chave")
    print("  search <key>          - Buscar valor por chave")
    print("  display               - Mostrar estrutura do hash")
    print("  help                  - Mostrar este menu")
    print("  exit                  - Sair do programa")


def main():
    
    # Initialize hash
    while True:
        try:
            bucket_size = int(input("Bucket size: "))
            if bucket_size < 1:
                print("Erro: bucket size deve ser >= 1")
                continue
            break
        except ValueError:
            print("Erro: digite um número válido")
        except (EOFError, KeyboardInterrupt):
            print("\nSaindo...")
            sys.exit(0)
    
    eh = ExtensibleHash(bucket_size=bucket_size)
    print(f"Hash criado (bucket_size={bucket_size})\n")
    print_help()
    
    # Command loop
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
                    eh.insert(key, value)
                    print(f"Inserido: ({key}, {value})")
                except ValueError:
                    print("Erro: key e value devem ser inteiros")
            
            elif cmd == "remove":
                if len(parts) != 2:
                    print("Uso: remove <key>")
                    continue
                try:
                    key = int(parts[1])
                    result = eh.remove(key)
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
                    result = eh.search(key)
                    if result is not None:
                        print(f"Encontrado: {key} -> {result}")
                    else:
                        print(f"Chave {key} não encontrada")
                except ValueError:
                    print("Erro: key deve ser inteiro")
            
            elif cmd == "display":
                eh.display()
            
            elif cmd == "help":
                print_help()
            
            elif cmd == "exit" or cmd == "quit":
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
