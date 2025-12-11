def calculate_sales():
    #each crop has 16 acres (80 acres / 5 segments)
    acres = 16 

    #Tomato Calculation
    tomatoes_30 = 0.30 * acres * 10 #30% land -> 10 tonnes/acre
    tomatoes_70 = 0.70 * acres * 12  #70% land_. 12 tonnes/acre
    tomatoes_total_tonnes = tomatoes_30 + tomatoes_70 
    tomatoes_sales = tomatoes_total_tonnes * 1000 * 7 # convert tonnes->kg * 7 rupees


    #potato Calculation
    potatoes_tonnes = acres * 10 
    potatoes_sales = potatoes_tonnes * 1000 * 20 

    #cabbage Calculation 
    cabbage_tonnes = acres * 14 
    cabbage_sales = cabbage_tonnes * 1000 *24 

    #sunflower calculation
    sunflower_tonnes = acres * 0.7 
    sunflower_sales = sunflower_tonnes * 1000 * 200

    sugarcane_tonnes = acres * 45 
    sugarcane_sales = sugarcane_tonnes * 4000 # price per tonne

    total_sales = (tomatoes_sales + potatoes_sales + cabbage_sales+sunflower_sales + sugarcane_sales)

    chemical_free_sales = (tomatoes_sales + potatoes_sales + cabbage_sales + sunflower_sales)

    return total_sales, chemical_free_sales

if __name__ == "__main__":
    total, chemical_free = calculate_sales()
    print("Total Sales from 80 acres: ₹{:,.2f}".format(total))  
    print("Sales from chemical-free farming at 11 months: ₹{:,.2f}".format(chemical_free))

