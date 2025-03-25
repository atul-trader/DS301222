import array as arr

# datatype,list of elements
data = arr.array('i',[4,5,2,5,7,3])
print(data)

fdata = arr.array('d',[6.8,54.5,9.7,9])
print(fdata)

fdata.append(87.9)
print(fdata)

fdata.extend([7.8,6.5,43.5])
print(fdata)

fdata.pop()
print(fdata)
