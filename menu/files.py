def read(figura):
    ar1 =[]
    with open("./knowlege_base/"+figura, "r", encoding="utf-8") as f:
        
        for line in f: 
            array = line.split("|")
            ficha =[]
            for part in array:

                pair = part.split(",")
                
                #print("----")
                #print(pair[1])
                out= [pair[0],pair[1].replace("\n","")]
                ficha.append(out)
            ar1.append(ficha)
        #print(ar1)
    return ar1


def write(figura, text):
    with open("./knowlege_base/"+figura, "a", encoding="utf-8") as f:
        f.write(text)
        f.write("\n")
        
    pass

def run():
    read()

if __name__ == '__main__':
    run()