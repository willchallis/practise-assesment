import datetime
today=datetime.datetime.now()





def breads():
        global breadtype,breadlist
        breadlist = ["White","Brown","Italian","Granary"]
        breadcount = 0
        print("We have the following breads")
        while breadcount < 4:
                print(breadcount,"  ",breadlist[breadcount])
                breadcount = breadcount + 1
        breadtype = int(input("What number bread do you want"))

def cheeses():
        global cheesetype,cheeselist
        cheeselist = ["Swiss","Feta","Brie","Tasty"]
        cheesecount = 0
        print("We have the following cheeses")
        while cheesecount < 4:
                print(cheesecount,"  ",cheeselist[cheesecount])
                cheesecount = cheesecount + 1
        cheesetype = int(input("What number cheese do you want"))

def meats():
        global meattype,meatlist
        meatlist = ["Chicken","Turkey","Tuna","Bacon"]
        meatcount = 0
        print("We have the following meats")
        while meatcount < 4:
                print(meatcount,"  ",meatlist[meatcount])
                meatcount = meatcount + 1
        meattype = int(input("What number meat do you want"))

def salads():
        global saladtype,saladlist,saladswanted
        saladlist = ["Lettuce","Tomato","Carrot","Cucumber","Onions"]
        saladcount = 0
        print("We have the following salads, you can pick as many as you want")
        while saladcount < 5:
                print(saladcount,"  ",saladlist[saladcount])
                saladcount = saladcount + 1
        print("Press enter when you have finished choosing your salads")
        saladswanted = ""
        saladtype = " "
        while saladtype != "":
                saladtype = input("What number salad do you want ")
                if saladtype != "":
                        saladtype = int(saladtype)
                        saladswanted = saladswanted + " " + saladlist[saladtype]



def dressingss():
        global dressingstype,dressingslist
        dressingslist = ["BBQ sauce","Ranch dressing","Mayo","No sauce"]
        dressingscount = 0
        print("We have the following dressings")
        while dressingscount < 4:
                print(dressingscount,"  ",dressingslist[dressingscount])
                dressingscount = dressingscount + 1
        dressingstype = int(input("What number dressing do you want"))

def output_order():
        breadorder = [] #empty list
#this adds the persons entire order details to the list
        breadorder.append(first_name)
        breadorder.append(cellphone)
        breadorder.append(breadlist[breadtype])
        breadorder.append(meatlist[meattype])
        breadorder.append(cheeselist[cheesetype])
        breadorder.append(saladswanted)
        breadorder.append(dressingslist[dressingstype])
        breadorder.append(today)
        outputfile = open("sams_orders.text","a")#opens text file
        print("******** Order for {} - {}******".format(first_name,cellphone))#test print to pyscripter
        outputfile.write("******** Order for {} - {}******".format(first_name,cellphone))
        for order in breadorder:
                print(order)
                outputfile.write("{}\n".format(order))
        outputfile.write("******** End of order: {}.******".format(today))
        print("******** End of order: {}.******".format(today))
        outputfile.close() #closes the text file
        




        
#main program that makes calls to other functions
first_name = str(input("What is your first name")).title
cellphone = str(input("What is your cellphone number"))
breads()
cheeses()
meats()
salads()
dressingss()
output_order()


