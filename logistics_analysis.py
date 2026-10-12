import pandas as pd
data = {
    "Order_ID": [101, 102, 103, 104, 105, 106],
    "Distance_KM": [5, 12, 8, 15, 7, 10],
    "Delivery_Time_Min": [20, 45, 30, 60, 25, 40],
    "Promised_Time_Min": [30, 40, 35, 50, 30, 45],
    "Delivery_Cost": [50, 100, 70, 140, 60, 90]
}

df = pd.DataFrame(data)
df["On_Time"] = (
    df["Delivery_Time_Min"] <= df["Promised_Time_Min"]
)
total_orders = len(df)
on_time_orders = df["On_Time"].sum()
on_time_rate = (on_time_orders / total_orders) * 100

average_delivery_time = df["Delivery_Time_Min"].mean()
average_delivery_cost = df["Delivery_Cost"].mean()
average_distance = df["Distance_KM"].mean()

print("LOGISTICS DATA ANALYSIS")
print("-----------------------")
print("Total Orders:", total_orders)
print("On-Time Delivery Rate:", round(on_time_rate, 2), "%")
print("Average Delivery Time:", round(average_delivery_time, 2), "minutes")
print("Average Delivery Cost:", round(average_delivery_cost, 2))
print("Average Distance:", round(average_distance, 2), "KM")

print("\nDelivery Details:")
print(df)