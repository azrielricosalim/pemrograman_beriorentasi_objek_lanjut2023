list = [1, 2, 3]
try:
    value = list[10]
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")