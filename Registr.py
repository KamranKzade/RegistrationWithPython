alluser = [["Kamran", "Kerimzade", "311_kamran@mail.ru", "kamran311", [27, "Mart", 1999], "Kisi"]]
allWorker = {
    0: {
        'Ad': 'Kamran',
        'Soyad': 'Kerimzade',
        'Ata adi': 'Natiq',
        'Dogum tarixi': [27, 'Mart', 1999],
        'Yas': 22,
        'Cinsiyyet': 'Kisi',
        'Vezife': 'Müdir',
        'Is tecrubesi': '1 - 3 il arasi',
        'Seher': 'Baki',
        'Unvan': 'Sabuncu',
        'Haqqinda': 'Yaxsi insanam\n'
    },
}

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date

window = Tk()
window.geometry("1500x750")
window.title("Ulduz Restoran")
window.resizable(0, 0)

## tarix
bugun = date.today()

## istifade olunan sekiller
loginPhoto = PhotoImage(file="Img-Ev-tapsirigi/login.gif")
aciqPhoto = PhotoImage(file="Img-Ev-tapsirigi/aciq.gif")
bagliPhoto = PhotoImage(file="Img-Ev-tapsirigi/bagli.gif")
savePhoto = PhotoImage(file="Img-Ev-tapsirigi/savebutton.gif")
searchPhoto = PhotoImage(file="Img-Ev-tapsirigi/searchbutton.gif")
editPhoto = PhotoImage(file="Img-Ev-tapsirigi/editbutton.gif")
deletePhoto = PhotoImage(file="Img-Ev-tapsirigi/deletebutton.gif")
filterPhoto = PhotoImage(file="Img-Ev-tapsirigi/filter.gif")
adduserPhoto = PhotoImage(file="Img-Ev-tapsirigi/add user.gif")
edituserPhoto = PhotoImage(file="Img-Ev-tapsirigi/edit.gif")
deleteuserPhoto = PhotoImage(file="Img-Ev-tapsirigi/delete.gif")
printuserPhoto = PhotoImage(file="Img-Ev-tapsirigi/printesas.gif")
solframme = PhotoImage(file="Img-Ev-tapsirigi/sol.gif")
adduserFrame = PhotoImage(file="Img-Ev-tapsirigi/adduserFrame.gif")
editFrame = PhotoImage(file="Img-Ev-tapsirigi/editFrame.gif")
deleteFrame = PhotoImage(file="Img-Ev-tapsirigi/deleteFrame.gif")
printFrame = PhotoImage(file="Img-Ev-tapsirigi/printFrame.gif")

## butun frame-ler
login_frame = Frame(window, bg="blue")
frame_sol = Frame(login_frame)
frame_sag = Frame(login_frame, bg="yellow")
frame_adduser = Frame(frame_sag)
frame_sagEdit = Frame(frame_sag)
frame_sagDelete = Frame(frame_sag)
frame_sagPrint = Frame(frame_sag)


frame_Beging = Frame(window)
frame_Beging.pack(expand=True, fill=BOTH)

## buttonlarin funksiyalari
def sagButton():
    frame_sagPrint.forget()
    frame_sagDelete.forget()
    frame_sagEdit.forget()
    frame_adduser.pack(expand=True, fill=BOTH)

def sagEditButton():
    frame_sagPrint.forget()
    frame_sagDelete.forget()
    frame_adduser.forget()
    frame_sagEdit.pack(expand=True, fill=BOTH)

def sagDeleteButton():
    frame_sagPrint.forget()
    frame_adduser.forget()
    frame_sagEdit.forget()
    frame_sagDelete.pack(expand=True, fill=BOTH)

def sagPrintButton():
    frame_adduser.forget()
    frame_sagDelete.forget()
    frame_sagEdit.forget()
    frame_sagPrint.pack(expand=True, fill=BOTH)

    index = 0

    listwiev.delete(0, END)
    for key, value in allWorker.items():
        listwiev.insert(index, f"{value['Ad']}   {value['Soyad']}   {value['Ata adi']}   {value['Vezife']}")
        index += 1

## edit frame in arxa fonu
labeladduser = Label(frame_sagEdit, image=editFrame)
labeladduser.place(x=0, y=0)

## Iscilerin edit edilmesinde yoxlanis buttonu

