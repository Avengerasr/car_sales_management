# expert_system.py
# Expert system functions used by the Flask app.
# analyze_sales(sales_rows) -> returns a string with insights
# recommend_car(budget, purpose, fuel) -> returns a recommendation string

def _get_amount(row):
    for k in ("price", "total_amount", "amount", "total"):
        if k in row and row[k] is not None:
            try:
                return float(row[k])
            except:
                pass
    return 0.0

def _get_model(row):
    for k in ("model_name", "car_model", "model"):
        if k in row and row[k]:
            return str(row[k])
    return "Unknown Model"

def _get_customer(row):
    for k in ("customer_name", "cust_name", "customer"):
        if k in row and row[k]:
            return str(row[k])
    return "Unknown Customer"

def analyze_sales(sales_rows):
    """
    Accepts `sales_rows` (list of dicts returned by cursor.fetchall(dictionary=True))
    Returns a readable string with insights (total revenue, avg, best seller, top customers).
    """
    if not sales_rows:
        return "No sales data available."

    total_orders = len(sales_rows)
    total_revenue = sum(_get_amount(r) for r in sales_rows)
    avg_sale = total_revenue / total_orders if total_orders else 0.0

    # Best selling model
    model_count = {}
    for r in sales_rows:
        m = _get_model(r)
        model_count[m] = model_count.get(m, 0) + 1
    best_seller = max(model_count, key=model_count.get)

    # Top customers by spending (top 3)
    customer_spend = {}
    for r in sales_rows:
        c = _get_customer(r)
        customer_spend[c] = customer_spend.get(c, 0.0) + _get_amount(r)
    top_customers = sorted(customer_spend.items(), key=lambda x: x[1], reverse=True)[:3]

    # Build the insights string
    lines = []
    lines.append("🔍 AI Expert Insights")
    lines.append(f"- Total Sales Records: {total_orders}")
    lines.append(f"- Total Revenue: ₹{total_revenue:,.2f}")
    lines.append(f"- Average Sale Value: ₹{avg_sale:,.2f}")
    lines.append(f"- Best Selling Model: {best_seller}")
    if top_customers:
        lines.append("- Top Customers by Spend:")
        for name, amt in top_customers:
            lines.append(f"  • {name} — ₹{amt:,.2f}")

    return "\n".join(lines)


def recommend_car(budget, purpose, fuel):
    """
    Rule-based recommendation. Inputs:
      - budget: string or number (in ₹)
      - purpose: 'family'|'luxury'|'economy'|'sports' (case-insensitive)
      - fuel: 'petrol'|'diesel'|'electric'|'hybrid' (case-insensitive)
    Returns human-readable recommendation.
    """
    try:
        budget = float(budget)
    except:
        return "Invalid budget value."

    purpose = (purpose or "").strip().lower()
    fuel = (fuel or "").strip().lower()

    # Electric preferred logic
    if fuel == "electric":
        if budget < 1000000:
            return "Tata Tiago EV — budget-friendly electric city car."
        if budget < 2000000:
            return "MG ZS EV — good range & features."
        return "Hyundai Ioniq 5 or BYD Seal — high-end electric options."

    # Hybrid
    if fuel == "hybrid":
        if budget < 1500000:
            return "Toyota Urban Cruiser Hyryder — practical hybrid for families."
        return "Honda City e:HEV / Toyota Camry Hybrid — premium hybrid choice."

    # Purpose-based suggestions (petrol/diesel hybrid included)
    if purpose == "family":
        if budget < 500000:
            return f"Maruti Alto ({fuel.title()}) — affordable reliable family starter car."
        if budget < 1000000:
            return f"Tata Nexon / Hyundai i20 ({fuel.title()}) — great family options."
        return f"Toyota Innova Crysta ({fuel.title()}) — spacious and comfortable for family trips."

    if purpose == "luxury":
        if budget < 3000000:
            return f"Skoda Superb ({fuel.title()}) — premium without going extreme."
        return f"Mercedes C-Class / BMW 3 Series ({fuel.title()}) — luxury experience."

    if purpose == "economy":
        if fuel == "diesel":
            return "Tata Altroz Diesel — efficient and safe."
        if fuel == "petrol":
            return "Maruti Swift Petrol — economy and reliability."
        return "Maruti CNG/Tiago EV — very economical options."

    if purpose == "sports" or purpose == "sport":
        if budget < 2000000:
            return f"Volkswagen Polo GT / Hyundai i20 N Line ({fuel.title()}) — sporty and fun."
        return f"BMW Z4 / Porsche 718 ({fuel.title()}) — high-performance sports options."

    # Fallback
    return "Please choose budget, purpose, and fuel to get a tailored recommendation."
