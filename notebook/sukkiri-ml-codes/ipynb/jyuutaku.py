import pandas as pd
import pickle
 
rm = float(input("部屋数:"))
lstat = float(input("低所得者割合(1～30):"))
ptratio = float(input("１教師あたりの生徒数(10～20):"))
 
with open('boston.pkl', "rb") as f:
    model2 = pickle.load(f)
 
with open('boston_scx.pkl', "rb") as f:
    sc_model_x3 = pickle.load(f)
 
with open('boston_scy.pkl', "rb") as f:
    sc_model_y3 = pickle.load(f)
 
mydf = pd.DataFrame({'RM':[rm],'LSTAT':[lstat],'PTRATIO':[ptratio]})
mydf['RM2'] = mydf['RM'] ** 2
mydf['LSTAT2'] = mydf['LSTAT'] ** 2
mydf['PTRATIO2'] = mydf['PTRATIO'] ** 2
mydf['RM * LSTAT'] =mydf['RM'] * mydf['LSTAT']
 
myhouse = sc_model_x3.transform(mydf)
prd = model2.predict(myhouse)
print("予想住宅価格: ${},000".format(int(sc_model_y3.inverse_transform(prd))))
