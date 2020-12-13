from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
width=0.25
lang=('Python','C++','C#','Java','Koltin','JavaScript')
lang_hp=np.arange(len(lang))
users_2020=(190,100,100,200,50,250)
users_2019=(180,120,150,180,80,220)
users_2018=(170,110,120,190,100,250)
plt.bar(lang_hp + width ,users_2020,color='Red',label='2020',width=0.25)
plt.bar(lang_hp ,users_2019,color='Blue',label='2019',width=0.25)
plt.bar(lang_hp - width ,users_2018,color='Green',label='2019',width=0.25)
plt.xticks(ticks=lang_hp,labels=lang)
plt.xlabel('Programming Languages')
plt.ylabel('Users (Millions)')
plt.title('How Many users?')
plt.legend()
style.use('ggplot')
plt.show()  
