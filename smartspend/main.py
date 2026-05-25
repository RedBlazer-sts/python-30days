import csv
import json
def load_transactions():
   try:
        with open("transaction.csv",'r') as f:
            reader = csv.DictReader(f)
            list_of_dictionary = []
            for Individual_transaction in reader:
                try:
                    Individual_transaction["amount"] = float(Individual_transaction["amount"])
                    list_of_dictionary.append(Individual_transaction)
                except ValueError:
                    print("invalid amount skipping")    
        return list_of_dictionary
   except FileNotFoundError:
       print("Seeked file doesnt exits")
       return []

data = load_transactions()
    
def calculate_total(data):
    total_credit=0
    total_debit=0
    for row in data:
        if row["type"] == "credit":
            total_credit+=row["amount"]
        else:
            total_debit+=row["amount"]
    total= total_debit + total_credit
    return {
        "total amount spend" : total,
        "total credit" : total_credit,
        "total debit": total_debit
  }

def categorize_spendings(data):
    category_and_its_total_spend={

    }
    for row in data:
        if row["category"] in category_and_its_total_spend:
            category_and_its_total_spend[row["category"]] += row["amount"]
        else:
            category_and_its_total_spend[row["category"]] = row["amount"]
    return category_and_its_total_spend


def detect_recurring_spends(data):
    recurring_spends_and_its_counts={

    }
    for row in data:
        if row["description"] in recurring_spends_and_its_counts:
            recurring_spends_and_its_counts[row["description"]]["count"] += 1
        else:
            recurring_spends_and_its_counts[row["description"]]={"count" : 1,"amount": row["amount"]}
    return {k:v for k,v in recurring_spends_and_its_counts.items ()  if v["count"]>1}

print(detect_recurring_spends(data))
def generate_report():
    report = {
        "total spendings" : calculate_total(data),
        "Category wise spendind" : categorize_spendings(data),
        "Recurring spending and its count and amount"   : detect_recurring_spends(data)
    }
    with open("report.json","w") as f:
        json.dump(report,f,indent=4)

generate_report()

def display_dashboard():
    print("================MONTHLY DASHBOARD=================")
    print(f"Total Spending : {calculate_total(data)}")
    cat_wise_spend=categorize_spendings(data)
    for cat in cat_wise_spend:
        print(f"{cat} : {cat_wise_spend[cat]}")
    recurring_spend = detect_recurring_spends(data)
    for description_reac in recurring_spend:
        print(f"{description_reac} : counts : {recurring_spend[description_reac]["count"]} amount {recurring_spend[description_reac]["amount"]}")


display_dashboard()