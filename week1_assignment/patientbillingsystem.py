services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI",
]

costs = [500, 300, 800, 1500, 4000, 7000] 
GST_Rate = 0.18 

def get_patient_details():
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    contact = input("Enter Contact Number: ")
    return name, age, gender, contact

def display_services():
    print("\nAvailable Services:")
    for i in range(len(services)):
        print(f"{i+1}. {services[i]} - {costs[i]}INR")

def select_services():
    selections = input("\nEnter service number separated by spaces (eg, 1 4)").split()
    selected_services = [] 
    selected_costs = []

    for choice in selections:
        index = int(choice) - 1
        if 0 <= index  < len(services):
            selected_services.append(services[index])
            selected_costs.append(costs[index])
    return selected_services, selected_costs


def calculateTotal(selected_costs):
    return (sum(selected_costs))


def apply_gst(subtotal):
    gst = subtotal * GST_Rate
    grandtotal = gst+ subtotal
    return gst, grandtotal

def generate_invoice(name, age, gender, contact, selected_services, selected_costs, subtotal, gst, grand_total):
    
    print("\n-----------------------------------------------")
    print("HealWell Care Hospital")
    print("Patient Invoice")
    print("-----------------------------------------------")

    print("\nPatient Information:")
    print("Name   :", name)
    print("Age    :", age)
    print("Gender :", gender)
    print("Contact:", contact)
    print("\nServices Availed:")
    for i in range(len(selected_services)):
        print(f"{i + 1}. {selected_services[i]}: ₹{selected_costs[i]}")
    print("\nSubtotal: ₹", subtotal)
    print("GST (18%): ₹", gst)
    print("Grand Total: ₹", grand_total)
    print("\nThank you for choosing HealWell Care Hospital!")

if __name__ == "__main__":
    try:
        print("=== HealWell Care Hospital ===\n")

        name, age, gender, contact = get_patient_details()
        display_services()
        selected_services, selected_costs = select_services()

        subtotal = calculateTotal(selected_costs)
        gst, grand_total = apply_gst(subtotal)

        generate_invoice(
            name, age, gender, contact,
            selected_services, selected_costs,
            subtotal, gst, grand_total
        )

    except ValueError:
        print("Invalid input! Please enter numbers correctly.")
    except Exception as e:
        print("An unexpected error occurred:", e)