def yoxlanisedit():
    for key, value in allWorker.items():
        if entryNameedit.get() == value['Ad']:
            if entrySurnameedit.get() == value["Soyad"]:
                if entryfatherNameedit.get() == value["Ata adi"]:
                    bosluqedit.config(text="İşçi tapıldı")
                    def edit():
                        if len(vezifecomboboxedit1.get()) < 1:
                            bosluqedit.config(text="Vəzifəni daxil edin!!!")
                        elif len(tecrubecomboboxedit2.get()) < 1:
                            bosluqedit.config(text="Təcrübəni daxil edin!!!")
                        elif len(sehercomboboxedit3.get()) < 1:
                            bosluqedit.config(text="Şəhəri daxil edin!!!")
                        elif len(unvanentryedit.get()) < 1:
                            bosluqedit.config(text="Ünvanınızı daxil edin!!!")
                        else:
                            bosluqedit.config(text="Məlumatlar uğurla dəyişdirildi")
                        value["Vezife"] = vezifecomboboxedit1.get()
                        value["Is tecrubesi"] = tecrubecomboboxedit2.get()
                        value["Seher"] = sehercomboboxedit3.get()
                        value["Unvan"] = unvanentryedit.get()

                    ## Vəzifənin yazılışı
                    vezifeLabeledit = Label(frame_sagEdit, text="Vəzifə", fg="black", bg="lavenderblush", font=("Comic Sans Ms", 10, "bold"))
                    vezifeLabeledit.place(relx=0.01, rely=0.35, relwidth=0.1, relheight=0.1)
                    ## İş təcrübəsinin yazılışı
                    tecrubeLabeledit = Label(frame_sagEdit, text="İş təcrübəsi", fg="black", bg="lavenderblush", font=("Comic Sans Ms", 10, "bold"))
                    tecrubeLabeledit.place(relx=0.3, rely=0.35, relwidth=0.1, relheight=0.1)
                    ## Doğum yerinin yazılışı
                    seherLabeledit = Label(frame_sagEdit, text="Doğum yeri", fg="black", bg="lavenderblush", font=("Comic Sans Ms", 10, "bold"))
                    seherLabeledit.place(relx=0.01, rely=0.45, relwidth=0.1, relheight=0.1)
                    ##Qeydiyyat ünvanının yazılışı
                    unvanLabeledit = Label(frame_sagEdit, text="Qeydiyyat ünvanı", fg="black", bg="lavenderblush", font=("Comic Sans Ms", 10, "bold"))
                    unvanLabeledit.place(relx=0.3, rely=0.45, relwidth=0.1, relheight=0.1)
                    ## Qeydiyyat ünvanının daxil edilməsi üçün kod
                    unvanentryedit = Entry(frame_sagEdit, fg="black", bg="white", font=("Comic Sans MS", 13, "bold"))
                    unvanentryedit.place(relx=0.45, rely=0.48, relwidth=0.2, relheight=0.05)

                    ## Vəzifə seçim
                    edit1 = StringVar()
                    vezife500 = ["Müdir", "Administrator", "Aşbaz", "Aşbaz köməkçisi", "Ofisiant", "Ofisiant köməkçisi", "Resepşn", "Vale"]
                    vezifecomboboxedit1 = ttk.Combobox(frame_sagEdit, state='readonly', values=vezife500, textvariable=edit1, font=("Comic Sans Ms", 10, "bold"))
                    vezifecomboboxedit1.place(relx=0.15, rely=0.38, relwidth=0.1, relheight=0.05)
                    ## İş təcrübəsi seçim
                    edit2 = StringVar()
                    Tecrube500 = ["1 ildən az", "1 - 3 il arası", "3 ildən cox"]
                    tecrubecomboboxedit2 = ttk.Combobox(frame_sagEdit, state='readonly', values=Tecrube500, textvariable=edit2, font=("Comic Sans Ms", 10, "bold"))
                    tecrubecomboboxedit2.place(relx=0.45, rely=0.38, relwidth=0.1, relheight=0.05)
                    ## Şəhər seçim
                    edit3 = StringVar()
                    seher500 = ['Ağcabədi', 'Ağdam', 'Ağdaş', 'Ağstafa', 'Ağsu', 'Astara', 'Babək', 'Bakı', 'Balakən', 'Beyləqan', 'Bərdə','Biləsuvar',
                                'Cəbrayıl', 'Cəlilabad', 'Culfa', 'Daşkəsən','Dəliməmmədli', 'Füzuli', 'Gədəbəy', 'Gəncə', 'Goranboy', 'Göyçay', 'Göygöl',
                                'Göytəpə', 'İmişli', 'İsmayıllı', 'Kəlbəcər', 'Kürdəmir', 'Qax', 'Qazax','Qəbələ', 'Qobustan', 'Qovlar', 'Quba', 'Qubadlı',
                                'Qusar', 'Laçın', 'Lerik', 'Lənkəran', 'Liman', 'Masallı', 'Mingəçevir', 'Naftalan', 'Naxçıvan', 'Neftçala', 'Oğuz', 'Ordubad',
                                'Saatlı', 'Sabirabad', 'Salyan', 'Samux', 'Siyəzən', 'Sumqayıt', 'Şabran', 'Şahbuz', 'Şamaxı', 'Şəki', 'Şəmkir', 'Şərur', 'Şirvan',
                                'Şuşa', 'Tərtər', 'Tovuz', 'Ucar', 'Yardımlı', 'Yevlax', 'Zaqatala', 'Zəngilan', 'Zərdab']
                    sehercomboboxedit3 = ttk.Combobox(frame_sagEdit, state='readonly', values=seher500, textvariable=edit3, font=("Comic Sans Ms", 10, "bold"))
                    sehercomboboxedit3.place(relx=0.15, rely=0.48, relwidth=0.1, relheight=0.05)

                    ## Edit düyməsi
                    editButtonedit = Button(frame_sagEdit, image=editPhoto, command=edit)
                    editButtonedit.place(relx=0.25, rely=0.55, relwidth=0.184, relheight=0.2)
                    break
                else:
                    bosluqedit.config(text="Belə Ata adı mövcud deyil")
            else:
                bosluqedit.config(text="Belə Soyad mövcüd deyil")
        else:
            bosluqedit.config(text="Belə Ad mövcüd deyil")

