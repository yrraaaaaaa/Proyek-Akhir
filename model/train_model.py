import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load data
url = 'https://raw.githubusercontent.com/yrraaaaaaa/Proyek-Akhir/main/data/data_bersih.csv'
df = pd.read_csv(url, sep=';')
df.columns = df.columns.str.strip().str.lower()

# Bersihkan dan normalisasi data
df = df[df['status'].isin(['Dropout', 'Graduate', 'Enrolled'])]
df = df[df['nationality'].isin(['Portuguese', 'Brazilian', 'Santomean'])]
df['status'] = df['status'].str.strip().str.capitalize()
df['nationality'] = df['nationality'].str.strip().str.capitalize()
df['course'] = df['course'].str.strip()
df['scholarship'] = df['scholarship'].str.strip().str.lower()
df['marital_status'] = df['marital_status'].str.strip().str.capitalize()

# Fitur dan label
X = df[['nationality', 'course', 'scholarship', 'marital_status']]
y = df['status']

# Label encoding
encoder_nat = LabelEncoder()
encoder_course = LabelEncoder()
encoder_sch = LabelEncoder()
encoder_marital = LabelEncoder()

X['nationality'] = encoder_nat.fit_transform(X['nationality'])
X['course'] = encoder_course.fit_transform(X['course'])
X['scholarship'] = encoder_sch.fit_transform(X['scholarship'])
X['marital_status'] = encoder_marital.fit_transform(X['marital_status'])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Train model
rf_model = RandomForestClassifier(
    criterion='entropy',
    max_depth=15,
    random_state=123,
    max_features='sqrt',
    n_estimators=500,
    n_jobs=-1
)
rf_model.fit(X_train, y_train)

# Evaluasi
y_pred = rf_model.predict(X_test)
print("Accuracy: {:.2f}%".format(accuracy_score(y_test, y_pred) * 100))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Simpan model dan encoder
import os
os.makedirs("model", exist_ok=True)

joblib.dump(rf_model, "model/rf_model.joblib")
joblib.dump(encoder_nat, "model/encoder_nat.joblib")
joblib.dump(encoder_course, "model/encoder_course.joblib")
joblib.dump(encoder_sch, "model/encoder_sch.joblib")
joblib.dump(encoder_marital, "model/encoder_marital.joblib")

print("Model dan encoder berhasil disimpan.")
