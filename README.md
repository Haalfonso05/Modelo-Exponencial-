# Modelo Exponencial por Mínimos Cuadrados

## Descripción del Proyecto

Esta aplicación implementa el método de mínimos cuadrados para ajustar modelos exponenciales del tipo **y = A·e^(B·x)** a conjuntos de datos experimentales. La aplicación cuenta con una interfaz gráfica intuitiva desarrollada en Python que permite visualizar tanto los cálculos intermedios como los resultados finales.

## Objetivos

- Implementar el método de mínimos cuadrados para modelos exponenciales
- Proporcionar una herramienta educativa para comprender la linearización de funciones exponenciales
- Visualizar el proceso completo de ajuste desde los datos originales hasta el modelo final
- Facilitar la interpretación de resultados mediante gráficas y tablas detalladas

## Fundamento Matemático

### Modelo Exponencial
```
y = A · e^(B·x)
```

### Linearización
Aplicando logaritmo natural:
```
ln(y) = ln(A) + B·x
```

Sustituyendo Y = ln(y), a₀ = ln(A), a₁ = B:
```
Y = a₀ + a₁·x
```

### Ecuaciones Normales
```
n·a₀ + a₁·Σx = ΣY
a₀·Σx + a₁·Σx² = Σ(x·Y)
```

## Instalación

### Requisitos del Sistema
- Python 3.6 o superior
- Sistema operativo: Windows, macOS, o Linux

### Paso 1: Clonar o Descargar
```bash
git clone https://github.com/Haalfonso05/Modelo-Exponencial-.git

```

### Paso 2: Instalar Dependencias
```bash

cd modelo_exponencial

pip install -r requirements.txt
```

### Paso 3: Ejecutar la Aplicación
```bash
python main.py
```

## Manual de Usuario

### Interfaz de la Aplicación

La aplicación cuenta con 4 pestañas principales:

#### 1. Ingreso de Datos
- **Número de puntos**: Selecciona cuántos pares (x,y) vas a ingresar (mínimo 2, máximo 20)
- **Generar Tabla**: Crea una tabla dinámica para ingresar los datos
- **Tabla de datos**: Ingresa los valores de X e Y en las celdas correspondientes
- **Botones de acción**:
  - `Calcular`: Procesa los datos y genera los resultados
  - `Limpiar`: Reinicia toda la aplicación

#### 2. Tabla de Cálculos
Muestra los cálculos intermedios necesarios para el método:
- **x**: Valores originales de la variable independiente
- **y**: Valores originales de la variable dependiente
- **Y = ln(y)**: Logaritmo natural de y (linearización)
- **x·Y**: Producto de x por ln(y)
- **x²**: Cuadrado de x
- **ŷi**: Valores predichos por la ecuación de la recta (a₀ + a₁·x)
- **Yi - ŷi**: Residuos en el espacio linealizado
- **(Yi - ŷi)²**: Residuos al cuadrado

**Sumas calculadas**:
- n: Número de datos
- Σx: Suma de valores x
- ΣY: Suma de ln(y)
- Σ(x·Y): Suma de productos x·ln(y)
- Σ(x²): Suma de cuadrados de x
- Σ(Yi - ŷi)²: Suma de residuos al cuadrado para el error típico de estima

#### 3. Resultados
Presenta los resultados del ajuste:

**Ecuación de la Recta Linealizada**:
```
Y = a₀ + a₁·x
```

**Modelo Exponencial Final**:
```
y = A·e^(B·x)
```

**Métricas de Calidad**:
- **Coeficiente de correlación (r)**: Calculado con r = ±√[Σ(ŷi-ȳ)²/Σ(yi-ȳ)²]
- **Error típico de estima (S_yx)**: Medida de dispersión en el espacio linealizado

**Gráfica**: Visualización de los datos originales (puntos rojos) y la curva ajustada (línea azul)

#### 4. Documentación
Contiene toda la teoría del método, interpretaciones y restricciones.

### Ejemplo Paso a Paso

#### Datos de Ejemplo
| x | y     |
|---|-------|
| 1 | 1.36  |
| 2 | 3.69  |
| 3 | 10.04 |
| 4 | 27.29 |