## delete frame in arxa  rengi
labeladduser = Label(frame_sagDelete, image=deleteFrame)
labeladduser.place(x=0, y=0)

## iscilerin silinmeyinde yoxlanis buttonunun funksiyasi
def yoxlanisdelete():
    for key, value in allWorker.items():
        if entryNamedelete.get() == value["Ad"]:
            if entrySurnamedelete.get() == value["Soyad"]:
                if entryfatherNamedelete.get() == value["Ata adi"]:
                    bosluqdelete.config(text="İşçi tapıldı")
                    def delete():
                        check = messagebox.askyesno("AskYesNO", "Silmək istədiyinizə əminsiniz? ")
                        if check:
                            del allWorker[key]
                    ## Delete düyməsi
                    deleteButtondelete = Button(frame_sagDelete, image=deletePhoto, command=delete)
                    deleteButtondelete.place(relx=0.30, rely=0.55, relwidth=0.184, relheight=0.185)
                else:
                    bosluqdelete.config(text="Belə Ata adı mövcud deyil")
            else:
                bosluqdelete.config(text="Belə Soyad mövcud deyil")
        else:
            bosluqdelete.config(text="Belə Ad mövcud deyil")


labeladduser = Label(frame_sagPrint, image=printFrame)
labeladduser.place(x=0, y=0)

## Run eldeikde olacaq sehvenin hansi sehvelerle bagli olma funksiyasi
def login_form():
    frame_Beging.forget()
    login_frame.pack(expand=True, fill=BOTH)
    frame_sol.place(relx=0, rely=0, relwidth=1, relheight=1)
    frame_sag.place(relx=0.2, rely=0, relwidth=1, relheight=1)

## adduser frame-in arxa fonu
labeladduser = Label(frame_adduser, image=adduserFrame)
labeladduser.place(x=0, y=0)

## Save düyməsinin yerinə yetirdiyi funksiya
index = 1
def save():
    global index
    if len(entryName.get()) < 3:
        bosluq.config(text="Adınız 3 hərfdən az ola bilməz!!!")
    elif len(entrySurname.get()) < 3:
        bosluq.config(text="Soyadınız 3 hərfdən az ola bilməz")
    elif len(entryfatherName.get()) < 3:
        bosluq.config(text="Ata adınız 3 hərfdən az ola bilməz")
    elif int(comboboxil.get()) < 1965:
        bosluq.config(text="Doğum iliniz 1965-dən aşağı ola bilməz!!!")
    elif len(comboboxay.get()) == 2:
        bosluq.config(text="Doğum ayınızı daxil edin!!!")
    elif int(comboboxgun.get()) < 1:
        bosluq.config(text="Doğum gününüzü daxil edin!!!")
    elif len(genderadduser.get()) < 1:
        bosluq.config(text="Cinsiyyətinizi daxil edin!!!")
    elif vezifecombobox.get() == 'Vezife':
        bosluq.config(text="Vəzifənizi daxil edin!!!")
    elif tecrubecombobox.get() == 'Tecrube':
        bosluq.config(text="Təcrübənizi daxil edin!!!")
    elif sehercombobox.get() == 'Seher':
        bosluq.config(text="Yaşadığınız şəhəri daxil edin!!!")
    elif len(unvanentry.get()) < 1:
        bosluq.config(text="Ünvanınızı daxil edin!!!")
    elif len(haqqinda.get(0.0, END)) == 1:
        bosluq.config(text="Haqqınızda məlumat daxil edin!!!")
    else:
        bosluq.config(text="Uğurla qeydiyyatdan keçdiniz")
        allWorker[index] = {
            "Ad": entryName.get(),
            "Soyad": entrySurname.get(),
            "Ata adi": entryfatherName.get(),
            "Dogum tarixi": [int(comboboxgun.get()), comboboxay.get(), int(comboboxil.get())],
            "Yas": bugun.year - int(comboboxil.get()),
            "Cinsiyyet": str(genderadduser.get()),
            "Vezife": vezifecombobox.get(),
            "Is tecrubesi": tecrubecombobox.get(),
            "Seher": sehercombobox.get(),
            "Unvan": unvanentry.get(),
            "Haqqinda": haqqinda.get(0.0, END)
        }
        index += 1


