#Dictionary

mydict={"Name":"Ashish Rajan",
        "Age":27,
        "year":1996}

print(mydict)

#length

mydict={"Name":"Ashish Rajan",
        "Age":27,
        "year":1996}
print(len(mydict))

#Type function

mydict={"Name":"Ashish Rajan",
        "Age":27,
        "year":1996}
print(type(mydict))

#empty dictionary

mydict={}
print(mydict)

#accesing element

mydict={"Name":"Ashish Rajan",
        "Age":27,
        "year":1996}
print(mydict["Name"])

#for loop for keys
mydict={"Name":"Ashish Rajan",
        "Age":27,
        "year":1996}
for x in mydict:
    print(x)

#clear function
    mydict={"Name":"Ashish Rajan",
        "Age":27,
        "year":1996}
    mydict.clear()
    print(mydict)

#for loop for values
mydict={"Name":"Ashish Rajan",
        "Age":27,
        "year":1996}
for x in mydict.values():
    print(x)

#copy

    mydict={"Name":"Ashish Rajan",
        "Age":27,
        "year":1996}
    mydict1=mydict.copy()
    print(mydict1)

#pop()

    mydict={"Name":"Ashish Rajan",
        "Age":27,
        "year":1996}
    print(mydict.pop("Age"))

#pop item()

    mydict={"Name":"Ashish Rajan",
        "Age":27,
        "year":1996}
    x=mydict.popitem()
    print(x)

        