#### Proceso:
1. **Ingreso**: Selecciona n=4, genera tabla, ingresa los datos
2. **Cálculo**: Haz clic en "Calcular"
3. **Revisión**: Ve a "Tabla de Cálculos" para ver los valores intermedios
4. **Resultados**: Ve a "Resultados" para ver el modelo final

#### Resultados Esperados:
- **a₀ ≈ -0.6930** (intercepto de la recta)
- **a₁ ≈ 0.9998** (pendiente de la recta)
- **A ≈ 0.5001** (coeficiente exponencial)
- **B ≈ 0.9998** (exponente)
- **Modelo**: y ≈ 0.5001·e^(0.9998·x)

## Interpretación de Resultados

### Parámetros de la Recta Linealizada
- **a₀ = ln(A)**: Intercepto en el eje Y del gráfico ln(y) vs x
- **a₁ = B**: Pendiente de la recta linealizada

### Parámetros del Modelo Exponencial
- **A**: Valor de y cuando x = 0 (valor inicial)
  - A > 0: Siempre debe ser positivo para modelos exponenciales
- **B**: Tasa de crecimiento/decaimiento exponencial
  - B > 0: Crecimiento exponencial (función creciente)
  - B < 0: Decaimiento exponencial (función decreciente)
  - |B| grande: Cambio rápido en la función

### Coeficiente de Correlación (r)
- **r ≈ ±1**: Excelente correlación (>0.95 en valor absoluto)
- **r ≈ ±0.8-0.95**: Buena correlación
- **r < ±0.8**: Correlación regular, considerar otro modelo
- **Signo positivo**: Crecimiento exponencial (B > 0)
- **Signo negativo**: Decaimiento exponencial (B < 0)

### Error Típico de Estima (S_yx)
- **Valor pequeño**: Los datos están muy cerca del modelo ajustado
- **Valor grande**: Hay mucha dispersión, el modelo no ajusta bien
- **Unidades**: Mismas unidades que ln(y) (espacio linealizado)

### Interpretación Gráfica
- **Puntos rojos**: Datos experimentales originales
- **Línea azul**: Modelo exponencial ajustado
- **Proximidad**: Qué tan cerca están los puntos de la curva indica la calidad del ajuste

## Restricciones y Limitaciones

### Restricciones de Datos
- **y > 0**: Todos los valores de Y deben ser estrictamente positivos
- **n ≥ 2**: Se requieren al menos 2 puntos para el ajuste
- **Patrón exponencial**: Los datos deben seguir aproximadamente un comportamiento exponencial

### Limitaciones del Método
- **Sensibilidad a outliers**: Valores atípicos pueden afectar significativamente el ajuste
- **Transformación logarítmica**: Puede amplificar errores en valores pequeños de y
- **Validez del modelo**: El método asume que el fenómeno sigue realmente un patrón exponencial

## Solución de Problemas

### Errores Comunes

#### "Los valores de Y deben ser positivos"
- **Causa**: Algún valor de y es cero o negativo
- **Solución**: Verifica que todos los valores de y sean > 0

#### "Se requieren al menos 2 puntos"
- **Causa**: No se han ingresado suficientes datos
- **Solución**: Ingresa al menos 2 pares (x,y)

#### "Error en el cálculo"
- **Causa**: Datos inconsistentes o valores muy extremos
- **Solución**: Revisa los datos ingresados y verifica que sigan un patrón exponencial

### Consejos para Mejores Resultados
1. **Datos de calidad**: Usa datos experimentales precisos
2. **Rango adecuado**: Incluye valores en un rango representativo
3. **Verificación visual**: Revisa que la gráfica tenga sentido
4. **Validación**: Compara r y S_yx para evaluar la calidad del ajuste
5. **Análisis de residuos**: Revisa la tabla de residuos para detectar patrones

## Casos de Uso

### Aplicaciones Típicas
- **Crecimiento poblacional**: Modelar crecimiento de bacterias, poblaciones
- **Decaimiento radioactivo**: Modelar desintegración de elementos
- **Crecimiento económico**: Modelar interés compuesto, inflación
- **Procesos químicos**: Reacciones de primer orden
- **Enfriamiento**: Ley de enfriamiento de Newton

### Ejemplo: Crecimiento Bacteriano
Si tienes datos de una colonia de bacterias:
- x: tiempo (horas)
- y: número de bacterias
- El modelo y = A·e^(B·x) te dará la tasa de crecimiento B