## Qeydiyyatda olan yazıların yazılma şəkli
namelabel = Label(frame_adduser, text="Ad                 ", fg="black", bg="darkslategrey", font=("Times New Roman", 15, "bold"))
namelabel.place(relx=0.01, rely=0.011, relwidth=0.08, relheight=0.05)
surnamelabel = Label(frame_adduser, text="Soyad          ", fg="black", bg="darkslategrey", font=("Times New Roman", 14, "bold"))
surnamelabel.place(relx=0.33, rely=0.011, relwidth=0.08, relheight=0.05)
fatherNamelabel = Label(frame_adduser, text="Ata adı", fg="black", bg="darkslategrey", font=("Times New Roman", 15, "bold"))
fatherNamelabel.place(relx=0.58, rely=0.011, relwidth=0.08, relheight=0.05)
labeldogumIli = Label(frame_adduser, text="Doğum tarixi", fg="black", bg="darkslategrey", font=("Times New Roman", 15, "bold"))
labeldogumIli.place(relx=0.01, rely=0.1, relwidth=0.08, relheight=0.05)
genderLabel = Label(frame_adduser, text="Cinsiyyət      ", fg="black", bg="darkslategrey", font=("Times New Roman", 14, "bold"))
genderLabel.place(relx=0.33, rely=0.1, relwidth=0.08, relheight=0.05)
vezifeLabel = Label(frame_adduser, text="Vəzifə           ", fg="black", bg="darkslategrey", font=("Times New Roman", 15, "bold"))
vezifeLabel.place(relx=0.01, rely=0.46, relwidth=0.08, relheight=0.05)
tecrubeLabel = Label(frame_adduser, text="İş təcrübəsi", fg="black", bg="darkslategrey", font=("Times New Roman", 15, "bold"))
tecrubeLabel.place(relx=0.33, rely=0.46, relwidth=0.08, relheight=0.05)
seherLabel = Label(frame_adduser, text="Doğum yeri  ", fg="black", bg="darkslategrey", font=("Times New Roman", 15, "bold"))
seherLabel.place(relx=0.01, rely=0.19, relwidth=0.08, relheight=0.05)
unvanLabel = Label(frame_adduser, text="Qeydiyyat ünvanı", fg="black", bg="darkslategrey", font=("Times New Roman", 14, "bold"))
unvanLabel.place(relx=0.33, rely=0.19, relwidth=0.10, relheight=0.05)
finkodlabel = Label(frame_adduser, text="Fin Kod         ", fg="black", bg="darkslategrey", font=("Times New Roman", 15, "bold"))
finkodlabel.place(relx=0.01, rely=0.37, relwidth=0.08, relheight=0.05)
faktikiunvanlabel = Label(frame_adduser, text=" Faktiki ünvan", fg="black", bg="darkslategrey", font=("Times New Roman", 15, "bold"))
faktikiunvanlabel.place(relx=0.01, rely=0.28, relwidth=0.08, relheight=0.05)
sexsiyyetvesiqelabel = Label(frame_adduser, text="Şəxsiyyət vəsiqəsinin seriyası", fg="black", bg="darkslategrey", font=("Times New Roman", 15, "bold"))
sexsiyyetvesiqelabel.place(relx=0.33, rely=0.28, relwidth=0.17, relheight=0.05)
elaqelabel = Label(frame_adduser, text="Əlaqə nömrəsi", fg="black", bg="darkslategrey", font=("Times New Roman", 15, "bold"))
elaqelabel.place(relx=0.33, rely=0.37, relwidth=0.085, relheight=0.05)
maillabel = Label(frame_adduser, text="Mail       ", fg="black", bg="darkslategrey", font=("Times New Roman", 15, "bold"))
maillabel.place(relx=0.58, rely=0.37, relwidth=0.08, relheight=0.05)
## Haqqınızdanın yazılışı
aboutLabel = Label(frame_adduser, text="Haqqınızda   ", fg="black", bg="darkslategrey", font=("Times New Roman", 15, "bold"))
aboutLabel.place(relx=0.01, rely=0.55, relwidth=0.08, relheight=0.05)

