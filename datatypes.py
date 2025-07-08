
values = [1,2,"Aditya",4,5]
print(values[0]) #1
print(values[4])#4
print(values[-1])#5
print(values[1:3]) #[2, 'Aditya']

values.insert(3,"joshi")#[1, 2, 'Aditya', 'joshi', 4, 5]
print(values)

values.append("End") #[1, 2, 'Aditya', 'joshi', 4, 5, 'End']
print(values)

values[2]= "aditya"#[1, 2, 'aditya', 'joshi', 4, 5, 'End']
print(values)

del values[0]
print(values)
print("**********************")

# tuple
val =(1, 2, 3, 'Aditya', 4.5)

print(val[1])

#dictonary

dic = {"a": 2, 4: "abc", "c": "Hello world"}
print(dic[4])
print(dic["c"])
print("**********************")

dict={}

dict["Firstname"]= "Aditya"
dict["Lastname "]= "Joshi"
dict["Gender"] ="male"
print(dict)
