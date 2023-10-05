import pandas as pd
import psycopg2
import seaborn as sns
import matplotlib.pyplot as plt


# conn = psycopg2.connect(user='postgres', password='Dekingumas123*', host='localhost', port=5432, database='ButaiProducts')
# cur = conn.cursor()
# cur.execute("SELECT *FROM butai")
# Butu_sarasas=cur.fetchall()
#
# df=pd.DataFrame(Butu_sarasas, columns = ['id', 'adresas', 'kambariu_sk', 'plotas', 'aukstas', 'kaina', 'kv_kaina'])
# print(df)
#
# grupavimas=df.groupby('adresas')['kaina'].mean()
# print(grupavimas)
#
#
# plt.figure(figsize=(8,5))
# sns.set(style='darkgrid')
# sns.barplot(x=grupavimas.index, y=grupavimas.values)
# plt.xticks(rotation = 8)
# plt.xlabel('Vidutinė kaina')
# plt.ylabel('Kainos vidurkis')
# plt.title('Atvirų būstų kainos vidurkis pagal miestus ir jų gatves')
# plt.show()







