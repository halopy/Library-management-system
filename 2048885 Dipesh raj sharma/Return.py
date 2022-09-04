import List
import dt
def returnBook():
    name=input("Enter name of borrower: ")
    a="Borrow-"+name+".txt"
    try:
        with open(a,"r") as f:
            line=f.readlines()
            line=[a.strip("$") for a in line]

        with open(a,"r") as f:
            data= f.read()
            print(data)
    except:
        print("The borrower name is incorrect")
        returnBook()
            
    b="Return-"+name+".txt"
    with open(b,"w+")as f:
        f.write("          Library Management system\n")
        f.write("              Returned By:"+name+"\n")
        f.write("  Date:"+dt.getDate()+"   Time:"+dt.getTime()+"\n\n")
        f.write("S.N\t\tBookname\t\tCost\n")

    total=0.0
    for i in range(3):
        if List.bookname[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+List.bookname[i]+"\t\t$"+List.cost[i]+"\n")
                List.quantity[i]=int(List.quantity[i])+1
                total+=float(List.cost[i])


    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat=input()
    if (stat.upper()=="Y"):
        print("By how many days was the book returned late?")
        day=int(input())
        fine=2*day
        with open(b,"a")as f:
            f.write("\t\t\t\t\tFine: $"+str(fine)+"\n")
        total=total+fine



    print("Final Total: "+"$"+str(total))
    with open(b,"a")as f:
        f.write("\t\t\t\t\tTotal: $"+ str(total))

    with open("stocks.txt","w+")as f:
        for i in range(3):
            f.write(List.bookname[i]+","+List.authorname[i]+","+str(List.quantity[i])+","+"$"+List.cost[i]+"\n")
