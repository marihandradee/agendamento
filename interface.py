import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import tarefas
import agenda


def criar_interface(janela):

    tarefas.carregar_tarefas()

    # =========================
    # CORES
    # =========================

    cor_menu = "#4A0E23"
    cor_principal = "#F7F1F3"
    cor_botao = "#7E3050"
    cor_texto = "#333333"

    # =========================
    # MENU LATERAL
    # =========================

    menu = tk.Frame(
        janela,
        bg=cor_menu,
        width=220
    )

    menu.pack(
        side="left",
        fill="y"
    )

    titulo = tk.Label(
        menu,
        text="TASKMANAGER",
        bg=cor_menu,
        fg="white",
        font=("Arial", 18, "bold")
    )

    titulo.pack(
        pady=30
    )

    botao_inicio = tk.Button(
        menu,
        text="🏠 Início",
        width=20,
        bg=cor_botao,
        fg="white",
        font=("Arial", 11),
        command=lambda: mostrar_inicio()
    )

    botao_inicio.pack(
        pady=8
    )

    botao_tarefas = tk.Button(
        menu,
        text="📋 Tarefas",
        width=20,
        bg=cor_botao,
        fg="white",
        font=("Arial", 11),
        command=lambda: mostrar_tarefas()
    )

    botao_tarefas.pack(
        pady=8
    )

    botao_agenda = tk.Button(
        menu,
        text="📅 Agenda",
        width=20,
        bg=cor_botao,
        fg="white",
        font=("Arial", 11),
        command=lambda: mostrar_agenda()
    )

    botao_agenda.pack(
        pady=8
    )

    botao_config = tk.Button(
        menu,
        text="⚙ Configurações",
        width=20,
        bg=cor_botao,
        fg="white",
        font=("Arial", 11)
    )

    botao_config.pack(
        pady=8
    )

    # =========================
    # ÁREA PRINCIPAL
    # =========================

    area_principal = tk.Frame(
        janela,
        bg=cor_principal
    )

    area_principal.pack(
        side="right",
        fill="both",
        expand=True
    )

    # =========================
    # FUNÇÃO PARA LIMPAR TELA
    # =========================

    def limpar_tela():

        for widget in area_principal.winfo_children():
            widget.destroy()

    # =========================
    # DASHBOARD
    # =========================

    def mostrar_inicio():

        limpar_tela()

        titulo = tk.Label(
            area_principal,
            text="DASHBOARD",
            bg=cor_principal,
            fg=cor_texto,
            font=("Arial", 24, "bold")
        )

        titulo.pack(
            pady=25
        )

        total, pendentes, concluidas = tarefas.contar_tarefas()

        cartoes = tk.Frame(
            area_principal,
            bg=cor_principal
        )

        cartoes.pack(
            pady=20
        )

        # CARTÃO TOTAL

        cartao_total = tk.Frame(
            cartoes,
            bg="white",
            width=180,
            height=120
        )

        cartao_total.grid(
            row=0,
            column=0,
            padx=10
        )

        tk.Label(
            cartao_total,
            text=str(total),
            bg="white",
            font=("Arial", 28, "bold")
        ).pack(
            pady=10
        )

        tk.Label(
            cartao_total,
            text="Tarefas",
            bg="white",
            font=("Arial", 12)
        ).pack()

        # CARTÃO PENDENTES

        cartao_pendente = tk.Frame(
            cartoes,
            bg="white",
            width=180,
            height=120
        )

        cartao_pendente.grid(
            row=0,
            column=1,
            padx=10
        )

        tk.Label(
            cartao_pendente,
            text=str(pendentes),
            bg="white",
            font=("Arial", 28, "bold")
        ).pack(
            pady=10
        )

        tk.Label(
            cartao_pendente,
            text="Pendentes",
            bg="white",
            font=("Arial", 12)
        ).pack()

        # CARTÃO CONCLUÍDAS

        cartao_concluido = tk.Frame(
            cartoes,
            bg="white",
            width=180,
            height=120
        )

        cartao_concluido.grid(
            row=0,
            column=2,
            padx=10
        )

        tk.Label(
            cartao_concluido,
            text=str(concluidas),
            bg="white",
            font=("Arial", 28, "bold")
        ).pack(
            pady=10
        )

        tk.Label(
            cartao_concluido,
            text="Concluídas",
            bg="white",
            font=("Arial", 12)
        ).pack()

        # PRÓXIMAS TAREFAS

        tk.Label(
            area_principal,
            text="Próximas tarefas",
            bg=cor_principal,
            font=("Arial", 16, "bold")
        ).pack(
            pady=25
        )

        for tarefa in tarefas.tarefas[:5]:

            texto = (
                tarefa["titulo"]
                + " - "
                + tarefa["prioridade"]
                + " - "
                + tarefa["status"]
            )

            tk.Label(
                area_principal,
                text=texto,
                bg=cor_principal,
                anchor="w"
            ).pack(
                padx=40,
                pady=3,
                fill="x"
            )

    # =========================
    # TELA DE TAREFAS
    # =========================

    def mostrar_tarefas():

        limpar_tela()

        titulo = tk.Label(
            area_principal,
            text="TAREFAS",
            bg=cor_principal,
            font=("Arial", 24, "bold")
        )

        titulo.pack(
            pady=15
        )

        # BOTÕES

        botoes = tk.Frame(
            area_principal,
            bg=cor_principal
        )

        botoes.pack(
            pady=5
        )

        botao_nova = tk.Button(
            botoes,
            text="+ Nova tarefa",
            command=lambda: nova_tarefa()
        )

        botao_nova.grid(
            row=0,
            column=0,
            padx=5
        )

        botao_concluir = tk.Button(
            botoes,
            text="✓ Concluir",
            command=lambda: concluir_selecionada()
        )

        botao_concluir.grid(
            row=0,
            column=1,
            padx=5
        )

        botao_excluir = tk.Button(
            botoes,
            text="🗑 Excluir",
            command=lambda: excluir_selecionada()
        )

        botao_excluir.grid(
            row=0,
            column=2,
            padx=5
        )

        # TABELA

        tabela = ttk.Treeview(
            area_principal,
            columns=(
                "ID",
                "Tarefa",
                "Responsável",
                "Prioridade",
                "Data",
                "Horário",
                "Status"
            ),
            show="headings"
        )

        tabela.heading("ID", text="ID")
        tabela.heading("Tarefa", text="Tarefa")
        tabela.heading("Responsável", text="Responsável")
        tabela.heading("Prioridade", text="Prioridade")
        tabela.heading("Data", text="Data")
        tabela.heading("Horário", text="Horário")
        tabela.heading("Status", text="Status")

        tabela.column("ID", width=40)
        tabela.column("Tarefa", width=180)
        tabela.column("Responsável", width=120)
        tabela.column("Prioridade", width=100)
        tabela.column("Data", width=100)
        tabela.column("Horário", width=80)
        tabela.column("Status", width=100)

        tabela.pack(
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

        for tarefa in tarefas.tarefas:

            tabela.insert(
                "",
                "end",
                values=(
                    tarefa["id"],
                    tarefa["titulo"],
                    tarefa["responsavel"],
                    tarefa["prioridade"],
                    tarefa["data"],
                    tarefa["horario"],
                    tarefa["status"]
                )
            )

        def pegar_selecionada():

            selecionado = tabela.selection()

            if not selecionado:
                return -1

            item = tabela.item(selecionado[0])

            id_tarefa = item["values"][0]

            for i in range(len(tarefas.tarefas)):

                if tarefas.tarefas[i]["id"] == id_tarefa:
                    return i

            return -1

        def concluir_selecionada():

            indice = pegar_selecionada()

            if indice == -1:
                messagebox.showwarning(
                    "Atenção",
                    "Selecione uma tarefa."
                )
                return

            tarefas.concluir_tarefa(indice)

            mostrar_tarefas()

        def excluir_selecionada():

            indice = pegar_selecionada()

            if indice == -1:
                messagebox.showwarning(
                    "Atenção",
                    "Selecione uma tarefa."
                )
                return

            tarefas.excluir_tarefa(indice)

            mostrar_tarefas()

        # FUNÇÃO PARA CRIAR TAREFA

        def nova_tarefa():

            limpar_tela()

            tk.Label(
                area_principal,
                text="NOVA TAREFA",
                bg=cor_principal,
                font=("Arial", 22, "bold")
            ).pack(pady=15)

            formulario = tk.Frame(
                area_principal,
                bg=cor_principal
            )

            formulario.pack()

            # TÍTULO

            tk.Label(
                formulario,
                text="Título:",
                bg=cor_principal
            ).grid(
                row=0,
                column=0,
                sticky="w",
                pady=5
            )

            entrada_titulo = tk.Entry(
                formulario,
                width=40
            )

            entrada_titulo.grid(
                row=0,
                column=1,
                pady=5
            )

            # DESCRIÇÃO

            tk.Label(
                formulario,
                text="Descrição:",
                bg=cor_principal
            ).grid(
                row=1,
                column=0,
                sticky="nw",
                pady=5
            )

            entrada_descricao = tk.Text(
                formulario,
                width=30,
                height=4
            )

            entrada_descricao.grid(
                row=1,
                column=1,
                pady=5
            )

            # RESPONSÁVEL

            tk.Label(
                formulario,
                text="Responsável:",
                bg=cor_principal
            ).grid(
                row=2,
                column=0,
                sticky="w",
                pady=5
            )

            entrada_responsavel = tk.Entry(
                formulario,
                width=40
            )

            entrada_responsavel.grid(
                row=2,
                column=1,
                pady=5
            )

            # PRIORIDADE

            tk.Label(
                formulario,
                text="Prioridade:",
                bg=cor_principal
            ).grid(
                row=3,
                column=0,
                sticky="w",
                pady=5
            )

            entrada_prioridade = ttk.Combobox(
                formulario,
                values=["Alta", "Média", "Baixa"],
                state="readonly"
            )

            entrada_prioridade.grid(
                row=3,
                column=1,
                pady=5
            )

            entrada_prioridade.set("Média")

            # DATA

            tk.Label(
                formulario,
                text="Data:",
                bg=cor_principal
            ).grid(
                row=4,
                column=0,
                sticky="w",
                pady=5
            )

            entrada_data = tk.Entry(
                formulario,
                width=40
            )

            entrada_data.grid(
                row=4,
                column=1,
                pady=5
            )

            # HORÁRIO

            tk.Label(
                formulario,
                text="Horário:",
                bg=cor_principal
            ).grid(
                row=5,
                column=0,
                sticky="w",
                pady=5
            )

            entrada_horario = tk.Entry(
                formulario,
                width=40
            )

            entrada_horario.grid(
                row=5,
                column=1,
                pady=5
            )

            # STATUS

            tk.Label(
                formulario,
                text="Status:",
                bg=cor_principal
            ).grid(
                row=6,
                column=0,
                sticky="w",
                pady=5
            )

            entrada_status = ttk.Combobox(
                formulario,
                values=[
                    "Pendente",
                    "Em andamento",
                    "Concluída"
                ],
                state="readonly"
            )

            entrada_status.grid(
                row=6,
                column=1,
                pady=5
            )

            entrada_status.set("Pendente")

            # CHECKBUTTON

            concluida = tk.BooleanVar()

            check = tk.Checkbutton(
                formulario,
                text="Tarefa concluída",
                variable=concluida,
                bg=cor_principal
            )

            check.grid(
                row=7,
                column=1,
                pady=5
            )

            def salvar():

                status = entrada_status.get()

                if concluida.get():
                    status = "Concluída"

                resultado = tarefas.adicionar_tarefa(
                    entrada_titulo.get(),
                    entrada_descricao.get("1.0", "end").strip(),
                    entrada_responsavel.get(),
                    entrada_prioridade.get(),
                    entrada_data.get(),
                    entrada_horario.get(),
                    status
                )

                if resultado:
                    mostrar_tarefas()

            botao_salvar = tk.Button(
                formulario,
                text="SALVAR TAREFA",
                command=salvar,
                bg=cor_botao,
                fg="white"
            )

            botao_salvar.grid(
                row=8,
                column=1,
                pady=15
            )

            botao_voltar = tk.Button(
                formulario,
                text="Voltar",
                command=mostrar_tarefas
            )

            botao_voltar.grid(
                row=9,
                column=1
            )

    # =========================
    # AGENDA
    # =========================

    def mostrar_agenda():

        limpar_tela()

        tk.Label(
            area_principal,
            text="📅 AGENDA",
            bg=cor_principal,
            font=("Arial", 24, "bold")
        ).pack(
            pady=20
        )

        formulario = tk.Frame(
            area_principal,
            bg=cor_principal
        )

        formulario.pack()

        tk.Label(
            formulario,
            text="Título do compromisso:",
            bg=cor_principal
        ).grid(
            row=0,
            column=0,
            pady=5
        )

        entrada_titulo = tk.Entry(
            formulario,
            width=40
        )

        entrada_titulo.grid(
            row=0,
            column=1
        )

        tk.Label(
            formulario,
            text="Data:",
            bg=cor_principal
        ).grid(
            row=1,
            column=0,
            pady=5
        )

        entrada_data = tk.Entry(
            formulario,
            width=40
        )

        entrada_data.grid(
            row=1,
            column=1
        )

        tk.Label(
            formulario,
            text="Horário:",
            bg=cor_principal
        ).grid(
            row=2,
            column=0,
            pady=5
        )

        entrada_horario = tk.Entry(
            formulario,
            width=40
        )

        entrada_horario.grid(
            row=2,
            column=1
        )

        tk.Label(
            formulario,
            text="Local:",
            bg=cor_principal
        ).grid(
            row=3,
            column=0,
            pady=5
        )

        entrada_local = tk.Entry(
            formulario,
            width=40
        )

        entrada_local.grid(
            row=3,
            column=1
        )

        tk.Label(
            formulario,
            text="Descrição:",
            bg=cor_principal
        ).grid(
            row=4,
            column=0,
            pady=5
        )

        entrada_descricao = tk.Text(
            formulario,
            width=30,
            height=4
        )

        entrada_descricao.grid(
            row=4,
            column=1
        )

        def agendar():

            resultado = agenda.adicionar_agendamento(
                entrada_titulo.get(),
                entrada_data.get(),
                entrada_horario.get(),
                entrada_local.get(),
                entrada_descricao.get("1.0", "end").strip()
            )

            if resultado:
                mostrar_agenda()

        tk.Button(
            formulario,
            text="AGENDAR",
            command=agendar,
            bg=cor_botao,
            fg="white"
        ).grid(
            row=5,
            column=1,
            pady=15
        )

        # =========================
        # LISTA DE AGENDAMENTOS
        # =========================

        tk.Label(
            area_principal,
            text="PRÓXIMOS AGENDAMENTOS",
            bg=cor_principal,
            font=("Arial", 16, "bold")
        ).pack(
            pady=10
        )

        lista_agendamentos = tk.Listbox(
            area_principal,
            width=60,
            height=8
        )

        lista_agendamentos.pack(
            pady=10
        )

        for item in agenda.agendamentos:

            texto = (
                item["data"]
                + "   "
                + item["horario"]
                + "   "
                + item["titulo"]
            )

            lista_agendamentos.insert(
                "end",
                texto
            )

        def excluir():

            selecionado = lista_agendamentos.curselection()

            if not selecionado:
                messagebox.showwarning(
                    "Atenção",
                    "Selecione um agendamento."
                )
                return

            indice = selecionado[0]

            agenda.excluir_agendamento(indice)

            mostrar_agenda()

        tk.Button(
            area_principal,
            text="Excluir agendamento",
            command=excluir,
            bg=cor_botao,
            fg="white"
        ).pack(
            pady=10
        )

    # =========================
    # INICIAR NO DASHBOARD
    # =========================

    mostrar_inicio()