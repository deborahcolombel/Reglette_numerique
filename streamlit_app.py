import tkinter as tk
from tkinter import ttk

# Fonction pour afficher un message selon les réponses
def afficher_recommandation():
    traitement = traitement_var.get()
    poids = poids_var.get()

    if traitement and poids:
        resultat_label.config(
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            foreground="white"
        )
    else:
        resultat_label.config(
            text="Veuillez répondre aux deux questions.",
            foreground="red"
        )

# Création de la fenêtre principale
root = tk.Tk()
root.title("Doser le traitement Winrevair de mon patient en 2 clics")
root.geometry("500x400")
root.configure(bg="#006647")  # Vert MSD

# Style général
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#006647", foreground="white", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TRadiobutton", background="#006647", foreground="white", font=("Helvetica", 11))

# Titre
titre_label = ttk.Label(root, text="Doser le traitement Winrevair de mon patient en 2 clics", font=("Helvetica", 16, "bold"))
titre_label.pack(pady=20)

# Question 1
ttk.Label(root, text="1) Est-ce que mon patient est en début ou milieu de traitement ?").pack(pady=5)
traitement_var = tk.StringVar()
ttk.Radiobutton(root, text="Oui", variable=traitement_var, value="oui").pack()
ttk.Radiobutton(root, text="Non", variable=traitement_var, value="non").pack()

# Question 2
ttk.Label(root, text="2) Quel est le poids de mon patient ?").pack(pady=10)
poids_var = tk.StringVar()
fourchettes = ["< 40 kg", "40 - 60 kg", "60 - 80 kg", "> 80 kg"]
for p in fourchettes:
    ttk.Radiobutton(root, text=p, variable=poids_var, value=p).pack()

# Bouton de validation
ttk.Button(root, text="Obtenir la recommandation", command=afficher_recommandation).pack(pady=20)

# Zone de résultat
resultat_label = ttk.Label(root, text="", font=("Helvetica", 12, "italic"))
resultat_label.pack(pady=10)

root.mainloop()
