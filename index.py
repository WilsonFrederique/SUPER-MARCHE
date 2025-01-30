import random
from time import strftime
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import Label, Frame, LabelFrame, W, ttk, GROOVE, StringVar, IntVar, Entry, Button, Text, BOTH, Scrollbar, VERTICAL, RIGHT, Y, messagebox, END
import tempfile, os

class SuperMarche:
    def __init__(self, root):
        self.root = root
        self.root.title("SUPER MARCHE")
        self.root.geometry("1365x1040+0+0")

        self.root.resizable(False, False)

        # Titre
        title = Label(self.root, text="SUPER MARCHE", font=("Algerian", 45), bg="#000000", fg="#fff")
        title.pack(side=tk.TOP, fill=tk.X)

        # Heure
        def heure():
            heur = strftime("%H:%M:%S")
            lblheur.config(text=heur)
            lblheur.after(1000, heure)

        lblheur = Label(self.root, text="HH:MM:SS", font=("times new roman", 15, "bold"), bg="#000000", fg="#fff")
        lblheur.place(x=0, y=25, width=120, height=45)
        heure()

        # Variables
        self.c_nom = StringVar()
        self.c_phon = StringVar()
        self.c_factu = StringVar(value=str(random.randint(1000, 9999)))
        self.c_email = StringVar()
        self.produit = StringVar()
        self.prix = IntVar()
        self.qte = IntVar()
        self.rech_factu = StringVar()
        # self.n_factu = StringVar()
        self.totalbruite = StringVar()
        self.taxe = StringVar()
        self.totalnet = StringVar()

        # Catégories et sous-catégories
        self.list_categorie = ["Selection", "Vetement", "Style de vie", "Téléphone"]
        self.sous_categories = {
            "Vetement": ["Pantelon", "T-Shirt", "Shirt"],
            "Style de vie": ["Bath Soap", "Crème", "Huile de cheveux"],
            "Téléphone": ["Iphone", "Samsung", "Huawei", "Techno"]
        }

        # Produits et prix
        self.produits_prix = {
            "Pantelon": {"Levis": 5000, "Mufty": 1000, "Skykar": 3000},
            "T-Shirt": {"Polo": 1500, "Roadster": 2550, "Jack&Jones": 3600},
            "Shirt": {"Peter England": 5900, "Louis Philipe": 6800, "Park Avenue": 9800},
            "Bath Soap": {"LiveBuy": 500, "Lux": 2400, "Santoor": 1450, "Pearl": 2100},
            "Crème": {"Fair&Lovely": 1560, "Pands": 1410, "Olay": 4530, "Garnier": 1250},
            "Huile de cheveux": {"Parachute": 2450, "Jasmin": 2300, "Bajaj": 1500},
            "Iphone": {"Iphone X": 45000, "Iphone 11": 65000, "Iphone 12": 930000},
            "Samsung": {"Samsung M16": 15600, "Samsung M12": 280000, "Samsung M21": 296000},
            "Huawei": {"Huawei Y9S": 180000, "Huawei P8": 280000, "Huawei Mate": 356000},
            "Techno": {"Techno Com11": 236000, "Techno Com12": 292000, "Techno Com13": 356000}
        }

        # Cadre principal
        Main_Frame = Frame(self.root, bd=2, relief=GROOVE, bg='white')
        Main_Frame.place(x=10, y=100, width=1345, height=630)

        # Cadre client
        client_frame = LabelFrame(Main_Frame, text="CLIENT", font=("times new roman", 15), bg="#fff")
        client_frame.place(x=10, y=5, width=350, height=150)

        Label(client_frame, text="Contact", font=("times new roman", 15, "bold"), bg="#fff").grid(row=0, column=0, sticky=W, padx=5, pady=2)
        Label(client_frame, text="Nom Client", font=("times new roman", 15, "bold"), bg="#fff").grid(row=1, column=0, sticky=W, padx=5, pady=2)
        Label(client_frame, text="Email Client", font=("times new roman", 15, "bold"), bg="#fff").grid(row=2, column=0, sticky=W, padx=5, pady=2)

        ttk.Entry(client_frame, textvariable=self.c_phon, font=("times new roman", 15)).grid(row=0, column=1, sticky=W, padx=5, pady=2)
        ttk.Entry(client_frame, textvariable=self.c_nom, font=("times new roman", 15)).grid(row=1, column=1, sticky=W, padx=5, pady=2)
        ttk.Entry(client_frame, textvariable=self.c_email, font=("times new roman", 15)).grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Cadre produit
        produit_form = LabelFrame(Main_Frame, text="PRODUIT", font=("times new roman", 15), bg="#fff")
        produit_form.place(x=380, y=5, width=540, height=150)

        Label(produit_form, text="Catégorie", font=("times new roman", 15, "bold"), bg="#fff").grid(row=0, column=0, sticky=W, padx=5, pady=2)
        Label(produit_form, text="Sous Catégorie", font=("times new roman", 15, "bold"), bg="#fff").grid(row=1, column=0, sticky=W, padx=5, pady=2)
        Label(produit_form, text="Produit", font=("times new roman", 15, "bold"), bg="#fff").grid(row=2, column=0, sticky=W, padx=5, pady=2)
        Label(produit_form, text="Prix", font=("times new roman", 15, "bold"), bg="#fff").grid(row=0, column=2, sticky=W, padx=5, pady=2)
        Label(produit_form, text="Quantité", font=("times new roman", 15, "bold"), bg="#fff").grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.txt_categorir = ttk.Combobox(produit_form, font=("times new roman", 15), values=self.list_categorie, width=13, state="readonly")
        self.txt_categorir.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.txt_categorir.current(0)
        self.txt_categorir.bind("<<ComboboxSelected>>", self.fonctionCategorie)

        self.txt_souscategorir = ttk.Combobox(produit_form, font=("times new roman", 15), values=[""], width=13, state="readonly")
        self.txt_souscategorir.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.txt_souscategorir.current(0)
        self.txt_souscategorir.bind("<<ComboboxSelected>>", self.fonctionsousCategorie)

        self.txt_nomproduit = ttk.Combobox(produit_form, font=("times new roman", 15), textvariable=self.produit, width=13, state="readonly")
        self.txt_nomproduit.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.txt_nomproduit.bind("<<ComboboxSelected>>", self.fonctionnomproduit)

        self.txt_prix = ttk.Combobox(produit_form, font=("times new roman", 15), textvariable=self.prix, width=10, state="readonly")
        self.txt_prix.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        self.txt_qte = ttk.Entry(produit_form, font=("times new roman", 15), textvariable=self.qte, width=12)
        self.txt_qte.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        # Cadre de recherche
        recher_Frame = Frame(Main_Frame, bd=2, bg="#333")
        recher_Frame.place(x=940, y=15, width=390, height=70)

        Label(recher_Frame, text="N° Facture", font=("times new roman", 15, "bold"), bg="#333", fg="#fff").grid(row=0, column=0, padx=5, pady=2)
        self.txt_recher_factu = Entry(recher_Frame, font=("times new roman", 15), width=17, textvariable=self.rech_factu)
        self.txt_recher_factu.grid(row=0, column=1, padx=5, pady=2)
        ttk.Button(recher_Frame, text="Rechercher", command=self.rechercher).grid(row=0, column=2, padx=5, pady=2)

        # Espace facture
        Facture_label = LabelFrame(Main_Frame, text="FACTURE", font=("times new roman", 15, "bold"), bg="white")
        Facture_label.place(x=940, y=80, width=390, height=400)

        scroll_y = Scrollbar(Facture_label, orient=VERTICAL)
        self.textarea = Text(Facture_label, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), bg="white", fg="blue")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)


        # Pied de page
        enbas_frame = LabelFrame(Main_Frame, text="BOUTTON", font=("times new roman", 15, "bold"), bg="#333", fg="#fff")
        enbas_frame.place(x=0, y=490, width=1350, height=140)

        self.lbl_totalbruite = Label(enbas_frame, text="Total Bruite", font=("times new roman", 17, "bold"), bg="#333", fg="#fff")
        self.lbl_totalbruite.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.lbl_taxe = Label(enbas_frame, text="Taxe", font=("times new roman", 17, "bold"), bg="#333", fg="#fff")
        self.lbl_taxe.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.lbl_totalnet = Label(enbas_frame, text="Total Net", font=("times new roman", 17, "bold"), bg="#333", fg="#fff")
        self.lbl_totalnet.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_totalbruite = ttk.Entry(enbas_frame, textvariable=self.totalbruite, font=("times new roman", 17, "bold"), width=13)
        self.txt_totalbruite.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.txt_taxe = ttk.Entry(enbas_frame, textvariable=self.taxe, font=("times new roman", 17, "bold"), width=13)
        self.txt_taxe.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.txt_totalnet = ttk.Entry(enbas_frame, textvariable=self.totalnet, font=("times new roman", 17, "bold"), width=13)
        self.txt_totalnet.grid(row=2, column=1, sticky=W, padx=5, pady=2)


        #Image
        self.imge = ImageTk.PhotoImage(Image.open("D:/2-PROJET/PYTHON/SuperMarche/images/1.jpg"))
        self.lbl_image1 = Label(image=self.imge)
        self.lbl_image1.place(x=480, y=270, width=450, height=310)

        self.imge2 = ImageTk.PhotoImage(Image.open("D:/2-PROJET/PYTHON/SuperMarche/images/2.jpg"))
        self.lbl_image2 = Label(image=self.imge2)
        self.lbl_image2.place(x=22, y=270, width=450, height=310)

        #Button
        Btn_Frame = Frame(enbas_frame, bd=2, bg="#fff")
        Btn_Frame.place(x=340, y=0)

        self.ajoutPanier = Button(Btn_Frame, text="Ajouter Card", command=self.ajouter, height=1, font=("times new roman", 19, "bold"), width=10, bg="green", cursor="hand2", fg="white")
        self.ajoutPanier.grid(row=0, column=0)

        self.generer = Button(Btn_Frame, text="Générer", command=self.genererFacture, height=1, font=("times new roman", 19, "bold"), width=10, bg="green", cursor="hand2", fg="white")
        self.generer.grid(row=0, column=1)

        self.souvegarde = Button(Btn_Frame, text="Sauvegarde", command=self.sauvegarder, height=1, font=("times new roman", 19, "bold"), width=10, bg="green", cursor="hand2", fg="white")
        self.souvegarde.grid(row=0, column=2)

        self.imprimer = Button(Btn_Frame, text="Imprimer", command=self.imprimerFacture, height=1, font=("times new roman", 19, "bold"), width=10, bg="green", cursor="hand2", fg="white")
        self.imprimer.grid(row=0, column=3)

        self.reini = Button(Btn_Frame, text="Réinisialiser", command=self.rein, height=1, font=("times new roman", 19, "bold"), width=10, bg="green", cursor="hand2", fg="white")
        self.reini.grid(row=0, column=4)

        self.quitte = Button(Btn_Frame, text="Quitter", command=self.quitter, height=1, font=("times new roman", 19, "bold"), width=10, bg="red", cursor="hand2", fg="white")
        self.quitte.grid(row=0, column=5)

        self.Bienvenu()
        self.l=[]



    # Fonctions
    def Bienvenu(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "Bienvenu Chez Super Marché Fred")
        self.textarea.insert(END, f"\n\nNuméro Facture : {self.c_factu.get()}")
        self.textarea.insert(END, f"\nNom Client : {self.c_nom.get()}")
        self.textarea.insert(END, f"\nTéléphone : {self.c_phon.get()}")
        self.textarea.insert(END, f"\nEmail : {self.c_email.get()}")

        self.textarea.insert(END, "\n************************************")
        self.textarea.insert(END, f"\nProduits\t\tQte\t\tPrix")
        self.textarea.insert(END, "\n************************************")


    def ajouter(self):
        self.n = self.prix.get()
        self.m = self.qte.get() * self.n
        self.l.append(self.n)
        if self.produit.get() == "":
            messagebox.showerror("Erreur", "Selectionner un produit")
        else:
            self.textarea.insert(END, f"\n{self.produit.get()}\t\t{self.qte.get()}\t\t{self.m}")
            self.totalbruite.set(str("Rs.%.2f"%(sum(self.l))))
            self.taxe.set(str("Rs.%.2f"%((((sum(self.l))-(self.prix.get()))*1)/100)))
            self.totalnet.set(str("Rs.%.2f"%(((sum(self.l))+((((sum(self.l))-(self.prix.get()))*1)/100)))))
    
    def sauvegarder(self):
            op = messagebox.askyesno("Sauvegarder", "Voulez-vous sauvegarder la facture")
            if op == True:
                self.donneFacture = self.textarea.get(1.0,END)
                f1 = open("D:/2-PROJET/PYTHON/SuperMarche/Facture/"+str(self.c_factu.get())+".txt","w")
                f1.write(self.donneFacture)
                messagebox.showinfo("Sauvegarder", f"La facture numéro {self.c_factu.get()} a été enregistré avec succès")
                f1.close()
                
    def genererFacture(self):
        if self.produit.get() == "":
            messagebox.showerror("Erreur", "Ajout d'abord un produit")
        else:
            text = self.textarea.get(10.0, (10.0+float(len(self.l))))
            self.Bienvenu()
            text = self.textarea.insert(END, text)
            self.textarea.insert(END, "\n************************************")
            self.textarea.insert(END, f"\nTotal Bruite : \t\t\t{self.totalbruite.get()}")
            self.textarea.insert(END, f"\nTaxe : \t\t\t{self.taxe.get()}")
            self.textarea.insert(END, f"\nTotal Net : \t\t\t{self.totalnet.get()}")

    def imprimerFacture(self):
        fichier = tempfile.mktemp(".txt")
        open(fichier, "w").write(self.textarea.get("1.0", END))
        os.startfile(fichier, "print")

    def rechercher(self):
        trouver = "non"
        for i in os.listdir("D:/2-PROJET/PYTHON/SuperMarche/Facture/"):
            if i.split(".")[0]==self.rech_factu.get():
                f1 = open(f"D:/2-PROJET/PYTHON/SuperMarche/Facture/{i}","r")
                self.textarea.delete(1.0, END)
                for d in f1:
                    self.textarea.insert(END, d)
                    f1.close
                    trouver="oui"
        if trouver == "non":
            messagebox.showerror("Erreur", "La facture n'existe pas")

    def rein(self):
        self.textarea.delete(1.0, END)
        self.c_nom.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.c_factu.set(str(x))
        self.rech_factu.set("")
        self.produit.set("")
        self.prix.set(0)
        self.qte.set(0)
        self.l.set[0]
        self.totalbruite.set("")
        self.taxe.set("")
        self.lbl_totalnet.set("")
        self.Bienvenu()

    def quitter(self):
        reponse = messagebox.askyesno("Confirmation", "Voulez-vous vraiment quitter ?")
        if reponse:
            self.root.destroy()  # Ferme la fenêtre principale

    def fonctionCategorie(self, event=None):
        cat = self.txt_categorir.get()
        self.txt_souscategorir['values'] = self.sous_categories.get(cat, [])
        self.txt_souscategorir.current(0)
        self.fonctionsousCategorie()

    def fonctionsousCategorie(self, event=None):
        sous_cat = self.txt_souscategorir.get()
        self.txt_nomproduit['values'] = list(self.produits_prix.get(sous_cat, {}).keys())
        self.txt_nomproduit.current(0)
        self.fonctionnomproduit()

    def fonctionnomproduit(self, event=None):
        produit = self.txt_nomproduit.get()
        sous_cat = self.txt_souscategorir.get()
        prix = self.produits_prix.get(sous_cat, {}).get(produit, 0)
        self.prix.set(prix)
        self.qte.set(1)  # Réinitialiser la quantité à 1

    




if __name__ == "__main__":
    root = tk.Tk()
    obj = SuperMarche(root)
    root.mainloop()