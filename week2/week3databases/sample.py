with open("sample.txt", 'r') as f:
    data = f.read() 
data = data.replace(',0,' , ',FALSE,').replace(',1,' , ',TRUE,')
with open("fixed.txt", 'w') as f:
    f.write(data) 