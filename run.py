import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import time

temp = 'Y'
password = 'eCommerceProject'
data = pd.read_csv('Train.csv')
sum = 1
while sum!=0:
    data['Customer_rating'] = data['Customer_rating'].fillna(method = 'ffill')
    data['Customer_rating'] = data['Customer_rating'].fillna(method = 'bfill')
    sum = data['Customer_rating'].isnull().sum()
print("How do you want to use this system?\nEnter:\n1 to use as Customer\n2 to use as Company Administrator")
choice = int(input("Your Choice:"))
if choice == 2:
    while temp == 'Y':
        key = input("Enter Password:")
        if key == password:
            os.system('cls')
            print("Login Successful!\n")
            time.sleep(3)
            while temp == 'Y':
                os.system('cls')
                print("Enter your choice!\n1. Firm Analysis\n2. Customer Gender Analysis\n3. Product Analysis\n4. Seller Analysis\n5. Data Visualization")
                c = int(input("Your Choice:"))
                os.system('cls')
                if c == 1:
                    print("\n\n********** FIRM ANALYSIS **********\n\n")
                    ware = data.Warehouse_Block.unique()
                    ware.sort()
                    warehouse = []
                    rat = []
                    for i in range(0, len(ware)):
                        warehouse.append(data[data.Warehouse_Block == ware[i]])
                        rat.append(warehouse[i].Customer_rating.mean() + warehouse[i].On_time_delivery.sum() / 1000)
                    high = ware[0]
                    maxrat = rat[0]
                    for i in range(1, len(rat)):
                        if rat[i] > maxrat:
                            maxrat = rat[i]
                            high = ware[i]
                    print("Best Performing Warehouse Block:", high)

                    sellers = data.Seller_Name.unique()
                    seller = []  # List of separate dataframes of different sellers.
                    rat = []
                    for i in range(0, len(sellers)):
                        seller.append(data[data.Seller_Name == sellers[i]])
                        rat.append(seller[i].Customer_rating.mean() + seller[i].On_time_delivery.sum() / 1000)
                    high = sellers[0]
                    maxrat = rat[0]
                    for i in range(1, len(rat)):
                        if rat[i] > maxrat:
                            maxrat = rat[i]
                            high = sellers[i]
                    print("Best Seller:", high)

                    ship = data.Mode_of_Shipment.unique()
                    shipment = []
                    rat = []
                    for i in range(0, len(ship)):
                        shipment.append(data[data.Mode_of_Shipment == ship[i]])
                        rat.append(shipment[i].Customer_rating.mean() + shipment[i].On_time_delivery.sum() / 1000)
                    high = ship[0]
                    maxrat = rat[0]
                    for i in range(1, len(rat)):
                        if rat[i] > maxrat:
                            maxrat = rat[i]
                            high = ship[i]
                    print("Best Mode of Shipment:", high)

                    prod = data.Product_ID.unique()
                    product = []  # List of separate dataframes of different products.
                    rat = []
                    for i in range(0, len(prod)):
                        product.append(data[data.Product_ID == prod[i]])
                        rat.append(product[i].Customer_rating.mean() + product[i].On_time_delivery.sum() / 1000)
                    high = prod[0]
                    maxrat = rat[0]
                    for i in range(1, len(rat)):
                        if rat[i] > maxrat:
                            maxrat = rat[i]
                            high = prod[i]
                    print("Best Performing Product: Product_ID", high)

                    print("Total Revenue Generated:", data.Cost_of_the_Product.sum())
                    print("Total Number of Products:", data.Product_ID.nunique())


                elif c == 2:
                    print("\n\n********** CUSTOMER GENDER ANALYSIS **********\n\n")
                    male = data[data.Gender == 'M']
                    female = data[data.Gender == 'F']
                    print("Male Customers:", len(male), "\nFemale Customers:", len(female))

                    mcall = male.Customer_care_calls.sum()
                    fcall = female.Customer_care_calls.sum()
                    print("\nMale Customer Care Calls:", int(mcall))
                    print("Female Customer Care Calls:", int(fcall))
                    if mcall > fcall:
                        print("Male Customers make more customer care calls!")
                    elif mcall < fcall:
                        print("Female Customers make more customer care calls!")
                    else:
                        print("Both call equally!")

                    mrat = male.Customer_rating.mean()
                    frat = female.Customer_rating.mean()
                    print("\nMale Customer Average Rating:", mrat, "\nFemale Customer Average Rating:", frat)
                    if mrat > frat:
                        print("Male Customers give more Ratings!")
                    elif mrat < frat:
                        print("Female Customers give more Ratings!")
                    else:
                        print("Both rate products equally!")

                    mdisc = male.Discount_Offered.mean()
                    fdisc = female.Discount_Offered.mean()
                    print()
                    if mdisc > fdisc:
                        print("Male Customers go for higher discounts!")
                    elif mdisc < fdisc:
                        print("Female Customers go for higher discounts!")
                    else:
                        print("There is no correlation between Gender and Discount Preference!")

                elif c == 3:
                    print("\n\n********** PRODUCT ANALYSIS **********\n\n")
                    pid = int(input("Enter a valid Product ID:"))
                    if pid in data.Product_ID.unique():
                        p = data[data.Product_ID == pid]
                        print("\nAverage Product Rating:", p.Customer_rating.mean())
                        print("Revenue Generated:", p.Cost_of_the_Product.sum())
                        sellers = p.Seller_Name.unique()
                        seller = []  # List of separate dataframes of different sellers.
                        rat = []
                        for i in range(0, len(sellers)):
                            seller.append(p[p.Seller_Name == sellers[i]])
                            rat.append(seller[i].Customer_rating.mean() + seller[i].On_time_delivery.sum() / 1000)
                        high = sellers[0]
                        maxrat = rat[0]
                        for i in range(1, len(rat)):
                            if rat[i] > maxrat:
                                maxrat = rat[i]
                                high = sellers[i]
                        print("Best Seller:", high)
                        print("\n-------------------Product Record-------------------\n\n", p)
                    else:
                        print("404: Product Not Found!")

                elif c == 4:
                    print("\n\n********** SELLER ANALYSIS **********\n\n")
                    sname = input("Enter a valid Seller Name:")
                    if sname in data.Seller_Name.unique():
                        s = data[data.Seller_Name == sname]
                        print("\nAverage Seller Rating:", s.Customer_rating.mean())
                        print("Revenue Generated:", s.Cost_of_the_Product.sum())
                        prod = s.Product_ID.unique()
                        product = []  # List of separate dataframes of different sellers.
                        rat = []
                        for i in range(0, len(prod)):
                            product.append(s[s.Product_ID == prod[i]])
                            rat.append(product[i].Customer_rating.mean() + product[i].On_time_delivery.sum() / 1000)
                        high = prod[0]
                        maxrat = rat[0]
                        for i in range(1, len(rat)):
                            if rat[i] > maxrat:
                                maxrat = rat[i]
                                high = prod[i]
                        print("Best Product: Product_ID", high)
                        print("\n-------------------Seller Record-------------------\n\n", s)
                    else:
                        print("404: Seller Not Found!")
                elif c ==5:
                    print("\n\n********** DATA VISUALIZATION **********\n\n")
                    print("1. Bar Charts\n\n2. Pie Charts\n\n")
                    chart = int(input("Your Choice:"))
                    os.system("cls")
                    
                    ware = data.Warehouse_Block.unique()
                    ware.sort()
                    warehouse = []
                    rat = []
                    for i in range(0, len(ware)):
                        warehouse.append(data[data.Warehouse_Block == ware[i]])
                    
                    sellers = data.Seller_Name.unique()
                    seller = []  # List of separate dataframes of different sellers.
                    for i in range(0, len(sellers)):
                        seller.append(data[data.Seller_Name == sellers[i]])
                        
                    male = data[data.Gender == 'M']
                    female = data[data.Gender == 'F']
                    r = [1,2,3,4,5]
                    if chart == 1:
                        print("********** BAR CHARTS **********\n\n")
                        print("1. Warehouse Wise Order-Rating Chart.\n2. Warehouse-Rating Chart\n3. Product Count-Warehouse Chart\n4. Warehouse-Revenue Chart\n5. Gender-Rating Chart\n6. Seller Wise Order Count-Rating Chart\n7. Seller-Rating Chart\n8. Seller-Revenue Chart\n9. Order Count-Rating Chart\n10. Male-Female Customers.")
                        fig = int(input("Enter Your Choice:"))
                        os.system('cls')
                        if fig == 1:
                            
                            w = input("Enter Warehouse Block:")
                            if w in ware:
                                wdata = data[data.Warehouse_Block == w]
                                prods = []
                                for i in range(len(r)):
                                    prods.append(wdata[wdata.Customer_rating == r[i]])
                                counts = []
                                for i in range(len(prods)):
                                    counts.append(prods[i].Order_ID.count())
                                plt.barh(r,counts)
                                plt.xlabel("Order Count")
                                plt.ylabel("Rating")
                                for index, value in enumerate(counts):
                                    plt.text(value, index+1,str(value))
                                plt.grid(True)
                                plt.show()
                            else:
                                print("404: Warehouse Not Found!")
                        
                        elif fig == 2:
                            for i in range(0, len(ware)):
                                rat.append(warehouse[i].Customer_rating.mean() + warehouse[i].On_time_delivery.sum() / 1000)   
                            plt.barh(ware,rat)
                            plt.ylabel("Warehouse Block")
                            plt.xlabel("Average Rating")
                            for index, value in enumerate(rat):
                                plt.text(value, index,str(value))
                            plt.grid(True)
                            plt.show()
                        
                        elif fig == 3:
                            counts = []
                            for i in range(len(warehouse)):
                                counts.append(warehouse[i].Product_ID.nunique())
                            plt.barh(ware,counts)
                            plt.ylabel("Warehouse Block")
                            plt.xlabel("Product Count")
                            for index, value in enumerate(counts):
                                plt.text(value, index,str(value))
                            plt.grid(True)
                            plt.show()
                            
                        elif fig == 4:
                            rev = []
                            for i in range(len(warehouse)):
                                rev.append(warehouse[i].Cost_of_the_Product.sum())
                            plt.barh(ware,rev)
                            plt.ylabel("Warehouse Block")
                            plt.xlabel("Revenue Generated (in Rs.)")
                            for index, value in enumerate(rev):
                                plt.text(value, index,str(value))
                            plt.grid(True)
                            plt.show()
                            
                        elif fig == 5:
                            ratings = data.Customer_rating.unique()
                            ratings.sort()
                            ma = []
                            fe = []
                            for i in range(len(ratings)):
                                ma.append(male[male.Customer_rating == ratings[i]].Order_ID.count())
                                fe.append(female[female.Customer_rating == ratings[i]].Order_ID.count())
                            X = np.arange(len(ratings))


                            plt.bar(X - 0.2, fe, 0.4, label = 'Female')
                            plt.bar(X + 0.2, ma, 0.4, label = 'Male')


                            plt.xticks(X, ratings)
                            plt.xlabel("Rating")
                            plt.ylabel("Rating Count")
                            plt.legend()
                            plt.grid(True)
                            plt.show()
                            
                        elif fig ==6:
                            se = input("Enter Seller Name:")
                            if se in sellers:
                                sdata = data[data.Seller_Name == se]
                                prods = []
                                for i in range(len(r)):
                                    prods.append(sdata[sdata.Customer_rating == r[i]])
                                counts = []
                                for i in range(len(prods)):
                                    counts.append(prods[i].Order_ID.count())
                                plt.barh(r,counts)
                                plt.xlabel("Order Count")
                                plt.ylabel("Rating")
                                for index, value in enumerate(counts):
                                    plt.text(value, index+1,str(value))
                                plt.grid(True)
                                plt.show()
                            else:
                                print("404: Seller Not Found!")
                                
                        elif fig == 7:
                            for i in range(0, len(sellers)):
                                rat.append(seller[i].Customer_rating.mean() + seller[i].On_time_delivery.sum() / 1000)   
                            plt.barh(sellers,rat)
                            plt.ylabel("Seller Name")
                            plt.xlabel("Average Rating")
                            for index, value in enumerate(rat):
                                plt.text(value, index,str(value))
                            plt.grid(True)
                            plt.show()
                            
                        elif fig == 8:
                            rev = []
                            for i in range(len(seller)):
                                rev.append(seller[i].Cost_of_the_Product.sum())
                            plt.barh(sellers,rev)
                            plt.ylabel("Seller Name")
                            plt.xlabel("Revenue Generated (in Rs.)")
                            for index, value in enumerate(rev):
                                plt.text(value, index,str(value))
                            plt.grid(True)
                            plt.show()
                            
                        elif fig == 9:
                            prods = []
                            for i in range(len(r)):
                                prods.append(data[data.Customer_rating == r[i]])
                            counts = []
                            for i in range(len(prods)):
                                counts.append(prods[i].Order_ID.count())
                            plt.barh(r,counts)
                            plt.xlabel("Order Count")
                            plt.ylabel("Rating")
                            for index, value in enumerate(counts):
                                plt.text(value, index+1,str(value))
                            plt.grid(True)
                            plt.show()
                            
                        elif fig == 10:
                            gender = ['M','F']
                            counts = []
                            for i in range(len(gender)):
                                counts.append(data[data.Gender == gender[i]].Order_ID.count())
                            plt.bar(gender,counts)
                            plt.xlabel("Customer Count")
                            plt.ylabel("Gender")
                            for index, value in enumerate(counts):
                                plt.text(index, value,str(value))
                            plt.grid(True,axis='y')
                            plt.show()
                            
                        else:
                            print("Invalid Entry!")
                    
                    elif chart == 2:
                        print("********** PIE CHARTS **********\n\n")
                        print("1. Warehouse-Revenue Distribution\n2. Seller-Revenue Distribution\n3. Warehouse-Order Count Distribution ")
                        fig = input("Enter Your Choice:")
                        if fig == 1:
                            rev = []
                            for i in range(len(warehouse)):
                                rev.append(warehouse[i].Cost_of_the_Product.sum())
                            plt.pie(rev, labels = ware,autopct='%.0f%%')
                            plt.show()
                            
                        elif fig == 2:
                            rev = []
                            for i in range(len(seller)):
                                rev.append(seller[i].Cost_of_the_Product.sum())
                            plt.pie(rev, labels = sellers,autopct='%.0f%%')
                            plt.show()
                            
                        elif fig == 3:
                            prods = []
                            for i in range(len(ware)):
                                prods.append(data[data.Warehouse_Block == ware[i]])
                            counts = []
                            for i in range(len(prods)):
                                counts.append(prods[i].Order_ID.count())
                            fig = plt.figure(figsize =(10, 7))
                            plt.pie(counts, labels = ware, autopct='%.0f%%')
                            plt.show()
                            
                temp = input("\n\nDo you wish to continue? (Y/N)")
                if temp == 'N':
                    os.system('cls')
                    print("Session Logged Out!")
                    time.sleep(5)

        else:
            print("Wrong Password!")
            temp = input("Try Again? (Y/N)")

