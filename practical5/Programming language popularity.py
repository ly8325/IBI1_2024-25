#create a dictionary to	record the	data
popularity={'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5}
import matplotlib.pyplot as plt
#list the categories and values
language=['JavaScript','HTML','Python','SQL','TypeScript']
users=[62.3,52.9,51,51,38.5]
#create a bar plot
plt.bar(language,users,color='black')
#add a title and labels for x and y
plt.title('Programming Language Popularity')
plt.xlabel('language')
plt.ylabel('popularity/%')
#print the bar plot
plt.show()
#
language=input('A programming language')
if language in popularity:
    users=popularity[language]
    print('The percentage is '+str(users)+'%')
else:
    print('No data available for the language')