#create a function to calculate the volume of drug
def volume(weight,strenth):
    #report an error if the supplied weight is outwith the expected range
    if weight>100 or weight<10:
        return "the supplied weight is outwith the expected range"
    #report an error if the paracetamol strength does not match an expected concentration
    elif strenth!=120 and strenth!=250:
        return "the paracetamol strength does not match an expected concentration"
    #calculate the volume of drug
    else:
        volume=15*weight/strenth*5
        return volume
#an example of using the function
weight=float(input("the weight (in kg) of the child"))
strenth=float(input("the weight (in mg) of paracetamol in 5 mL"))
print(volume(weight,strenth))