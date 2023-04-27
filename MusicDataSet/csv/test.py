with open ("Beyonce.txt") as f:
    for i,line in enumerate(f):
        with open(f"{i+120}.txt","w")as g:
            g.write(line)
