"""
Blackout PDF

Versão: 0.1
Status: Em desenvolvimento

Projeto offline para sanitização de PDFs.

Todo o processamento acontece localmente.
Nenhum arquivo é enviado para a internet.
"""

import tkinter as tk
from tkinter import filedialog, messagebox

import fitz  # PyMuPDF


def abrir_pdf():
    arquivo = filedialog.askopenfilename(
        title="Selecione um PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )

    if not arquivo:
        return

    try:
        documento = fitz.open(arquivo)

        paginas = documento.page_count

        documento.close()

        messagebox.showinfo(
            "Sucesso",
            f"PDF carregado com sucesso!\n\n"
            f"Páginas: {paginas}"
        )

    except Exception as erro:
        messagebox.showerror(
            "Erro",
            str(erro)
        )


janela = tk.Tk()
janela.title("Blackout PDF")
janela.geometry("420x180")
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="Blackout PDF",
    font=("Arial", 16, "bold")
)

titulo.pack(pady=20)

botao = tk.Button(
    janela,
    text="Selecionar PDF",
    width=20,
    command=abrir_pdf
)

botao.pack()

janela.mainloop()
