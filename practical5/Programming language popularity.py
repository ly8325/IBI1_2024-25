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
#create a variable called language to store the input language
language=input('A programming language')
#test if the language is in the dictionary
if language in popularity:
#attain the value from the dictionary
    users=popularity[language]
#print the value
    print('The percentage is '+str(users)+'%')
else:
    print('No data available for the language')