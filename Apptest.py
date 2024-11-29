import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titel der App
st.title("Graphenvisualisierung basierend auf Benutzereingaben")

# Einführung
st.write("Diese App ermöglicht es dir, Daten für `x` und `y` einzugeben und den resultierenden Graphen zu visualisieren.")

# Eingabe für x-Werte
x_input = st.text_area("Gib die Werte für x ein (kommagetrennt):", "1, 2, 3, 4, 5")
x_values = [float(i.strip()) for i in x_input.split(",")]

# Eingabe für y-Werte
y_input = st.text_area("Gib die Werte für y ein (kommagetrennt):", "2, 4, 6, 8, 10")
y_values = [float(i.strip()) for i in y_input.split(",")]

# Prüfen, ob die Länge der Eingaben übereinstimmt
if len(x_values) != len(y_values):
    st.error("Die Anzahl der Werte in `x` und `y` muss übereinstimmen.")
else:
    # DataFrame zur Übersicht
    data = pd.DataFrame({"x": x_values, "y": y_values})
    st.write("Eingegebene Daten:")
    st.dataframe(data)

    # Plot erstellen
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, marker="o", linestyle="-", color="blue", label="y = f(x)")
    ax.set_xlabel("x-Werte")
    ax.set_ylabel("y-Werte")
    ax.set_title("Visualisierung der Eingaben")
    ax.legend()

    # Graph anzeigen
    st.pyplot(fig)

    