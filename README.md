# predikcija_kategorije_proizvoda
U ovom repozitorijumu su svi fajlovi za treniranje, testiranje i eksploataciju modela koji predviđa kategoriju proizvoda na osnovu ulaznih podataka u vidu naziva proizvoda i drugih.

# Svrha

Ovaj repozitorijum kreiran je u svrhu izrade zadatka "Predikcija kategorije proizvoda na osnovu naslova". 
Repozitorijum je javan.

#Struktura projekta

Fajl products.csv predstavlja početni izvor podataka o proizvodima. 

U folderu notebooks nalazi se jupyter notebook u kome je urađeno: 
    
    pretprocesiranje podataka (brisanje nedostajućih vrednosti, duplikata, konvertovanje podataka u odgovarajući tip i sl.)

    treniranje i testiranje pet različitih modela i sagledavanje njihovih metrika i

    odabir najboljeg modela.

U fajlu train_model.py odabrani model je testiran na celom skupu podataka i sačuvan kao pkl fajl. Nije komitovan na GitHub.

U fajlu predict_category.py napisan je kod za korisnika koji želi da testira model unosom naziva proizvoda. Program se prekida upisivanjem reči "izlaz".

Ako želite samo da testirate model, pokrenite kod u fajlu predict_category.py.

Ako želite da detaljno sagledate proces koji je doveo do odabira i čuvanja modela, na raspolaganju su Vam svi potrebni fajlovi opisani u strukturi projekta.

