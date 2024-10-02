import tkinter as tk
from tkinter import messagebox

class GelatariaChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot Gelataria")
        self.root.geometry("400x400")

        self.recipient_choice = None
        self.size_choice = None
        self.flavors_choice = []
        self.cover_choice = None

        # Preços para cada item
        self.precos_recipientes = {"Copo": 2.00, "Cone": 1.50}
        self.precos_tamanhos = {"Pequeno": 2.00, "Médio": 3.00, "Grande": 4.00}
        self.precos_coberturas = {
            "Calda de Chocolate": 1.50,
            "Granulado": 1.00,
            "Chantilly": 2.00,
            "Caramelo": 1.50,
            "Sem Cobertura": 0.00
        }

        # Mensagem inicial
        self.label = tk.Label(root, text="Bem-vindo à Gelataria!", font=("Arial", 14))
        self.label.pack(pady=20)

        # Botão para iniciar o pedido
        self.iniciar_button = tk.Button(root, text="Iniciar Pedido", command=self.escolher_recipient)
        self.iniciar_button.pack(pady=10)

    def escolher_recipient(self):
        # Limpar a tela
        self.limpar_tela()

        self.label = tk.Label(self.root, text="Escolha o tipo de recipiente:", font=("Arial", 12))
        self.label.pack(pady=20)

        # Criar variável para o recipiente
        self.recipient_var = tk.StringVar(value="Copo")

        # Radiobuttons para escolher recipiente
        for recipiente in self.precos_recipientes.keys():
            radio_button = tk.Radiobutton(self.root,
                                           text=f"{recipiente} - €{self.precos_recipientes[recipiente]:.2f}",
                                           variable=self.recipient_var,
                                           value=recipiente)
            radio_button.pack(pady=5)

        # Botão para prosseguir
        proseguir_button = tk.Button(self.root, text="Próximo", command=self.escolher_tamanho)
        proseguir_button.pack(pady=10)

    def escolher_tamanho(self):
        self.recipient_choice = self.recipient_var.get()
        self.limpar_tela()

        self.label = tk.Label(self.root, text=f"Escolha o tamanho do gelado ({self.recipient_choice}):", font=("Arial", 12))
        self.label.pack(pady=20)

        # Criar variável para o tamanho
        self.size_var = tk.StringVar(value="Pequeno")

        # Radiobuttons para escolher tamanho
        for tamanho in self.precos_tamanhos.keys():
            radio_button = tk.Radiobutton(self.root,
                                           text=f"{tamanho} - €{self.precos_tamanhos[tamanho]:.2f}",
                                           variable=self.size_var,
                                           value=tamanho)
            radio_button.pack(pady=5)

        # Botão para prosseguir
        proseguir_button = tk.Button(self.root, text="Próximo", command=self.escolher_sabores)
        proseguir_button.pack(pady=10)

    def escolher_sabores(self):
        self.size_choice = self.size_var.get()
        self.limpar_tela()

        self.label = tk.Label(self.root, text="Escolha até 3 sabores:", font=("Arial", 12))
        self.label.pack(pady=20)

        self.flavors = ["Baunilha", "Chocolate", "Morango", "Menta", "Limão", "Coco", "Doce de Leite"]
        self.flavors_vars = []

        # Criar checkboxes para os sabores
        for sabor in self.flavors:
            var = tk.IntVar()
            checkbox = tk.Checkbutton(self.root, text=sabor, variable=var)
            checkbox.pack(pady=2)
            self.flavors_vars.append((var, sabor))

        # Botão para escolher cobertura
        coberturas_button = tk.Button(self.root, text="Escolher Cobertura", command=self.escolher_cobertura)
        coberturas_button.pack(pady=20)

    def escolher_cobertura(self):
        # Verificar quais sabores foram escolhidos
        self.flavors_choice = [sabor for var, sabor in self.flavors_vars if var.get() == 1]

        if len(self.flavors_choice) == 0:  # Verificar se nenhum sabor foi escolhido
            messagebox.showerror("Erro", "Por favor, escolha pelo menos um sabor!")
            return  # Interromper a execução se nenhum sabor foi selecionado

        if len(self.flavors_choice) > 3:  # Verificar se mais de 3 sabores foram escolhidos
            messagebox.showerror("Erro", "Escolha no máximo 3 sabores!")
        else:
            self.limpar_tela()

            self.label = tk.Label(self.root, text="Escolha uma cobertura:", font=("Arial", 12))
            self.label.pack(pady=20)

            # Criar variável para a cobertura
            self.cover_var = tk.StringVar(value="Sem Cobertura")

            # Criar radiobuttons para as coberturas
            for cobertura in self.precos_coberturas.keys():
                radio_button = tk.Radiobutton(self.root,
                                               text=f"{cobertura} - €{self.precos_coberturas[cobertura]:.2f}",
                                               variable=self.cover_var,
                                               value=cobertura)
                radio_button.pack(pady=2)

            # Botão para finalizar o pedido
            finalizar_button = tk.Button(self.root, text="Finalizar Pedido", command=self.finalizar_pedido)
            finalizar_button.pack(pady=20)

    def finalizar_pedido(self):
        self.cover_choice = self.cover_var.get()

        # Calcular preço total
        preco_recipiente = self.precos_recipientes[self.recipient_choice]
        preco_tamanho = self.precos_tamanhos[self.size_choice]
        preco_cobertura = self.precos_coberturas[self.cover_choice]
        preco_total = preco_recipiente + preco_tamanho + preco_cobertura

        self.limpar_tela()

        # Resumo do pedido
        resumo = f"Recipiente: {self.recipient_choice} - €{preco_recipiente:.2f}\n"
        resumo += f"Tamanho: {self.size_choice} - €{preco_tamanho:.2f}\n"
        resumo += f"Sabores: {', '.join(self.flavors_choice)}\n"
        resumo += f"Cobertura: {self.cover_choice} - €{preco_cobertura:.2f}\n"
        resumo += f"\nPreço Total: €{preco_total:.2f}"

        self.label = tk.Label(self.root, text="Resumo do seu pedido:", font=("Arial", 14))
        self.label.pack(pady=20)

        self.resumo_label = tk.Label(self.root, text=resumo, font=("Arial", 12))
        self.resumo_label.pack(pady=20)

        # Botão para novo pedido
        novo_button = tk.Button(self.root, text="Novo Pedido", command=self.escolher_recipient)
        novo_button.pack(pady=10)

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Criar a janela principal
root = tk.Tk()
app = GelatariaChatbot(root)
root.mainloop()