## Qeydiyyatda məlumat daxil etmək üçün olan kodlar
entryName = Entry(frame_adduser, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
entryName.place(relx=0.14, rely=0.01325, relwidth=0.12, relheight=0.05)
entrySurname = Entry(frame_adduser, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
entrySurname.place(relx=0.44, rely=0.01325, relwidth=0.1, relheight=0.05)
entryfatherName = Entry(frame_adduser, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
entryfatherName.place(relx=0.7, rely=0.01325, relwidth=0.09, relheight=0.05)
## Qeydiyyat ünvanı məlumatını daxil etmək üçün
unvanentry = Entry(frame_adduser, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
unvanentry.place(relx=0.44, rely=0.19, relwidth=0.21, relheight=0.05)
## Faktiki ünvan və  Şəxsiyyət vəsiqəsinin seriya nömrəsini daxil etmək üçün
entryfaktikiunvan = Entry(frame_adduser, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
entryfaktikiunvan.place(relx=0.14, rely=0.28, relwidth=0.12, relheight=0.05)
entrysexsiyyetvesiqe = Entry(frame_adduser, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
entrysexsiyyetvesiqe.place(relx=0.54, rely=0.28, relwidth=0.11, relheight=0.05)
#### FİN kod, Əlaqə nömrəsi, Maili daxil etmək üçün
finkodentry = Entry(frame_adduser, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
finkodentry.place(relx=0.14, rely=0.37, relwidth=0.12, relheight=0.05)
entryelaqe = Entry(frame_adduser, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
entryelaqe.place(relx=0.44, rely=0.37, relwidth=0.1, relheight=0.05)
entrymail = Entry(frame_adduser, fg="black", bg="white", font=("Times New Roman", 14, "normal"))
entrymail.place(relx=0.7, rely=0.37, relwidth=0.09, relheight=0.05)

## Seçim etmək üçün
## Günü seçmək
comboNumber = IntVar()
gunler = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
comboboxgun = ttk.Combobox(frame_adduser, state='readonly', text=1, values=gunler, textvariable=comboNumber, font=("Times New Roman", 15, "normal"))
comboboxgun.place(relx=0.14, rely=0.1, relwidth=0.05, relheight=0.05)
comboboxgun.current(0)
## Ayı seçmək
addusercomboString = StringVar()
adduseraylar = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "İyun", "İyul", "Avqust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]
comboboxay = ttk.Combobox(frame_adduser, state='readonly', values=adduseraylar, textvariable=addusercomboString, font=("Times New Roman", 10, "normal"))
comboboxay.set('Ay')
comboboxay.place(relx=0.2, rely=0.1, relwidth=0.05, relheight=0.05)
## İL - i seçmək
comboIl = IntVar()
iller=[1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982,
       1983, 1984,1985, 1986, 1987, 1988, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002,
       2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
comboboxil = ttk.Combobox(frame_adduser,  state='readonly', text=1, values=iller, textvariable=comboIl, font=("Times New Roman", 13, "normal"))
comboboxil.place(relx=0.26, rely=0.1, relwidth=0.05, relheight=0.05)
comboboxil.current(0)
## Vəzifə seçimi
vezifecomboString = StringVar()
vezifeadduser = ["Müdir", "Administrator", "Aşbaz", "Aşbaz köməkçisi", "Ofisiant", "Ofisiant köməkçisi", "Resepşn", "Vale"]
vezifecombobox = ttk.Combobox(frame_adduser, state='readonly', values=vezifeadduser, textvariable=vezifecomboString, font=("Times New Roman", 15, "normal"))
vezifecombobox.place(relx=0.14, rely=0.46, relwidth=0.12, relheight=0.05)
vezifecombobox.set("Vəzifə")
## İş təcrübəsi seçimi
tecrubecomboString = StringVar()
tecrubeadduser = ["1 ildən az", "1 - 3 il arası", "3 ildən çox"]
tecrubecombobox = ttk.Combobox(frame_adduser, state='readonly', values=tecrubeadduser, textvariable=tecrubecomboString, font=("Times New Roman", 15, "normal"))
tecrubecombobox.place(relx=0.44, rely=0.46, relwidth=0.1, relheight=0.05)
tecrubecombobox.set("Təcrübə")
## Şəhər seçimi
comboStringSeher = StringVar()
seherAdduser = ['Ağcabədi', 'Ağdam', 'Ağdaş', 'Ağstafa', 'Ağsu', 'Astara', 'Babək', 'Bakı', 'Balakən', 'Beyləqan', 'Bərdə', 'Biləsuvar',
                'Cəbrayıl', 'Cəlilabad', 'Culfa', 'Daşkəsən', 'Füzuli', 'Gədəbəy', 'Gəncə','Goranboy', 'Göyçay', 'Göygöl', 'Göytəpə',
                'İmişli', 'İsmayıllı', 'Kəlbəcər', 'Kürdəmir', 'Qax', 'Qazax', 'Qəbələ', 'Qobustan', 'Qovlar', 'Quba', 'Qubadlı',
                'Qusar', 'Laçın', 'Lerik', 'Lənkəran', 'Liman', 'Masallı', 'Mingəçevir', 'Naftalan', 'Naxçıvan', 'Neftçala', 'Oğuz',
                'Ordubad', 'Saatlı', 'Sabirabad', 'Salyan', 'Samux', 'Siyəzən', 'Sumqayıt', 'Şabran', 'Şahbuz', 'Şamaxı', 'Şəki',
                'Şəmkir', 'Şərur', 'Şirvan', 'Şuşa', 'Tərtər', 'Tovuz', 'Ucar', 'Yardımlı', 'Yevlax', 'Zaqatala', 'Zəngilan', 'Zərdab']
sehercombobox = ttk.Combobox(frame_adduser, state='readonly', values=seherAdduser, textvariable=comboStringSeher, font=("Times New Roman", 15, "normal"))
sehercombobox.place(relx=0.14, rely=0.19, relwidth=0.08, relheight=0.05)
sehercombobox.set("Doğum yeri")

## İkili seçim (Kişi və ya Qadın)
genderadduser = StringVar()
## Kişi yazılış
maleAdduser = Radiobutton(frame_adduser, text="Kişi", bg="darkslategrey", variable=genderadduser, value="Kisi", font=("Times New Roman", 15, "bold"))
maleAdduser.place(relx=0.44, rely=0.1, relwidth=0.08, relheight=0.05)
## Qadin yazılış
femaleAdduser = Radiobutton(frame_adduser, text="Qadın", bg="darkslategrey", variable=genderadduser, value="Qadin", font=("Times New Roman", 15, "bold"))
femaleAdduser.place(relx=0.566, rely=0.1, relwidth=0.08, relheight=0.05)
## İkili seçim (Kişi və ya Qadın)
genderadduser = StringVar()
## Kişi yazılış
maleAdduser = Radiobutton(frame_adduser, text="Kişi", bg="darkslategrey", variable=genderadduser, value="Kisi", font=("Times New Roman", 15, "bold"))
maleAdduser.place(relx=0.44, rely=0.1, relwidth=0.08, relheight=0.05)
## Qadin yazılış
femaleAdduser = Radiobutton(frame_adduser, text="Qadın", bg="darkslategrey", variable=genderadduser, value="Qadin", font=("Times New Roman", 15, "bold"))
femaleAdduser.place(relx=0.566, rely=0.1, relwidth=0.08, relheight=0.05)

## Haqqınızda əlavə etmək üçün yer
haqqinda = Text(frame_adduser, fg="black", font=("Times New Roman", 15, "normal"))
haqqinda.place(relx=0.14, rely=0.55, relwidth=0.6, relheight=0.15)
## Save düyməsi zamanı yoxlanışda səhvlik olsa görünəcək yazıların kodu
bosluq = Label(frame_adduser, text="", fg="red", bg="darkslategrey", font=("Times New Roman", 15, "bold"))
bosluq.place(relx=0.2, rely=0.75, relwidth=0.4, relheight=0.05)
## Qeydiyyatda olan save düyməsi
saveButton = Button(frame_adduser, image=savePhoto, command=save)
saveButton.place(relx=0.35, rely=0.83, relwidth=0.05, relheight=0.04)


## Düzəlişdə olan yazılar
namelabeledit = Label(frame_sagEdit, text="Ad                 ", fg="black", bg="lavenderblush", font=("Times New Roman", 15, "bold"))
namelabeledit.place(relx=0.01, rely=0.011, relwidth=0.08, relheight=0.05)
surnamelabeledit = Label(frame_sagEdit, text="Soyad          ", fg="black", bg="lavenderblush", font=("Times New Roman", 15, "bold"))
surnamelabeledit.place(relx=0.33, rely=0.011, relwidth=0.08, relheight=0.05)
fatherNamelabeledit = Label(frame_sagEdit, text="Ata adı", fg="black", bg="lavenderblush", font=("Times New Roman", 15, "bold"))
fatherNamelabeledit.place(relx=0.58, rely=0.011, relwidth=0.08, relheight=0.05)
finkodlabeledit= Label(frame_sagEdit, text="Fin Kod         ", fg="black", bg="lavenderblush", font=("Times New Roman", 15, "bold"))
finkodlabeledit.place(relx=0.01, rely=0.11, relwidth=0.08, relheight=0.05)
## Düzəlişdə olan gizli yazılar
bosluqedit = Label(frame_sagEdit, text="", fg="red", bg="lavenderblush", font=("Comic Sans Ms", 13, "bold"))
bosluqedit.place(relx=0.15, rely=0.20, relwidth=0.4, relheight=0.05)

## Düzəlişdə məlumatların daxil edilməsi üçün
entryNameedit = Entry(frame_sagEdit, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
entryNameedit.place(relx=0.14, rely=0.01325, relwidth=0.12, relheight=0.05)
entrySurnameedit = Entry(frame_sagEdit, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
entrySurnameedit.place(relx=0.44, rely=0.01325, relwidth=0.1, relheight=0.05)
entryfatherNameedit = Entry(frame_sagEdit, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
entryfatherNameedit.place(relx=0.7, rely=0.01325, relwidth=0.09, relheight=0.05)
finkodentryedit = Entry(frame_sagEdit, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
finkodentryedit.place(relx=0.14, rely=0.11, relwidth=0.12, relheight=0.05)
## Düzəlişdə olan save button
yoxlanisButtonedit = Button(frame_sagEdit, image=searchPhoto, command=yoxlanisedit)
yoxlanisButtonedit.place(relx=0.3, rely=0.27, relwidth=0.08, relheight=0.07)


## Silməkdə olan yazılar
namelabeldelete = Label(frame_sagDelete, text="Ad                 ", fg="black", bg="mediumseagreen", font=("Times New Roman", 15, "bold"))
namelabeldelete.place(relx=0.01, rely=0.011, relwidth=0.08, relheight=0.05)
surnamelabeldelete = Label(frame_sagDelete, text="Soyad          ", fg="black", bg="mediumseagreen", font=("Times New Roman", 15, "bold"))
surnamelabeldelete.place(relx=0.33, rely=0.011, relwidth=0.08, relheight=0.05)
fatherNamelabeldelete = Label(frame_sagDelete, text="Ata adı", fg="black", bg="mediumseagreen", font=("Times New Roman", 15, "bold"))
fatherNamelabeldelete.place(relx=0.58, rely=0.011, relwidth=0.08, relheight=0.05)
finkodlabeldelete = Label(frame_sagDelete, text="Fin Kod         ", fg="black", bg="mediumseagreen", font=("Times New Roman", 15, "bold"))
finkodlabeldelete.place(relx=0.01, rely=0.11, relwidth=0.08, relheight=0.05)
## Silməkdə olan axtarisda görünəcək yazılar
bosluqdelete = Label(frame_sagDelete, text="", fg="red", bg="mediumseagreen", font=("Comic Sans Ms", 13, "bold"))
bosluqdelete.place(relx=0.15, rely=0.20, relwidth=0.4, relheight=0.05)

## Silməkdə olan məlumatları daxil etmək üçün olan kodlar
entryNamedelete = Entry(frame_sagDelete, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
entryNamedelete.place(relx=0.14, rely=0.01325, relwidth=0.12, relheight=0.05)
entrySurnamedelete = Entry(frame_sagDelete, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
entrySurnamedelete.place(relx=0.44, rely=0.01325, relwidth=0.1, relheight=0.05)
entryfatherNamedelete = Entry(frame_sagDelete, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
entryfatherNamedelete.place(relx=0.7, rely=0.01325, relwidth=0.09, relheight=0.05)
finkodentrydelete = Entry(frame_sagDelete, fg="black", bg="white", font=("Times New Roman", 15, "normal"))
finkodentrydelete.place(relx=0.14, rely=0.11, relwidth=0.12, relheight=0.05)

## Silmıkdə olan0 yoxlanis düyməsi
yoxlanisButtondelete = Button(frame_sagDelete, image=searchPhoto, command=yoxlanisdelete)
yoxlanisButtondelete.place(relx=0.3, rely=0.27, relwidth=0.08, relheight=0.07)


## printde olan funksiya

def printFunktion():
    index = 0
    listwiev.delete(0, END)
    for key, value in allWorker.items():
        if vezifecomboboxprint.get() == value["Vezife"]:
            listwiev.insert(index, f"{value['Ad']}  {value['Soyad']}   {value['Ata adi']}")
        elif vezifecomboboxprint.get() == value['Vezife']:
            listwiev.insert(index, f"{value['Ad']}  {value['Soyad']}    {value['Ata adi']}")
        elif vezifecomboboxprint.get() == value['Vezife']:
            listwiev.insert(index, f"{value['Ad']}  {value['Soyad']}    {value['Ata adi']}")
        elif vezifecomboboxprint.get() == value['Vezife']:
            listwiev.insert(index, f"{value['Ad']}   {value['Soyad']}    {value['Ata adi']}")
        elif vezifecomboboxprint.get() == value['Vezife']:
            listwiev.insert(index, f"{value['Ad']}   {value['Soyad']}    {value['Ata adi']}")
        elif vezifecomboboxprint.get() == value['Vezife']:
            listwiev.insert(index, f"{value['Ad']}   {value['Soyad']}    {value['Ata adi']}")
        elif vezifecomboboxprint.get() == value['Vezife']:
            listwiev.insert(index, f"{value['Ad']}   {value['Soyad']}    {value['Ata adi']}")
        elif vezifecomboboxprint.get() == value['Vezife']:
            listwiev.insert(index, f"{value['Ad']}   {value['Soyad']}    {value['Ata adi']}")
        index += 1

## Bütün istifadəçilər səhifəsində olan yazılar
namelabelprint = Label(frame_sagPrint, text="Ad                 ", fg="white", bg="black", font=("Times New Roman", 15, "bold"))
namelabelprint.place(relx=0.01, rely=0.01, relwidth=0.08, relheight=0.1)
surnamelabelprint = Label(frame_sagPrint, text="Soyad          ", fg="white", bg="black", font=("Times New Roman", 15, "bold"))
surnamelabelprint.place(relx=0.15, rely=0.01, relwidth=0.08, relheight=0.1)
fatherNamelabelprint = Label(frame_sagPrint, text="Ata adı", fg="white", bg="black", font=("Times New Roman", 15, "bold"))
fatherNamelabelprint.place(relx=0.33, rely=0.01, relwidth=0.08, relheight=0.1)
vezifeLabelprint = Label(frame_sagPrint, text="Vəzifə   ", fg="white", bg="black", font=("Times New Roman", 15, "bold"))
vezifeLabelprint.place(relx=0.45, rely=0.01, relwidth=0.08, relheight=0.1)

## Bütün istifadəçilər səhifəsində olan listwiev
listwiev = Listbox(frame_sagPrint, font=("Times New Roman", 44, "normal"))
listwiev.place(relx=0, rely=0.15, relwidth=1, relheight=1)

## Bütün istifadəçilər səhifəsində olan seçim
print1 = StringVar()
print2 = ["Müdir", "Administrator", "Aşbaz", "Aşbaz köməkçisi", "Ofisiant", "Ofisiant köməkçisi", "Resepşn", "Vale"]
vezifecomboboxprint = ttk.Combobox(frame_sagPrint, state="readonly", values=print2, textvariable=print1)
vezifecomboboxprint.place(relx=0.55, rely=0.03, relwidth=0.08, relheight=0.05)
vezifecomboboxprint.set("Müdir")

## Bütün istifadəçilər səhifəsində olan düymə
filterButton = Button(frame_sagPrint, image=filterPhoto, command=printFunktion)
filterButton.place(relx=0.65, rely=0.03, relwidth=0.09, relheight=0.064)

## solframe ve sagframe - in arxa fonlari
labelsolFrame = Label(frame_sol, image=solframme)
labelsolFrame.place(x=0, y=0)

## framede olan buttonlar
button1 = Button(frame_sol, image=adduserPhoto, command=lambda: sagButton())
button1.place(relx=0.07, rely=0.15, relwidth=0.07, relheight=0.15)
button2 = Button(frame_sol, image=edituserPhoto, command=lambda: sagEditButton())
button2.place(relx=0.07, rely=0.35, relwidth=0.07, relheight=0.15)
button3 = Button(frame_sol, image=deleteuserPhoto, command=lambda: sagDeleteButton())
button3.place(relx=0.07, rely=0.55, relwidth=0.07, relheight=0.15)
button4 = Button(frame_sol, image=printuserPhoto, command=lambda: sagPrintButton())
button4.place(relx=0.07, rely=0.75, relwidth=0.07, relheight=0.15)

## Window penceresindeki Restoranın adının qeyd edilməsi kodu
text_label = Label(frame_Beging, text="Ulduz Restoran", bg="grey", fg="black", font=("Comic Sans MS", 20, "bold"))
text_label.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.1)
## Window penceresindeki User İD -ni və Password - un yazılış kodu
text_username = Label(frame_Beging, text="User ID", fg="black", font=("Comic Sans Ms", 25, "bold"))
text_username.place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.1)
text_password = Label(frame_Beging, text="Password", fg="black", font=("Comic Sans Ms", 25, "bold"))
text_password.place(relx=0.05, rely=0.3, relwidth=0.4, relheight=0.1)
## Window penceresindeki User İD və Password - un daxil edilməsi kodu
entry_username = Entry(frame_Beging, fg="black", bg="white", font=("Comic Sans MS", 20, "bold"))
entry_username.place(relx=0.5, rely=0.2, relwidth=0.4, relheight=0.08)
entry_password = Entry(frame_Beging, fg="black", bg="white", font=("Comic Sans MS", 20, "bold"), show="*")
entry_password.place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.08)
## Window penceresindeki User İD və Password - un daxil edilməsi zamanı yanlışlıq olanda cıxan kodu
labelbosluq = Label(frame_Beging, text="", fg="red", font=("Comic Sans Ms", 20, "bold"))
labelbosluq.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.1)

## daxil edilen mail ve parolu yoxlamaq funksiyasi
def yoxlanis():
    a = 1
    login_form()
    for i in range(len(alluser)):
        if entry_username.get() == alluser[i][2]:
            a = 0
            if entry_password.get() == alluser[i][3]:
                login_form()
            else:
                labelbosluq.config(text="Invalid Password")
    if a == 1:
        labelbosluq.config(text="Invalid email")

## passwordun gorunub gorunmemesi
check = True
def passwordShow():
    global check
    if check:
        entry_password.config(show="")
        logincheckButton.config(image=aciqPhoto)
        check = False
    else:
        check = True
        logincheckButton.config(image=bagliPhoto)
        entry_password.config(show="*")

## passwordun gorunub gorunmemesi buttonu
logincheckButton = Button(frame_Beging, image=bagliPhoto, text="*", command=passwordShow)
logincheckButton.place(relx=0.92, rely=0.315, relwidth=0.03, relheight=0.05)
## window penceresindeki login buttonu
btnLogin = Button(frame_Beging, image=loginPhoto, command=yoxlanis).place(relx=0.40, rely=0.45, relwidth=0.18, relheight=0.15)

window.mainloop()