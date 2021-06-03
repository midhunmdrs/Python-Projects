import array as arr  # ( from array import * )

vals = arr.array('i', [3, 4, 6, 7, 8])
print(vals.buffer_info())

for i in range(5):  # prints by refering index number
    print(vals[i], i)

for e in vals:  # prints by referring values
    print(e)

print()
print()

new_arr = arr.array(vals.typecode, (a**a for a in vals))
for d in new_arr:
     print(d)