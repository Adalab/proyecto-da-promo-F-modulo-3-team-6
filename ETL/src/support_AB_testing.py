import pandas as pd
# Evaluar linealidad de las relaciones entre las variables
# y la distribución de las variables
# ------------------------------------------------------------------------------
import scipy.stats as stats
from scipy.stats import shapiro, poisson, chisquare, expon, kstest, chi2_contingency, ttest_ind


def test_chi(df):
    # Crear una tabla de contingencia
    contingency_table = pd.crosstab(df['Attrition'], df['Groups'])

    # Ejecutar el test de chi-cuadrado
    chi2, p_valor, _, _ = chi2_contingency(contingency_table)

    # Mostrar los resultados del test
    print("\nResultados del test de Chi-cuadrado:")
    print(f"Estadística de Chi-cuadrado: {chi2}")
    print(f"P-valor: {p_valor}")

    # Interpretación del resultado
    alpha = 0.05  # Nivel de significancia
    if p_valor < alpha:
        print("\nHay evidencia suficiente para rechazar la hipótesis nula.")
    else:
        print("\nNo hay suficiente evidencia para rechazar la hipótesis nula.")
