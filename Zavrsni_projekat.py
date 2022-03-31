from tkinter import *
import tkinter.messagebox
import json
import matplotlib.pyplot as plt
import numpy as np
import Student
import os, zipfile, shutil

#_____________________________________________
def provera(uneto_ime, uneto_prezime, uneti_broj, uneti_jmbg, unete_ocene, otvoren_prozor):
    
    if len(uneti_broj) != 8:
        tkinter.messagebox.showerror("Ups!","Dužina broja indeksa je pogrešna.\nPokušajte ponovo.")
        return
    elif uneti_broj[0:2].isdigit() or uneti_broj[2:].isdigit() == False:
        tkinter.messagebox.showerror("Ups!","Broj indeksa nije validan.\nPokušajte ponovo.")
        return
    elif uneti_broj[0:2].isupper() == False:
        tkinter.messagebox.showerror("Ups!","Broj indeksa mora sadržati velika slova!\nPokušajte ponovo.")
        return
    else: 
        studentski_podaci = open("Podaci_studenata.json", "r", encoding = "utf-8")
        ocitano = json.load(studentski_podaci)
        studentski_podaci.close()
    
        indeksi = ocitano.keys()
        if uneti_broj in indeksi:
            tkinter.messagebox.showerror("Ups!", "Takav broj indeksa već postoji u bazi, molimo Vas unesite drugi broj indeksa.")
            return
    
    if len(uneti_jmbg) != 13 or uneti_jmbg.isnumeric() == False:
        tkinter.messagebox.showerror("Ups!", "Uneti matični broj nije ispravan.\nMatični broj mora sadržati samo brojeve i mora ih imati 13!")
        return

    for i in unete_ocene:
        if i in ["", " "]:
            tkinter.messagebox.showerror("Ups!", "Polje ne sme biti prazno! Unesite ocene u opsegu od 6 do 10!")
            return
        else:
            m = int(i)
            if m not in range(6,11):
                tkinter.messagebox.showerror("Ups!", "Unete ocene nisu ispravne!\nOcene moraju biti u opsegu od 6 do 10.")
                return

    studentski_podaci = open("Podaci_studenata.json", "r", encoding = "utf-8")

    data = json.load(studentski_podaci)
    studentski_podaci.close()

    data[uneti_broj] = {"ime" : uneto_ime, "prezime" : uneto_prezime, "jmbg" : uneti_jmbg, "predmeti" : {"OST1" : int(unete_ocene[0]), "OST2" : int(unete_ocene[1]), "SUKN" : int(unete_ocene[2]), "OPKN": int(unete_ocene[3])}}
    
    studentski_podaci = open("Podaci_studenata.json", "w", encoding = "utf-8")
    json.dump(data, studentski_podaci, indent = 4)
    studentski_podaci.close()

    otvoren_prozor.destroy()
    otvoren_prozor.update()

    tkinter.messagebox.showinfo("Bravo!", f"Uspešno ste upisali novog studenta sa brojem indeksa {uneti_broj}")

def provera_br_indeksa():
    
    broj_indeksa = unos.get()
    poruka = ""

    if len(broj_indeksa) != 8:
        poruka = "Dužina broja indeksa je pogrešna.\nPokušajte ponovo."
    elif broj_indeksa[0:2].isdigit() or broj_indeksa[2:].isdigit() == False:
        poruka = "Broj indeksa nije validan.\nPokušajte ponovo."
    elif broj_indeksa[0:2].isupper() == False:
        poruka = "Broj indeksa mora sadržati velika slova!\nPokušajte ponovo."
    
    if poruka == "":
        novi_prozor(broj_indeksa)
    else:
         tkinter.messagebox.showerror("Ups!", poruka)
    
def izbor_studenta(x):
    
    studentski_podaci = open("Podaci_studenata.json", "r", encoding = "utf-8")
    ocitano = json.load(studentski_podaci)
    studentski_podaci.close()
    
    indeksi = ocitano.keys()

    if x not in indeksi:
        tkinter.messagebox.showerror("Ups!","Student sa unetim brojem indeksa nije u bazi podataka.\nUkoliko želite da upišete novog studenta, vratite se na početnu stranu.")
    else: 
        student = ocitano[x]
        student_1 = Student.Student(student["ime"], student["prezime"], student["jmbg"], student["predmeti"])
        return student_1    

