import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler 
import logging

logging.basicConfig(filename="Data_preprocessing.log", level=logging.INFO, format='%(asctime)s %(message)s',datefmt="%Y-%m-%d %H:%M:%S")

# Data preprocessing
logging.info("Data preprocessing started.........")
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/thyroid-disease/thyroid0387.data")
logging.info("Read the dataset successfully.")

df["target"] = df["-[840801013]"].str[0]
df.drop(columns="-[840801013]", inplace=True)

disease_list = ['S', 'F', 'A', 'R', 'I', 'M', 'N', 'G', 'K', 'L', 'Q', 'J', 'C', 'O', 'H', 'D', 'P', 'B', 'E']
df['target'].replace(to_replace=disease_list, value="yes", inplace=True)
df.target.replace({"-":0, "yes":1}, inplace=True)

df.rename(columns = {"29":"age", "F":"sex", "f":"thyroxine", "f.1":"query_thyroxine", "f.2":"medication","f.3":"sick", 
                        "f.4":"pregnant", "f.5":"surgery", "f.6":"I131_treatment", "t":"query_hypothyroid", 
                        "f.7":"query_hyperthyroid", "f.8":"lithium", "f.9":"goitre", "f.10":"tumor", "f.11":"hypopituitary", 
                        "f.12":"psych", "t.1":"TSH_measured","0.3":"TSH", "f.13":"T3_measured", "?":"T3", 
                        "f.14":"TT4_measured", "?.1":"TT4", "f.15":"T4U_measured", "?.2":"T4U", "f.16":"FTI_measured", 
                        "?.3":"FTI", "f.17":"TBG_measured", "?.4":"TBG", "other":"referral_source"}, inplace=True)

df.to_csv("data_processed.csv", index=False)
logging.info("Data Preprocessing complete.")

# Further preprocessing
df = pd.read_csv("data_processed.csv")
df.replace({"?":np.nan}, inplace=True)
df.drop(columns=["TBG", "T3"], inplace=True)
df.sex.fillna("unknown", inplace=True)
df.TSH = pd.to_numeric(df.TSH)
df.TT4 = pd.to_numeric(df.TT4)
df.T4U = pd.to_numeric(df.T4U)
df.FTI = pd.to_numeric(df.FTI)

index_age = df[df["age"]>100].index
df.drop(index_age, inplace=True)
index_tsh = df[df["TSH"]>15].index
df.drop(index_tsh, inplace=True)

df_dummy = pd.get_dummies(df)

imputer = KNNImputer(n_neighbors=3)
df_imputed = imputer.fit_transform(df_dummy)
df_final = pd.DataFrame(df_imputed, columns=df_dummy.columns)

validation_data = df_final[7000:]
x_train, x_test, y_train, y_test = train_test_split(df_final.drop(columns="target"), df_final["target"], test_size=0.2)

valid_imputed = imputer.transform(validation_data)
valid_final = pd.DataFrame(valid_imputed, columns=validation_data.columns)

ros = RandomOverSampler(random_state=42)
x_train, y_train = ros.fit_resample(x_train, y_train)
x_test, y_test = ros.fit_resample(x_test, y_test)
x_valid, y_valid = ros.fit_resample(valid_final.drop(columns="target"), valid_final["target"])

x_train.to_csv("x_train.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
x_test.to_csv("x_test.csv", index=False)
y_test.to_csv("y_test.csv", index=False)
x_valid.to_csv("x_valid.csv", index=False)
y_valid.to_csv("y_valid.csv", index=False)
logging.info("Data Preprocessing complete.")

