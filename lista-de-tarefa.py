
---

# 2️⃣ Projeto: Lista de Tarefas (To-Do List)

📌 **Descrição:**  
Permite **adicionar, listar e remover tarefas**.

### `todo.py`

```python
tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa.")
        return
    
    print("\nLista de tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")

def remover_tarefa():
    listar_tarefas()
    try:
        num = int(input("Número da tarefa para remover: "))
        tarefa = tarefas.pop(num - 1)
        print(f"Tarefa '{tarefa}' removida!")
    except:
        print("Número inválido")

while True:
    print("\n=== Lista de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    op = input("Escolha: ")

    if op == "1":
        adicionar_tarefa()
    elif op == "2":
        listar_tarefas()
    elif op == "3":
        remover_tarefa()
    elif op == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida")