from tkinter import messagebox


agendamentos = []


def adicionar_agendamento(titulo, data, horario, local, descricao):

    if titulo == "":
        messagebox.showwarning(
            "Atenção",
            "Informe o título do compromisso."
        )
        return False

    if data == "":
        messagebox.showwarning(
            "Atenção",
            "Informe a data."
        )
        return False

    if horario == "":
        messagebox.showwarning(
            "Atenção",
            "Informe o horário."
        )
        return False

    novo_agendamento = {
        "titulo": titulo,
        "data": data,
        "horario": horario,
        "local": local,
        "descricao": descricao
    }

    agendamentos.append(novo_agendamento)

    messagebox.showinfo(
        "Sucesso",
        "Agendamento realizado!"
    )

    return True


def excluir_agendamento(indice):

    if indice >= 0 and indice < len(agendamentos):

        agendamentos.pop(indice)

        messagebox.showinfo(
            "Sucesso",
            "Agendamento excluído!"
        )