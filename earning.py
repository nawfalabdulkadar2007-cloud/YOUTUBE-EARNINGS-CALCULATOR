print("=" * 50)
print("      YOUTUBE CREATOR EARNINGS CALCULATOR")
print("=" * 50)

channel_name = input("Enter Channel Name: ")

subscribers = int(input("Enter Total Subscribers: "))

monthly_views = int(input("Enter Monthly Views: "))

cpm = float(input("Enter CPM (Earnings per 1000 views in ₹): "))

monthly_earnings = (monthly_views / 1000) * cpm

yearly_earnings = monthly_earnings * 12

print("\n")
print("=" * 50)
print("           CHANNEL REPORT")
print("=" * 50)

print("Channel Name       :", channel_name)
print("Subscribers        :", subscribers)
print("Monthly Views      :", monthly_views)
print("CPM                : ₹", cpm)
print("Monthly Earnings   : ₹", round(monthly_earnings, 2))
print("Yearly Earnings    : ₹", round(yearly_earnings, 2))

if subscribers >= 1000000:
    level = "Diamond Creator"
elif subscribers >= 100000:
    level = "Gold Creator"
elif subscribers >= 10000:
    level = "Silver Creator"
elif subscribers >= 1000:
    level = "Growing Creator"
else:
    level = "Beginner Creator"

print("Channel Level      :", level)

if monthly_views >= 1000000:
    performance = "Excellent"
elif monthly_views >= 500000:
    performance = "Very Good"
elif monthly_views >= 100000:
    performance = "Good"
else:
    performance = "Needs Improvement"

print("Performance        :", performance)

print("=" * 50)
print("Thank You for Using the Calculator!")
print("=" * 50)