def datum(jmbg):

    dan = jmbg[0:2].lstrip("0")
    mesec = jmbg[2:4].lstrip("0")
    godina = "1" + jmbg[4:7]
    
    datum = dan + "." + mesec + "." + godina + "."
    return datum 

def izabrani_smer(indeks):
    izabrani_smer = indeks[0:2]
    if izabrani_smer == "TS":
        return "Telekomunikacioni saobraćaj i mreže."
    elif izabrani_smer == "VD":
        return "Vodni saobraćaj i transport."
    elif izabrani_smer == "ZE":
        return "Železnički saobraćaj i transport."

def godinaUpisa(indeks):
    
    godinaUpisa = "20" + indeks[2:4]

    return godinaUpisa

def cuvanje(br_indeksa):

    if os.path.exists(f"{br_indeksa}.txt") == False:
        datoteka = open(f"{br_indeksa}.txt", "w", encoding = "utf-8")
    else:
        tkinter.messagebox.showinfo("Obaveštenje!",f"Fajl {br_indeksa}.txt već postoji!")
        return

    datoteka.write(f"Ime i prezime studenta: {izabrani_student.ime} {izabrani_student.prezime}\nDatum rođenja: {datum(izabrani_student.jmbg)}\nSmer: {izabrani_smer(br_indeksa)}\nGodiina upisa:{godinaUpisa(br_indeksa)}\nSpisak predmeta i ocene: {izabrani_student.predmeti.items()}""")
    
    datoteka.close()

def zipovanje_fajla():

    lokacija_datoteka = "C:\\Users\\Sonja\\Desktop\\Procoding\\Napredni nivo\\Završni projekat"
    fajlovi = os.listdir(lokacija_datoteka)

    if os.path.exists("Zipovanje") == False:
        os.makedirs("Zipovanje")
    else:
        tkinter.messagebox.showinfo("Obaveštenje!","Direktorijum već postoji!")
        return
    
    for i in fajlovi:
        if i != "__pycache__":
            shutil.copy(lokacija_datoteka + "\\" + i,".\\Zipovanje\\" + i)
    
    novi_fajlovi = os.listdir(".\\Zipovanje")

    fajl = zipfile.ZipFile(".\\Zipovanje.zip","w")

    for k in novi_fajlovi:
        fajl.write(".\\Zipovanje\\" + k, compress_type = zipfile.ZIP_DEFLATED)
    fajl.close()

    shutil.rmtree(".\\Zipovanje")

def grafikon():
    recnik = izabrani_student.predmeti

    ocene = recnik.values()
    novi_recnik = {6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0}

    for j in ocene:
        if j in novi_recnik.keys():
            novi_recnik[j] += 1

    x = novi_recnik.keys()
    y = novi_recnik.values()
    
    plt.clf()
    plt.bar(x,y)
    plt.title("Odnos ocena")
    plt.show()
    plt.grid()
    plt.savefig("grafik.jpg")
                
