import json
from tkinter import messagebox


tarefas = []


def carregar_tarefas():
    global tarefas

    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)
    except:
        tarefas = []


def salvar_arquivo():
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)


def adicionar_tarefa(titulo, descricao, responsavel, prioridade, data, horario, status):
    if titulo == "":
        messagebox.showwarning(
            "Atenção",
            "Informe o título da tarefa."
        )
        return False

    if data == "":
        messagebox.showwarning(
            "Atenção",
            "Informe a data da tarefa."
        )
        return False

    if horario == "":
        messagebox.showwarning(
            "Atenção",
            "Informe o horário da tarefa."
        )
        return False

    if prioridade == "":
        messagebox.showwarning(
            "Atenção",
            "Informe a prioridade da tarefa."
        )
        return False

    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "responsavel": responsavel,
        "prioridade": prioridade,
        "data": data,
        "horario": horario,
        "status": status
    }

    tarefas.append(nova_tarefa)

    salvar_arquivo()

    messagebox.showinfo(
        "Sucesso",
        "Tarefa cadastrada com sucesso!"
    )

    return True


def excluir_tarefa(indice):
    if indice >= 0 and indice < len(tarefas):
        tarefas.pop(indice)

        salvar_arquivo()

        messagebox.showinfo(
            "Sucesso",
            "Tarefa excluída!"
        )


def concluir_tarefa(indice):
    if indice >= 0 and indice < len(tarefas):
        tarefas[indice]["status"] = "Concluída"

        salvar_arquivo()

        messagebox.showinfo(
            "Sucesso",
            "Tarefa concluída!"
        )


def editar_tarefa(indice, titulo, descricao, responsavel, prioridade, data, horario, status):
    if indice >= 0 and indice < len(tarefas):

        if titulo == "":
            messagebox.showwarning(
                "Atenção",
                "Informe o título da tarefa."
            )
            return False

        tarefas[indice]["titulo"] = titulo
        tarefas[indice]["descricao"] = descricao
        tarefas[indice]["responsavel"] = responsavel
        tarefas[indice]["prioridade"] = prioridade
        tarefas[indice]["data"] = data
        tarefas[indice]["horario"] = horario
        tarefas[indice]["status"] = status

        salvar_arquivo()

        messagebox.showinfo(
            "Sucesso",
            "Tarefa editada com sucesso!"
        )

        return True

    return False


def contar_tarefas():
    total = len(tarefas)
    pendentes = 0
    concluidas = 0

    for tarefa in tarefas:
        if tarefa["status"] == "Concluída":
            concluidas += 1
        else:
            pendentes += 1

    return total, pendentes, concluidas