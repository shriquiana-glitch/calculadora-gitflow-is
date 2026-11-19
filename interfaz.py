"""Interfaz gráfica de la calculadora, construida con Tkinter."""

import tkinter as tk
from tkinter import messagebox, ttk


OPCIONES_OPERACION = {
    "Suma (+)": "+",
    "Resta (-)": "-",
    "Multiplicación (*)": "*",
    "División (/)": "/",
    "Potencia (**)": "**",
    "Raíz cuadrada": "raiz",
}


def iniciar_interfaz(calcular, agregar, listar, limpiar):
    """Abre la calculadora y conecta sus botones con las funciones recibidas."""
    ventana = tk.Tk()
    ventana.title("Calculadora")
    ventana.geometry("420x660")
    ventana.minsize(360, 600)
    ventana.configure(background="#f1f5f9")

    estilo = ttk.Style(ventana)
    if "clam" in estilo.theme_names():
        estilo.theme_use("clam")

    estilo.configure("Fondo.TFrame", background="#f1f5f9")
    estilo.configure("Tarjeta.TFrame", background="#ffffff", padding=20)
    estilo.configure(
        "Titulo.TLabel",
        background="#f1f5f9",
        foreground="#0f172a",
        font=("Helvetica", 22, "bold"),
    )
    estilo.configure(
        "Subtitulo.TLabel",
        background="#f1f5f9",
        foreground="#475569",
        font=("Helvetica", 11),
    )
    estilo.configure(
        "Resultado.TLabel",
        background="#ffffff",
        foreground="#1d4ed8",
        font=("Helvetica", 24, "bold"),
    )
    estilo.configure("TButton", padding=(12, 8), font=("Helvetica", 11))
    estilo.configure(
        "Principal.TButton",
        padding=(12, 10),
        background="#2563eb",
        foreground="#ffffff",
        font=("Helvetica", 11, "bold"),
        borderwidth=0,
    )
    estilo.map(
        "Principal.TButton",
        background=[("active", "#1d4ed8"), ("pressed", "#1e40af")],
    )
    estilo.configure("TLabel", font=("Helvetica", 11))
    estilo.configure("TEntry", padding=8)
    estilo.configure("TCombobox", padding=6)

    contenedor = ttk.Frame(ventana, style="Fondo.TFrame", padding=20)
    contenedor.pack(fill="both", expand=True)

    ttk.Label(
        contenedor, text="Calculadora", style="Titulo.TLabel"
    ).pack(anchor="w")
    ttk.Label(
        contenedor,
        text="Realiza operaciones de forma sencilla.",
        style="Subtitulo.TLabel",
    ).pack(anchor="w", pady=(4, 16))

    tarjeta_calculo = ttk.Frame(contenedor, style="Tarjeta.TFrame")
    tarjeta_calculo.pack(fill="x")
    tarjeta_calculo.columnconfigure(0, weight=1)

    ttk.Label(tarjeta_calculo, text="Primer número").grid(
        row=0, column=0, sticky="w", pady=(0, 5)
    )
    entrada_a = ttk.Entry(tarjeta_calculo)
    entrada_a.grid(row=1, column=0, sticky="ew", pady=(0, 14))

    ttk.Label(tarjeta_calculo, text="Operación").grid(
        row=2, column=0, sticky="w", pady=(0, 5)
    )
    operacion_var = tk.StringVar(value="Suma (+)")
    selector_operacion = ttk.Combobox(
        tarjeta_calculo,
        textvariable=operacion_var,
        values=tuple(OPCIONES_OPERACION),
        state="readonly",
    )
    selector_operacion.grid(row=3, column=0, sticky="ew", pady=(0, 14))

    etiqueta_b = ttk.Label(tarjeta_calculo, text="Segundo número")
    etiqueta_b.grid(row=4, column=0, sticky="w", pady=(0, 5))
    entrada_b = ttk.Entry(tarjeta_calculo)
    entrada_b.grid(row=5, column=0, sticky="ew")

    resultado_var = tk.StringVar(value="—")
    ttk.Label(tarjeta_calculo, text="Resultado").grid(
        row=6, column=0, sticky="w", pady=(18, 4)
    )
    ttk.Label(
        tarjeta_calculo,
        textvariable=resultado_var,
        style="Resultado.TLabel",
    ).grid(row=7, column=0, sticky="w")

    historial = []
    tarjeta_historial = ttk.Frame(contenedor, style="Tarjeta.TFrame")
    tarjeta_historial.pack(fill="both", expand=True, pady=(14, 0))
    tarjeta_historial.columnconfigure(0, weight=1)
    tarjeta_historial.rowconfigure(1, weight=1)

    encabezado_historial = ttk.Frame(tarjeta_historial)
    encabezado_historial.grid(row=0, column=0, sticky="ew", pady=(0, 8))
    encabezado_historial.columnconfigure(0, weight=1)
    ttk.Label(
        encabezado_historial, text="Historial", font=("Helvetica", 14, "bold")
    ).grid(row=0, column=0, sticky="w")

    lista_historial = tk.Listbox(
        tarjeta_historial,
        height=5,
        activestyle="none",
        relief="flat",
        highlightthickness=0,
        font=("Helvetica", 11),
        background="#f8fafc",
        foreground="#1e293b",
    )
    lista_historial.grid(row=1, column=0, sticky="nsew")
    barra_historial = ttk.Scrollbar(
        tarjeta_historial, orient="vertical", command=lista_historial.yview
    )
    barra_historial.grid(row=1, column=1, sticky="ns")
    lista_historial.configure(yscrollcommand=barra_historial.set)

    def actualizar_historial():
        lista_historial.delete(0, tk.END)
        operaciones = listar(historial)
        if operaciones:
            for operacion in operaciones:
                lista_historial.insert(tk.END, operacion)
        else:
            lista_historial.insert(tk.END, "Aún no hay operaciones.")

    def mostrar_error(mensaje):
        messagebox.showerror("No se pudo calcular", mensaje, parent=ventana)

    def calcular_resultado():
        texto_a = entrada_a.get().strip()
        if not texto_a:
            mostrar_error("Escribe el primer número.")
            entrada_a.focus_set()
            return
        try:
            numero_a = float(texto_a)
        except ValueError:
            mostrar_error("El primer valor debe ser un número válido.")
            entrada_a.focus_set()
            return

        identificador = OPCIONES_OPERACION.get(operacion_var.get())
        if identificador is None:
            mostrar_error("Selecciona una operación de la lista.")
            return

        numero_b = None
        if identificador != "raiz":
            texto_b = entrada_b.get().strip()
            if not texto_b:
                mostrar_error("Escribe el segundo número.")
                entrada_b.focus_set()
                return
            try:
                numero_b = float(texto_b)
            except ValueError:
                mostrar_error("El segundo valor debe ser un número válido.")
                entrada_b.focus_set()
                return

        try:
            if identificador == "raiz":
                valor = calcular(identificador, numero_a)
                expresion = f"raiz({numero_a:g}) = {valor:g}"
            else:
                valor = calcular(identificador, numero_a, numero_b)
                expresion = (
                    f"{numero_a:g} {identificador} {numero_b:g} = {valor:g}"
                )
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            resultado_var.set("—")
            mostrar_error(str(error) or "Revisa los valores y la operación.")
            return

        resultado_var.set(f"{valor:g}")
        agregar(historial, expresion)
        actualizar_historial()
        entrada_a.delete(0, tk.END)
        entrada_b.delete(0, tk.END)
        entrada_a.focus_set()

    def borrar_historial():
        limpiar(historial)
        actualizar_historial()

    def actualizar_campo_segundo(_evento=None):
        if OPCIONES_OPERACION.get(operacion_var.get()) == "raiz":
            etiqueta_b.grid_remove()
            entrada_b.grid_remove()
        else:
            etiqueta_b.grid()
            entrada_b.grid()

    selector_operacion.bind("<<ComboboxSelected>>", actualizar_campo_segundo)
    ttk.Button(
        tarjeta_calculo,
        text="Calcular",
        command=calcular_resultado,
        style="Principal.TButton",
    ).grid(row=8, column=0, sticky="ew", pady=(16, 0))
    ttk.Button(
        encabezado_historial,
        text="Borrar historial",
        command=borrar_historial,
    ).grid(row=0, column=1, sticky="e")

    actualizar_historial()
    ventana.bind("<Return>", lambda _evento: calcular_resultado())
    ventana.after(100, entrada_a.focus_set)
    ventana.mainloop()