def novi_prozor(x):
    global izabrani_student
    izabrani_student = izbor_studenta(x)
    if izabrani_student == None:
        return

    prozor = Toplevel(root)
    prozor.title("Studentski dosije")

    # Naslov
    opis = Label(prozor, text = x, font = ('Helvetica', 12, 'bold'), fg = "#0E063D",bg = "#DDF2E8")
    opis.grid(row = 0, columnspan = 4)
    
    # Ime i Prezime
    ime_i_prezime = Label(prozor, text = "Ime i prezime studenta:", font = ("Helvetica", 10, "bold"),bg = "#DDF2E8", fg = "#0E063D")
    ime_i_prezime.grid(row = 1, column = 1,padx = 10, pady = 10)

    ip = Label(prozor, text = izabrani_student.ime + " " + izabrani_student.prezime, font = ("Helvetica", 10),bg = "#DDF2E8", fg = "#0E063D")
    ip.grid(row = 1, column = 2, columnspan = 2)

    # Matični broj
    datum_rodjenja = Label(prozor, text = "Datum rođenja:", font = ("Helvetica",10, "bold"),bg = "#DDF2E8", fg = "#0E063D")
    datum_rodjenja.grid(row = 2, column = 1, pady = 10)
    
    dr = Label(prozor, text = datum(izabrani_student.jmbg), font=("Helvatica", 10),bg = "#DDF2E8", fg = "#0E063D")
    dr.grid(row = 2, column = 2, columnspan = 2)

    # Smer
    smer = Label(prozor, text = "Smer: ", font = ("Helvetica", 10, "bold"),bg = "#DDF2E8", fg = "#0E063D")
    smer.grid(row = 3, column = 1, pady = 10)

    izs = Label(prozor, text = izabrani_smer(x), font = ("Helvetica", 10),bg = "#DDF2E8", fg = "#0E063D")
    izs.grid(row = 3, column = 2, columnspan = 2)

    #Godina upisa
    godina_upisa = Label(prozor, text = "Godina upisa:", font = ("Helvetica", 10, "bold"),bg = "#DDF2E8", fg = "#0E063D")
    godina_upisa.grid(row = 4, column = 1, pady = 10)

    gup = Label(prozor, text = godinaUpisa(x), font = ("Helvetica", 10),bg = "#DDF2E8", fg = "#0E063D")
    gup.grid(row = 4, column = 2, columnspan = 2)

    #Spisak predmeta
    spisak = Label(prozor, text = "Spisak predmeta",font = ("Helvetica", 10, "bold"),bg = "#DDF2E8", fg = "#0E063D")   
    spisak.grid(row = 5, column = 1, pady = 10)

    predmeti = izabrani_student.predmeti
    brojac = 1
    br = 6
    a = 0
    for i in predmeti.keys():
        labela1 = Label(prozor, text = str(brojac) + "." + " " + i, font = ("Helvetica", 10),bg = "#DDF2E8", fg = "#0E063D")
        labela1.grid(row = br, column  = 1)
        labela2 = Label(prozor, text = predmeti[i], font = ("Helvetica", 10), bg = "#DDF2E8", fg = "#0E063D")
        labela2.grid(row = br, column  = 2)
        a += int(predmeti[i])
        br +=1
        brojac +=1
    pros_a = a/(brojac-1)

    #Ocene 
    ocene = Label(prozor, text = "Ocene", font = ("Helvetica", 10, "bold"),bg = "#DDF2E8", fg = "#0E063D")
    ocene.grid(row = 5, column = 2, padx = 30)

    # Prosek
    prosek = Label(prozor, text = "Prosečna ocena", font = ("Helvetica", 10, "bold"),bg = "#DDF2E8", fg = "#0E063D")
    prosek.grid(row = 5, column = 3, padx = 30) 

    prosecna = Label(prozor, text = pros_a, font = ("Helvetica", 10, "bold"),bg = "#DDF2E8", fg = "#0E063D")
    prosecna.grid(row = 8, column = 3)

    # Dugme u txt
    tekst = Button(prozor, text = "Sačuvaj", font = ("Helvetica", 10, "bold"),bg = "#F4F589", fg = "#0E063D", command = lambda:cuvanje(x))
    tekst.grid(row = 10, column = 1, pady = 20)

    # Dugme u zip
    zipovanje = Button(prozor, text = "ZIP file", font = ("Helvetica", 10, "bold"),bg = "#F4F589", fg = "#0E063D", command = zipovanje_fajla)
    zipovanje.grid(row = 10, column = 2, pady = 20)

    # Dugme za grafik
    grafik = Button(prozor, text = "Grafički prikaz", font = ("Helvetica", 10, "bold"),bg = "#F4F589", fg = "#0E063D", command = grafikon)
    grafik.grid(row = 10, column = 3, pady = 20)

    prozor.geometry("475x455")
    prozor.configure(bg = "#DDF2E8")
    prozor.resizable(False,False)

def o_programu():
    tkinter.messagebox.showinfo("O programu:", "Završni projekat\nPython programiranje - Procoding centar\nRadila: Sonja Jović")