elif choice == 1:
    print("\n\n\n----Advertisement: Highest Discounted Products (Super Saver Deals)----\n", data.loc[
        data.Discount_Offered == data.Discount_Offered.max(), ['Product_ID', 'Cost_of_the_Product', 'Discount_Offered',
                                                               'Seller_Name']])
    while temp == 'Y':
        pid = int(input("\nEnter a valid Product ID to search for:"))
        if pid in data.Product_ID.unique():
            p = data[data.Product_ID == pid]
            sellers = p.Seller_Name.unique()
            seller = []  # List of separate dataframes of different sellers.
            rat = []
            for i in range(0, len(sellers)):
                seller.append(p[p.Seller_Name == sellers[i]])
                rat.append(seller[i].Customer_rating.mean() + seller[i].On_time_delivery.sum() / 1000)
            high = sellers[0]
            maxrat = rat[0]
            for i in range(1, len(rat)):
                if rat[i] > maxrat:
                    maxrat = rat[i]
                    high = sellers[i]
            print("\nBest Seller (Rating):", high)
            ship = p.Mode_of_Shipment.unique()
            shipment = []
            rat = []
            for i in range(0, len(ship)):
                shipment.append(p[p.Mode_of_Shipment == ship[i]])
                rat.append(shipment[i].Customer_rating.mean() + shipment[i].On_time_delivery.sum() / 1000)
            high = ship[0]
            maxrat = rat[0]
            for i in range(1, len(rat)):
                if rat[i] > maxrat:
                    maxrat = rat[i]
                    high = ship[i]
            print("Best Mode of Shipment:", high)
            print("\n----FOUND", len(p), "BUYING OPTIONS----\n")
            print(p.loc[:, ['Cost_of_the_Product', 'Seller_Name', 'Customer_rating']])
            low = p.Cost_of_the_Product.min()
            print("\n----BEST MONEY SAVER DEAL----\n")
            print(p.loc[p.Cost_of_the_Product == low, ['Cost_of_the_Product', 'Seller_Name', 'Customer_rating']])
            
        else:
            print("Product Not Found!")
        temp = input("\nDo you wish to continue? (Y/N)")
        os.system('cls')
        if temp == 'N':
            print("Thank You For Using Our Services!\nHave A Nice Day!")
            time.sleep(5)
