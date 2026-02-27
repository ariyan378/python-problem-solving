big_l = ['Be Quiet' for i in range(100)]

with open('big.txt',"w") as f:
    f.writelines(big_l)
with open('big.txt',"r") as f:
    chunk_size = 20

    while len(f.read(chunk_size))>0:
        print(f.read(chunk_size) , end=',')
        f.read(chunk_size)


        