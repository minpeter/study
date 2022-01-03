import array

f = open("data.bin", "wb")

byte_arr = bytes([255,0, 127])

f.write(byte_arr)
f.close()

f = open("data.bin", "rb")

data = array.array("B")
data.fromfile(f, 3)

for item in data:
    print(item)
f.close()