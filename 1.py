# # # import requests
  
# import numpy as np
# import  re 
# # # from bs4 import BeautifulSoup

# # resul1 = requests.get('https://market.todaypricerates.com/Andhra-Pradesh-vegetables-price')
# # resul2 = requests.get('https://market.todaypricerates.com/Andhra-Pradesh-fruits-price')



# # soup1 = BeautifulSoup(resul1.content,'html.parser')
# # soup2 = BeautifulSoup(resul2.content,'html.parser')

# # table1 = soup1.find(class_ = "Table").get_text()
# # table2 = soup2.find(class_ = "Table").get_text()


# # with open("vege.txt",'w',encoding = 'utf-8') as f:
# #     f.write(table1.strip())
# #     f.close()

# # with open("frui.txt",'w',encoding = 'utf-8') as f:
# #     f.write(table2.strip())
# #     f.close()
# a = "user/documents/"
# f1 = open('vege.txt')
# a1 = f1.readlines()

# f2 = open('frui.txt')
# a2 = f2.readlines()


# result1 = []
# result2 = []

# for i in range(len(a1)):
#     if(a1[i] != '\n' and a1[i] != 'Kg / Pcs\n'):
#         result1.append(a1[i])

# for i in range(len(a2)):
#     if(a2[i] != '\n' and a2[i] != 'Kg / Pcs\n'):
#         result2.append(a2[i])
    

# fruits = []
# i = 5
    
# while(i<len(result1)):
#     fruits.append(result1[i:i+4])
#     i+=4


# j= 5
# while(j<len(result2)):
#     fruits.append(result2[j:j+4])
#     j+=4

# for i in fruits:
#     u = len(i[0])
#     i[0] = i[0][:u-1]
#     x = len(i[1])
#     i[1] = i[1][5:x-1]
#     y = len(i[2])
#     i[2] = i[2][5:y-1]
#     z = len(i[3])
#     i[3] = i[3][5:z-1]


# fruits = np.array(fruits)
# eq = '[0-9][0-9]*'

# range = []
# for i in  fruits[:,2]:
#     range.append(re.findall(eq,i))

# fruit = zip(fruits[:,0],range)


# print(int(range[3][0])+ int(range[3][0])*0.2)


# from playsound import playsound

# a = 'C:/Users/user/Downloads/master'
# playsound(a)


# a  = ['priyaarul@gmail.com', 'rocklohithreddy@gmail.com', 'priyaarul@gmail.com']
# b = [1,2,3]
# c = ['a','b','c']
# d = []
# for i,j,k in zip(a,b,c):
#     print(i)
#     print(j)
#     print(k)
#     d.append((i,j,k))

# print(d)

# class Train:
#     def __init__(self,name,fare,ticket):
#         self.name=name
#         self.fare=fare
#         self.ticket=ticket

#     def bookticket(self):
#         if self.ticket>0:
#             print(self.ticket)
#             print(f"your ticket is confirmed, number is {self.ticket}")
            
#             ticket_list.remove(self.ticket)
#             self.ticket=self.ticket-1
#         else:
#             print("Sorry, this train is full. Kindly try tatkal")

#     def getstatus(self):
#         print(f"Name of the train is {self.name},NO. of seats available is {self.ticket} and the fare per ticket is {self.fare}")
   
#     def getinfo(self):
#         print(f"The fare of ticket per head is Rs. {self.fare}")
   
#     def cancelticket(self,c):
#         self.cancel=c
#         ticket_list.append(self.cancel)
#         self.ticket=self.ticket+1

# ticket_list=[*range(1,21)]
# passenger=Train("Rajdhani Express",45,20)
# passenger.getinfo()
# print(ticket_list)

# passenger.bookticket()
# passenger.getstatus()
# print(ticket_list)
# passenger.bookticket()
# passenger.getstatus()

# print(ticket_list)



# passenger.bookticket()
# passenger.getstatus()

# print(ticket_list)

# passenger.bookticket()
# passenger.getstatus()

# c=int(input("Enter ticket number you want to cancel: "))
# passenger.cancelticket(c)
# print(ticket_list)



a = "https://bluedart.com/tracking"

print(a)