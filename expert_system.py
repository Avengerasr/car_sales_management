# expert_system.py
def recommend_car(budget, car_type, fuel_type):
    # Simple rule-based AI Expert System
    if budget < 500000:
        if fuel_type == "petrol":
            return "Recommended Car: Maruti Alto or Renault Kwid (Best for low budget & petrol users)"
        else:
            return "Recommended Car: Tata Tiago Diesel (Fuel efficient low-cost car)"
    elif 500000 <= budget <= 1000000:
        if car_type == "SUV":
            return "Recommended Car: Kia Sonet or Tata Nexon"
        else:
            return "Recommended Car: Maruti Baleno or Hyundai i20"
    else:
        if car_type == "SUV":
            return "Recommended Car: MG Hector or Mahindra XUV700"
        else:
            return "Recommended Car: Hyundai Verna or Honda City"

# You can test it separately
if __name__ == "__main__":
    print(recommend_car(800000, "SUV", "petrol"))
