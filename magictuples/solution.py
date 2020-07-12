def magic_tuples(tsum, tmax):
    return ( (x, tsum - x) 
    for x in range(  tsum - tmax +1 , tmax))

if __name__ == "__main__":
    print(list(magic_tuples(500, 255)))
