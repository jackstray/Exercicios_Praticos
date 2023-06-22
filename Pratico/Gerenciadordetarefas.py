tarefas = []

def criar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {"titulo": titulo, "descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    print("Tarefa criada com sucesso!")

def listar_tarefas():
    print("Lista de tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        concluida = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. Título: {tarefa['titulo']}, Descrição: {tarefa['descricao']}, Status: {concluida}")

def marcar_concluida():
    num_tarefa = int(input("Digite o número da tarefa a ser marcada como concluída: "))
    if 1 <= num_tarefa <= len(tarefas):
        tarefa = tarefas[num_tarefa - 1]
        tarefa["concluida"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Número de tarefa inválido.")

def excluir_tarefa():
    num_tarefa = int(input("Digite o número da tarefa a ser excluída: "))
    if 1 <= num_tarefa <= len(tarefas):
        tarefa = tarefas.pop(num_tarefa - 1)
        print(f"Tarefa '{tarefa['titulo']}' excluída com sucesso!")
    else:
        print("Número de tarefa inválido.")

while True:
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1. Criar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Excluir tarefa")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        criar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        marcar_concluida()
    elif opcao == "4":
        excluir_tarefa()
    elif opcao == "0":
        print("Saindo do gerenciador de tarefas...")
        break
    else:
        print("Opção inválida. Escolha novamente.")
