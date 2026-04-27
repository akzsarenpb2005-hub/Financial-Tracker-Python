import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fin=pd.read_csv('Financial Tracker.csv')
ex=pd.read_csv('Live Exchange Rates.csv')

x=0

while x<fin['Amount'].count():
    sp=(fin.loc[x,'Amount'].split())
    y=0
    while y<ex['Code'].count():
        if (ex.loc[y,'Code'])==sp[1]:
            z=(float(sp[0])*float(ex.loc[y,'LKR']))
            zz=str(z)
            fin.loc[x,'Amount']=zz
        y=y+1
    x=x+1
   
fin['Amount']=fin['Amount'].str.split().str[0].astype(float)
group1=(fin.groupby('Category')['Amount'].sum())
new1=group1.reset_index()
print(new1)
num=(fin['Amount'])
py=num.to_numpy()
print(f'Avarege Monthly Sell :{np.mean(py)}')
reven=float(input("Enter you're Monthly Revenue :\n"))
sum=(np.sum(py))
if sum>reven:
    print(f'You are spending more than your monthly revenue. You should reduce your unnecessary expenses \n Non Important sell \n{new1.loc[1]}')
    print(f'Because you made unnecessary expenses ypu have incurred a loss of {float(sum-reven)}LKR')
else:
    print(f'You get profit {float(reven-sum)}LKR')
group=(fin.groupby('Description')['Amount'].sum())
new=group.reset_index()
pi=(new['Amount']/sum*100)

plt.bar(new['Description'],new['Amount'])
plt.xticks(rotation=90)
plt.show()
    
