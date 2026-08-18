import joblib
import pandas as pd
 
# Ucitaj sacuvani model
model = joblib.load("model/product_category_model.pkl")
 
print("Model uspešno učitan!")
print("Napiši 'izlaz' ako želiš da program prestane sa radom.\n")
 
while True:
    title = input("Unesi naziv proizvoda: ")
    if title.lower() == "izlaz":
        print("Izlaz iz programa...")
        break
 
    # Odredi ključne reči
    keywords = ['frost', 'fridge', 'cm', 'litre', 'sim', 'galaxy', 'iphone', 'handy', 'phone', 'smartphone', 'xperia', 'android', 'kg', 'spin', 'rpm', 'ghz', 'inch', 'led', 'hd', 'hdr', '4k', 'dish', 'mp', 'zoom', 'mm', 'oven', 'wave']
    
    def pronadji_kljucne_reci(naslov):
        naslov_mali = str(naslov).lower()
        pronadjene_reci = []
        for rec in keywords:
            if rec in naslov_mali:
                pronadjene_reci.append(rec) # Ako reč postoji u naslovu, ubaci je u listu
        return pronadjene_reci
    
    keywords = " ".join(pronadji_kljucne_reci(title))
 
    # Create a DataFrame from input
    user_input = pd.DataFrame([{
        "Product Title": title,
        "Keywords": keywords
    }])
 
    # Predict product category
    prediction = model.predict(user_input)[0]
    print(f" Prognozirana kategorija proizvoda: {prediction}\n" + "-" * 40)
    
    #Nakon ručnog unosa naziva proizvoda predloženih u tekstu zadatka, konstatovano je:
    # Model je pogrešio u prognozi kategorije dva proizvoda: kenwood k20mss15 solo (prognozirao je washing machines umesto microwaves) i smeg sbs8004po (prognozirao je fridges umesto Fridge Freezers)