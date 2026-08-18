import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report


url = "https://raw.githubusercontent.com/beexy86-rgb/predikcija_kategorije_proizvoda/main/products.csv"
df = pd.read_csv(url)

df.rename(columns={' Category Label': 'Category Label', '_Product Code': 'Product Code', ' Listing Date  ': 'Listing Date'}, inplace=True)

#Uklanjanje redova u kojima nedostaje vrednost u koloni Product Title ili Category Label
df.dropna(subset=['Product Title', 'Category Label'], inplace=True)

#Konvertovanje vrednosti u koloni Product Title u string
df['Product Title'] = df['Product Title'].astype(str)

#Standardizacija vrednosti u koloni Category Label i konvertovanje u category tip podataka
df['Category Label'] = df['Category Label'].astype(str).str.lower().str.strip()

df['Category Label'] = df['Category Label'].replace('mobile phone', 'mobile phones')
df['Category Label'] = df['Category Label'].replace('cpu', 'cpus')
df['Category Label'] = df['Category Label'].replace('fridge', 'fridges')

df['Category Label'] = df['Category Label'].astype('category')

#Provera duplikata
duplikati = df[df.duplicated(subset=['Product Title', 'Category Label'], keep=False)]
df_cleaned = df.drop_duplicates(subset=['Product Title', 'Category Label'], keep='first')

df_filtered = df_cleaned.drop(columns=['product ID', 'Merchant ID', 'Product Code', 'Number_of_Views', 'Merchant Rating', 'Listing Date'])

keywords = ['frost', 'fridge', 'cm', 'litre', 'sim', 'galaxy', 'iphone', 'handy', 'phone', 'smartphone', 'xperia', 'android', 'kg', 'spin', 'rpm', 'ghz', 'inch', 'led', 'hd', 'hdr', '4k', 'dish', 'mp', 'zoom', 'mm', 'oven', 'wave']

#Funkcija za pronalaženje ključnih reči
def pronadji_kljucne_reci(naslov):
    naslov_mali = str(naslov).lower()
    pronadjene_reci = []
    for rec in keywords:
        if rec in naslov_mali:
            pronadjene_reci.append(rec) # Ako reč postoji u naslovu, ubaci je u listu
    return pronadjene_reci

#Primena funkcije na kolonu
df_filtered['Keywords'] = df_filtered['Product Title'].apply(pronadji_kljucne_reci).apply(lambda x: " ".join(x))

# Podela podataka
X = df_filtered[["Product Title", "Keywords"]]
y = df_filtered["Category Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Preprocessor: TF-IDF for text, MinMaxScaler for numeric feature
preprocessor = ColumnTransformer(transformers=[
    ("title", TfidfVectorizer(), "Product Title"),
    ("keywords", TfidfVectorizer(), "Keywords")
])


pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("classifier", LinearSVC())])
    
# Treniranje modela sa celim skupom podataka
pipeline.fit(X, y)

# Snimanje modela u fajl
import joblib
joblib.dump(pipeline, "model/product_category_model.pkl")

print(" Model je treniran i sačuvan kao 'product_category_model.pkl'")