def upis():
    prozor2 = Toplevel(root)
    prozor2.title("Upis novog studenta")

    prozor2.geometry("475x600")
    prozor2.configure(bg = "#DDF2E8")
    prozor2.resizable(False,False)


    # Ime
    ime = Label(prozor2, text = "Ime:", font = ("Helvetica", 10, "bold"), bg = "#DDF2E8")
    ime.pack(pady = 10)

    ime_unos = Entry(prozor2, width = 30)
    ime_unos.pack()

    # Prezime
    prezime = Label(prozor2, text = "Prezime:", font = ("Helvetica", 10, "bold"), bg = "#DDF2E8")
    prezime.pack(pady = 10)

    prezime_unos = Entry(prozor2, width = 30)
    prezime_unos.pack()
    
    # jmbg
    jmbg = Label(prozor2, text = "Matični broj studenta:", font = ("Helvetica", 10, "bold"), bg = "#DDF2E8")
    jmbg.pack(pady = 10)

    jmbg_unos = Entry(prozor2, width = 30)
    jmbg_unos.pack()

    # Broj indeksa:
    novi_br_indeksa = Label(prozor2, text = "Broj indeksa prijavljenog studenta:",  font = ("Helvetica", 10, "bold"), bg = "#DDF2E8")
    novi_br_indeksa.pack(pady = 10)

    br_indeksa_unos = Entry(prozor2, width = 10)
    br_indeksa_unos.pack()

    # predmeti i ocene:
    predmeti_unos = Label(prozor2, text = "Predmeti:", font = ("Helvetica", 10, "bold"), bg = "#DDF2E8")
    predmeti_unos.pack(pady = 10)

    ost1 = Label(prozor2, text = "OST1", font = ("Helvetica", 10, "bold"), bg = "#DDF2E8")
    ost1.pack()
    ost1_ocena = Entry(prozor2, width = 30)
    ost1_ocena.pack()

    ost2 = Label(prozor2, text = "OST2", font = ("Helvetica", 10, "bold"), bg = "#DDF2E8")
    ost2.pack()
    ost2_ocena = Entry(prozor2, width = 30)
    ost2_ocena.pack()

    sukn = Label(prozor2, text = "SUKN", font = ("Helvetica", 10, "bold"), bg = "#DDF2E8")
    sukn.pack()
    sukn_ocena = Entry(prozor2, width = 30)
    sukn_ocena.pack()

    opks = Label(prozor2, text = "OPKS", font = ("Helvetica", 10, "bold"), bg = "#DDF2E8")
    opks.pack()
    opks_ocena = Entry(prozor2, width = 30)
    opks_ocena.pack()

    # Dugme provere:
    upisS = Button(prozor2, text = "Upis studenta", font = ('Helvetica', 11), bg = "#C39BD3", command = lambda: provera(ime_unos.get(), prezime_unos.get(), br_indeksa_unos.get(), jmbg_unos.get(), [ost1_ocena.get(),ost2_ocena.get(),sukn_ocena.get(),opks_ocena.get()], prozor2))
    upisS.pack(pady = 30)
#______________________________________________

root = Tk()

# Naslov
naslov = Label(root, text = "STUDENTSKI DOSIJE",font = ('Helvetica', 14, 'bold'), bg = "#DDF2E8", fg = "#0E063D")
naslov.pack(padx = 10, pady = 10)

# Unos indeksa
unos_opis = Label(root, text = "Uneti broj indeksa:",font = ('Helvetica', 12), bg = "#DDF2E8")
unos_opis.pack()

unos = Entry()
unos.pack()

# Dugme za proveru
pr_indeksa = Button(root, text = "PROVERA", font = ('Helvetica', 11), bg = "#96B7B6", command = provera_br_indeksa)
pr_indeksa.pack(padx = 10, pady = 10)

# Meni
meni = Menu(root)
podmeni = Menu(meni, tearoff = 0)
podmeni.add_command(label = "Podaci o studentu",command = upis)
podmeni.add_command(label = "Izađi", command = root.destroy)
meni.add_cascade(label = "Upis novog studenta", menu = podmeni)
meni.add_command(label = "O programu", command = o_programu)
root.config(menu = meni)


root.configure(bg = "#DDF2E8")
root.geometry("300x200+550+220")
root.resizable(False, False)
root.title(" Saobraćajni fakultet ")
root.mainloop()