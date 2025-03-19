#create two lists of sorted	values with the given data
uk_countries=[57.11,3.13,1.91,5.45]
china_province=[65.77,41.88,45.28,61.27,85.15]
#print the lists
print(uk_countries)
print(china_province)
import matplotlib.pyplot as plt
#create a pie plot of UK countries
labels=['England','Wales','Northern Ireland','Scotland']
explode=[0.1,0,0,0]
colors=['blue','red','green','yellow']
plt.pie(uk_countries,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%', startangle=80)
#add a title
plt.title('The distribution of population sizes separately in UK countries')
#print the plot
plt.show()
#create a pie plot of Zhejiang-neighbouring	provinces
labels=['Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu']
explode=[0.1,0,0,0,0]
colors=['blue','red','green','yellow','purple']
plt.pie(china_province,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%', startangle=80)
#add a title
plt.title('The distribution	of population sizes separately in Zhejiang-neighbouring	provinces')
#print the plot
plt.show()