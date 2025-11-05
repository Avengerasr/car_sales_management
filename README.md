# car_sales_management
DBMS Mini Project - Car Sales Management System

The Car Sales Management System is a web-based application built using Flask (Python) and MySQL, designed to help manage car sales, customers, and records efficiently.

In addition to traditional database management, this project features an AI Expert System that provides intelligent insights and car recommendations based on various parameters such as budget, fuel type, performance, and eco score.

In addition to traditional database management, this project features an AI Expert System that provides intelligent insights and car recommendations based on various parameters such as budget, fuel type, performance, and eco score. 


This system automates the car sales workflow, supports CRUD operations, and integrates AI reasoning to enhance decision-making for customers and dealers.


# Features

| Feature                             | Description                                                                   |
| ----------------------------------- | ------------------------------------------------------------------------------|
|  **AI Car Recommendation Engine**   | Suggests best cars based on budget and fuel type using knowledge-based rules  |
|  **Performance & Eco Scoring**      | Calculates performance score using engine power, mileage, and price           |
| **Eco-Friendly Evaluation**         | Assigns an “Eco Score” based on fuel type and manufacturing year              |
| **Knowledge-Based Reasoning**       | Uses logical rules to filter and rank cars dynamically                        |
| **Future Expansion**                | Can be extended to include resale prediction, financing suggestions, and more |



#  Core Functionalities


| Module                           | Description                                                         |
| -------------------------------- | ------------------------------------------------------------------- |
|  **Sales Management**            | Add, update, delete, and view car sales records                     |
|  **Customer Details**            | Store and retrieve customer data linked to sales                    |
|  **Dashboard Insights**          | Shows AI-based insights like top-selling model, total revenue, etc. |
|  **Expert System Integration**   | AI recommendations displayed dynamically through Flask              |
|  **Financial Overview**          | Calculates total and average sale value                             |
|  **Search & Sort (optional)**    | Filter records by car model, customer, or date                      |





##  Tech Stack

1. **Frontend:** HTML5, CSS3, Bootstrap 5  
2. **Backend:** Python (Flask Framework)  
3. **Database:** MySQL  
4. **AI Module:** Rule-Based Expert System in Python  
5. **Visualization:** Chart.js  

---

##  Project Structure

**car_sales_management/**
│|
|├── app.py                 # Main Flask Application ---
├── expert_system.py       # AI Expert System Logic ---
├── templates/ --
│   |├── index.html         # Main Dashboard UI ---
│   |├── edit.html          # Edit Record Page ---
│   └|── recommend.html     # AI Recommendation Page ---
├── static/                # CSS, JS, Images ---
├── requirements.txt       # Python Dependencies ---
└── README.md              # Project Description File ---

---






