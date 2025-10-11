import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')

class AplicacionMC:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 Modelo Exponencial por Mínimos Cuadrados")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        self.configurar_estilo()
        
        self.num_datos = tk.IntVar()
        self.entries_x = []
        self.entries_y = []
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=15, padx=15, expand=True, fill='both')
        
        self.tab_datos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_datos, text="📊 Ingreso de Datos")
        
        self.tab_calculos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_calculos, text="🧮 Tabla de Cálculos")
        
        self.tab_resultados = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_resultados, text="🏆 Resultados")
        
        self.tab_docs = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_docs, text="📚 Documentación")
        
        self.configurar_interfaz_datos()
        self.configurar_interfaz_calculos()
        self.configurar_interfaz_resultados()
        self.configurar_documentacion()
    
    def configurar_estilo(self):
        style = ttk.Style()
        
        style.theme_use('clam')
        colors = {
            'bg': '#ffffff',
            'fg': '#2c3e50',
            'select_bg': '#3498db',
            'select_fg': '#ffffff',
            'button_bg': '#3498db',
            'button_fg': '#ffffff',
            'frame_bg': '#ecf0f1'
        }
        style.configure('Modern.TLabelFrame', 
                       background=colors['frame_bg'],
                       relief='flat',
                       borderwidth=1)
        
        style.configure('Modern.TButton',
                       background=colors['button_bg'],
                       foreground=colors['button_fg'],
                       borderwidth=0,
                       focuscolor='none',
                       padding=(10, 5))
        
        style.map('Modern.TButton',
                 background=[('active', '#2980b9'),
                           ('pressed', '#21618c')])
        
        style.configure('Modern.TEntry',
                       fieldbackground='white',
                       borderwidth=1,
                       relief='solid')
        
        style.configure('Modern.Treeview',
                       background='white',
                       foreground=colors['fg'],
                       rowheight=25,
                       fieldbackground='white')
        
        style.configure('Modern.Treeview.Heading',
                       background=colors['select_bg'],
                       foreground=colors['select_fg'],
                       relief='flat')
        
        style.configure('Modern.TNotebook.Tab',
                       padding=[20, 10],
                       background=colors['frame_bg'],
                       foreground=colors['fg'])
        
        style.map('Modern.TNotebook.Tab',
                 background=[('selected', colors['select_bg']),
                           ('active', '#5dade2')],
                 foreground=[('selected', colors['select_fg']),
                           ('active', colors['fg'])])
    
    def configurar_interfaz_datos(self):
        main_frame = ttk.Frame(self.tab_datos)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        frame_entrada = ttk.LabelFrame(main_frame, text="🔢 Configuración de Datos", padding=20)
        frame_entrada.pack(pady=(0, 15), fill='x')
        
        entrada_container = ttk.Frame(frame_entrada)
        entrada_container.pack(fill='x')
        
        ttk.Label(entrada_container, text="Número de puntos (n):", 
                 font=('Segoe UI', 10)).pack(side='left', padx=(0, 10))
        
        spinbox = ttk.Spinbox(entrada_container, from_=2, to=20, textvariable=self.num_datos, 
                             width=8, font=('Segoe UI', 10))
        spinbox.pack(side='left', padx=(0, 15))
        
        btn_generar = ttk.Button(entrada_container, text="✨ Generar Tabla", 
                               command=self.generar_tabla)
        btn_generar.pack(side='left', padx=(0, 10))
        
        self.frame_tabla = ttk.LabelFrame(main_frame, text="📋 Tabla de Datos", padding=20)
        self.frame_tabla.pack(pady=(0, 15), fill='both', expand=True)
        
        frame_botones = ttk.Frame(main_frame)
        frame_botones.pack(pady=10)
        
        btn_calcular = ttk.Button(frame_botones, text="🚀 Calcular Modelo", 
                                command=self.calcular)
        btn_calcular.pack(side='left', padx=(0, 15))
        
        btn_limpiar = ttk.Button(frame_botones, text="🧹 Limpiar Todo", 
                               command=self.limpiar)
        btn_limpiar.pack(side='left')
    
    def configurar_interfaz_resultados(self):
        main_frame = ttk.Frame(self.tab_resultados)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        frame_resultados = ttk.LabelFrame(main_frame, text="📊 Resultados del Ajuste", padding=15)
        frame_resultados.pack(pady=(0, 15), fill='both', expand=True)
        
        self.texto_resultados = scrolledtext.ScrolledText(frame_resultados, height=8, wrap=tk.WORD,
                                                        font=('Consolas', 10),
                                                        bg='#f8f9fa', fg='#2c3e50',
                                                        relief='flat', borderwidth=1)
        self.texto_resultados.pack(fill='both', expand=True, padx=5, pady=5)
        
        frame_grafica = ttk.LabelFrame(main_frame, text="📈 Visualización del Modelo", padding=15)
        frame_grafica.pack(fill='both', expand=True)
        
        self.figura = Figure(figsize=(10, 5), dpi=100, facecolor='white')
        self.grafica = self.figura.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figura, master=frame_grafica)
        self.canvas.get_tk_widget().pack(fill='both', expand=True, padx=5, pady=5)
    
    def configurar_interfaz_calculos(self):
        main_frame = ttk.Frame(self.tab_calculos)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        frame_tabla_calc = ttk.LabelFrame(main_frame, text="🧮 Tabla de Cálculos Intermedios", padding=15)
        frame_tabla_calc.pack(pady=(0, 15), fill='both', expand=True)
        
        self.tree_calculos = ttk.Treeview(frame_tabla_calc, columns=('x', 'y', 'Y_ln', 'xY', 'x2', 'y_pred', 'residuo', 'residuo2'), 
                                        show='headings', height=12)
        
        self.tree_calculos.heading('#1', text='x')
        self.tree_calculos.heading('#2', text='y')
        self.tree_calculos.heading('#3', text='Y = ln(y)')
        self.tree_calculos.heading('#4', text='x*Y')
        self.tree_calculos.heading('#5', text='x²')
        self.tree_calculos.heading('#6', text='ŷi = a₀+a₁x')
        self.tree_calculos.heading('#7', text='Yi - ŷi')
        self.tree_calculos.heading('#8', text='(Yi - ŷi)²')
        
        column_widths = {'x': 80, 'y': 80, 'Y_ln': 100, 'xY': 100, 'x2': 80, 'y_pred': 100, 'residuo': 100, 'residuo2': 120}
        for col in ('x', 'y', 'Y_ln', 'xY', 'x2', 'y_pred', 'residuo', 'residuo2'):
            self.tree_calculos.column(col, width=column_widths[col], anchor='center')
        
        scrollbar_calc = ttk.Scrollbar(frame_tabla_calc, orient='vertical', command=self.tree_calculos.yview)
        self.tree_calculos.configure(yscrollcommand=scrollbar_calc.set)
        
        self.tree_calculos.pack(side='left', fill='both', expand=True, padx=(5, 0), pady=5)
        scrollbar_calc.pack(side='right', fill='y', padx=(0, 5), pady=5)
        
        frame_sumas = ttk.LabelFrame(main_frame, text="📊 Sumas para Cálculos", padding=15)
        frame_sumas.pack(fill='x')
        
        self.texto_sumas = scrolledtext.ScrolledText(frame_sumas, height=6, wrap=tk.WORD,
                                                   font=('Consolas', 9),
                                                   bg='#f8f9fa', fg='#2c3e50',
                                                   relief='flat', borderwidth=1)
        self.texto_sumas.pack(fill='both', expand=True, padx=5, pady=5)
    
    def configurar_documentacion(self):
        texto_docs = """
        MÉTODO DE MÍNIMOS CUADRADOS - MODELO EXPONENCIAL
        =====================================================
        
        ENUNCIADO DEL MÉTODO:
        ----------------------
        Dado un conjunto de puntos (xᵢ, yᵢ) donde i = 1, 2, ..., n, se desea encontrar
        los parámetros A y B que mejor ajusten el modelo exponencial:
        
                            y = A · e^(B·x)
        
        mediante el método de mínimos cuadrados, minimizando la suma de los cuadrados
        de los residuos de la forma linealizada.
        
        FUNDAMENTO TEÓRICO:
        --------------------
        El modelo exponencial y = A · e^(B·x) se lineariza aplicando logaritmo natural:
        
        ln(y) = ln(A) + B·x
        
        Haciendo la sustitución Y = ln(y), a₀ = ln(A), a₁ = B, obtenemos:
        
                            Y = a₀ + a₁·x
        
        Esta es una ecuación lineal que se resuelve por mínimos cuadrados clásico.
        
        Las ecuaciones normales son:
        n·a₀ + a₁·Σx = ΣY
        a₀·Σx + a₁·Σx² = Σ(x·Y)
        
        INTERPRETACIÓN GEOMÉTRICA:
        ----------------------------
        • Los datos originales (x, y) forman una curva exponencial
        • Al transformar y → ln(y), los puntos (x, ln(y)) deben formar una línea recta
        • La pendiente de esta recta es B (parámetro exponencial)
        • El intercepto de esta recta es ln(A)
        • El ajuste lineal en el espacio transformado equivale al ajuste exponencial
          en el espacio original
        
        INTERPRETACIÓN NUMÉRICA:
        -------------------------
        • A > 0: valor inicial del modelo cuando x = 0
        • B > 0: crecimiento exponencial (función creciente)
        • B < 0: decaimiento exponencial (función decreciente)
        • |B| grande: cambio rápido en la función
        
        DATOS DE ENTRADA:
        -----------------
        • n: número de puntos de datos (n ≥ 2)
        • xᵢ: valores de la variable independiente
        • yᵢ: valores de la variable dependiente (yᵢ > 0)
        
        INFORMACIÓN DE SALIDA:
        ----------------------
        • Tabla de cálculos intermedios: x, y, Y=ln(y), x·Y, x², ŷi, Yi-ŷi, (Yi-ŷi)²
        • Sumas necesarias: Σx, ΣY, Σ(x·Y), Σx²
        • Parámetros de la recta: a₀ = ln(A), a₁ = B
        • Ecuación de la recta: Y = a₀ + a₁·x
        • Parámetros del modelo: A = e^(a₀), B = a₁
        • Modelo exponencial final: y = A · e^(B·x)
        • Coeficiente de correlación: r
        • Error típico de estima: S_yx
        • Gráfica con datos originales y curva ajustada
        
        INSTRUCCIONES DE USO:
        1. En la pestaña 'Ingreso de Datos':
           - Ingrese el número de puntos de datos que tiene.
           - Haga clic en 'Generar Tabla'.
           - Complete la tabla con los valores de X e Y.
           
        2. Haga clic en 'Calcular' para obtener los resultados.
        
        3. Los resultados incluirán:
           - Una tabla de cálculos intermedios con Y=ln(y), x*Y, x², ŷi, Yi-ŷi, (Yi-ŷi)².
           - Las sumas necesarias para resolver las ecuaciones normales.
           - Los parámetros a₀ y a₁ de la ecuación de la recta Y = a₀ + a₁·x.
           - Los parámetros 'A' y 'B' del modelo exponencial y = A*e^(B*x).
           - El coeficiente de correlación (r) con fórmula r = ±√[Σ(ŷi-ȳ)²/Σ(yi-ȳ)²].
           - El error típico de estima (S_yx) en el espacio linealizado.
           - Una gráfica con los puntos originales y la curva ajustada.
        
        4. Use el botón 'Limpiar' para reiniciar la aplicación.
        
        RESTRICCIONES:
        • Todos los valores de Y deben ser positivos (yᵢ > 0)
        • Se requieren al menos 2 puntos para el ajuste
        • Los datos deben seguir aproximadamente un patrón exponencial
        """
        
        main_frame = ttk.Frame(self.tab_docs)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        texto = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD,
                                        font=('Segoe UI', 10),
                                        bg='#f8f9fa', fg='#2c3e50',
                                        relief='flat', borderwidth=1,
                                        padx=15, pady=15)
        texto.insert(tk.INSERT, texto_docs)
        texto.config(state='disabled')
        texto.pack(fill='both', expand=True)
    
    def generar_tabla(self):
        n = self.num_datos.get()
        
        if n <= 0:
            messagebox.showerror("Error de Validación", 
                               "El número de puntos debe ser mayor que 1.\n\n"
                               "Por favor ingrese un valor válido (mínimo 2 puntos).")
            return
        
        if n == 1:
            messagebox.showwarning("Advertencia", 
                                 "Se requieren al menos 2 puntos para realizar el ajuste exponencial.\n\n"
                                 "Por favor ingrese 2 o más puntos.")
            return
        
        # Limpiar tabla existente
        for widget in self.frame_tabla.winfo_children():
            widget.destroy()
        self.entries_x = []
        self.entries_y = []
        
        header_style = {'font': ('Segoe UI', 10, 'bold'), 'foreground': '#2c3e50'}
        ttk.Label(self.frame_tabla, text="#", width=8, **header_style).grid(row=0, column=0, padx=8, pady=8)
        ttk.Label(self.frame_tabla, text="X", width=18, **header_style).grid(row=0, column=1, padx=8, pady=8)
        ttk.Label(self.frame_tabla, text="Y", width=18, **header_style).grid(row=0, column=2, padx=8, pady=8)
        
        for i in range(n):
            ttk.Label(self.frame_tabla, text=f"{i+1}", 
                     font=('Segoe UI', 9)).grid(row=i+1, column=0, padx=8, pady=4)
            
            entry_x = ttk.Entry(self.frame_tabla, width=18, font=('Segoe UI', 9))
            entry_x.grid(row=i+1, column=1, padx=8, pady=4)
            self.entries_x.append(entry_x)
            
            entry_y = ttk.Entry(self.frame_tabla, width=18, font=('Segoe UI', 9))
            entry_y.grid(row=i+1, column=2, padx=8, pady=4)
            self.entries_y.append(entry_y)
    
    def obtener_datos(self):
        try:
            x = [float(entry.get().replace(',', '.')) for entry in self.entries_x]
            y = [float(entry.get().replace(',', '.')) for entry in self.entries_y]
            return np.array(x), np.array(y)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")
            return None, None
    
    def calcular(self):
        x, y = self.obtener_datos()
        if x is None or y is None:
            return
        
        if len(x) < 2:
            messagebox.showerror("Error", "Se requieren al menos 2 puntos para el ajuste")
            return
        
        if np.any(y <= 0):
            messagebox.showerror("Error", "Los valores de Y deben ser positivos para el modelo exponencial")
            return
        
        try:
            ln_y = np.log(y)
            
            n = len(x)
            sum_x = np.sum(x)
            sum_y = np.sum(ln_y)
            sum_x2 = np.sum(x**2)
            sum_xy = np.sum(x * ln_y)
            
            A_matrix = np.array([[n, sum_x], [sum_x, sum_x2]])
            B_vector = np.array([sum_y, sum_xy])
            
            ln_A, B = np.linalg.solve(A_matrix, B_vector)
            A = np.exp(ln_A)
            
            y_prom = np.mean(y) 
            y_pred_exp = A * np.exp(B * x)  
            
            SCR = np.sum((y_pred_exp - y_prom)**2) 
            SCT = np.sum((y - y_prom)**2)  
            
            r_cuadrado = SCR / SCT if SCT != 0 else 0
            r = np.sqrt(r_cuadrado) if r_cuadrado >= 0 else 0
            
            if B < 0:
                r = -r
            
            self.mostrar_tabla_calculos(x, y, ln_y, A, B, ln_A)
            
            self.mostrar_resultados(A, B, ln_A, r, x, y)
            
            self.notebook.select(self.tab_resultados)
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error en el cálculo: {str(e)}")
    
    def mostrar_resultados(self, a, b, ln_a, r, x, y):
        self.texto_resultados.config(state='normal')
        self.texto_resultados.delete(1.0, tk.END)
        
        resultado = f"""
        RESULTADOS DEL AJUSTE EXPONENCIAL
        =================================
        
        ECUACIÓN DE LA RECTA LINEALIZADA:
        Y = a₀ + a₁·x
        Y = {ln_a:.6f} + {b:.6f}·x
        
        Parámetros de la recta:
        a₀ = ln(A) = {ln_a:.6f}
        a₁ = B = {b:.6f}
        
        MODELO EXPONENCIAL FINAL:
        y = A·e^(B·x)
        y = {a:.6f} * e^({b:.6f}*x)
        
        Parámetros del modelo exponencial:
        A = e^(a₀) = {a:.6f}
        B = a₁ = {b:.6f}
        
        Coeficiente de correlación (r) = {r:.6f}
        Error típico de estima (S_yx) = {np.sqrt(np.sum((np.log(y) - (ln_a + b * x))**2) / len(x)):.6f}
        """
        
        self.texto_resultados.insert(tk.INSERT, resultado)
        self.texto_resultados.config(state='disabled')
        
        self.graficar_resultados(a, b, x, y)
    
    def mostrar_tabla_calculos(self, x, y, ln_y, A, B, ln_A):
        for item in self.tree_calculos.get_children():
            self.tree_calculos.delete(item)
        
        x_Y = x * ln_y  
        x2 = x ** 2
        
        y_pred_ln = ln_A + B * x    
        residuos = ln_y - y_pred_ln   
        residuos2 = residuos ** 2     
        
        for i in range(len(x)):
            self.tree_calculos.insert('', 'end', values=(
                f"{x[i]:.4f}",
                f"{y[i]:.4f}",
                f"{ln_y[i]:.4f}",
                f"{x_Y[i]:.4f}",
                f"{x2[i]:.4f}",
                f"{y_pred_ln[i]:.4f}",
                f"{residuos[i]:.4f}",
                f"{residuos2[i]:.4f}"
            ))
        
        
        n = len(x)
        sum_x = np.sum(x)
        sum_y = np.sum(ln_y)
        sum_xY = np.sum(x_Y)
        sum_x2 = np.sum(x2)
        sum_residuos2_ln = np.sum(residuos2)
        y_pred_ln = ln_A + B * x
        residuos_ln = ln_y - y_pred_ln
        sum_residuos2_ln = np.sum(residuos_ln ** 2)
        s_yx = np.sqrt(sum_residuos2_ln / n)
        
        texto_sumas = f"""
SUMAS PARA EL CÁLCULO DE MÍNIMOS CUADRADOS:

n = {n}
Σx = {sum_x:.4f}
ΣY = Σln(y) = {sum_y:.4f}
Σ(x*Y) = Σ(x*ln(y)) = {sum_xY:.4f}
Σ(x²) = {sum_x2:.4f}

CÁLCULO DEL ERROR TÍPICO DE ESTIMA (en espacio linealizado):
Σ(Yi - ŷi)² = {sum_residuos2_ln:.4f}
S_yx = √(Σ(Yi - ŷi)² / n) = {s_yx:.4f}

Ecuaciones normales para Y = a₀ + a₁·x:
n·a₀ + a₁·Σx = ΣY
a₀·Σx + a₁·Σ(x²) = Σ(x·Y)

Donde:
a₀ = ln(A) (intercepto de la recta)
a₁ = B (pendiente de la recta)
        """
        
        self.texto_sumas.config(state='normal')
        self.texto_sumas.delete(1.0, tk.END)
        self.texto_sumas.insert(tk.INSERT, texto_sumas)
        self.texto_sumas.config(state='disabled')
    
    def graficar_resultados(self, a, b, x, y):
        self.grafica.clear()
        
        self.grafica.scatter(x, y, color='#e74c3c', s=80, alpha=0.8, 
                           edgecolors='white', linewidth=2, label='Datos originales', zorder=5)
        
        x_ajuste = np.linspace(min(x), max(x), 100)
        y_ajuste = a * np.exp(b * x_ajuste)
        self.grafica.plot(x_ajuste, y_ajuste, color='#3498db', linewidth=3, 
                        label=f'y = {a:.2f}e^({b:.2f}x)', alpha=0.9)
        
        self.grafica.set_xlabel('X', fontsize=12, fontweight='bold', color='#2c3e50')
        self.grafica.set_ylabel('Y', fontsize=12, fontweight='bold', color='#2c3e50')
        self.grafica.set_title('Ajuste Exponencial por Mínimos Cuadrados', 
                             fontsize=14, fontweight='bold', color='#2c3e50', pad=20)
        
        legend = self.grafica.legend(frameon=True, fancybox=True, shadow=True, 
                                   loc='upper left', fontsize=10)
        legend.get_frame().set_facecolor('#f8f9fa')
        legend.get_frame().set_alpha(0.9)
        
        self.grafica.grid(True, alpha=0.3, linestyle='--', color='#bdc3c7')
        self.grafica.set_facecolor('#fdfdfd')
        
        for spine in self.grafica.spines.values():
            spine.set_color('#bdc3c7')
            spine.set_linewidth(1)
        
        self.figura.tight_layout()
        
        self.canvas.draw()
    
    def limpiar(self):
        for widget in self.frame_tabla.winfo_children():
            widget.destroy()
        
        self.texto_resultados.config(state='normal')
        self.texto_resultados.delete(1.0, tk.END)
        self.texto_resultados.config(state='disabled')
        
        for item in self.tree_calculos.get_children():
            self.tree_calculos.delete(item)
        
        self.texto_sumas.config(state='normal')
        self.texto_sumas.delete(1.0, tk.END)
        self.texto_sumas.config(state='disabled')
        
        self.grafica.clear()
        self.canvas.draw()
        
        self.entries_x = []
        self.entries_y = []
        self.num_datos.set(0)

def main():
    root = tk.Tk()
    app = AplicacionMC(root)
    root.mainloop()

if __name__ == "__main__":
    main()
