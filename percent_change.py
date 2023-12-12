import matplotlib.pyplot as plt

years = [2015, 2016, 2017, 2018, 2019, 2020]
installed_capacities = [71, 77.7, 81, 83.1, 84.9, 89]

plt.bar(years, installed_capacities, color='blue')
plt.xlabel('Years', fontsize=24)  # Adjust font size for x-axis label
plt.ylabel('Licensed Installed Capacities (in GW)', fontsize=24)  # Adjust font size for y-axis label
plt.title('Licensed Installed Capacities Over the Years', fontsize=28)  # Adjust font size for title

# Add the values and percentage change on top of each bar with larger font size
for i, value in enumerate(installed_capacities):
    plt.text(years[i], value + 1, f'{value:.2f}', ha='center', va='bottom', fontsize=18)  # Adjust font size for value
    if i > 0:
        percentage_change = ((value - installed_capacities[i - 1]) / installed_capacities[i - 1]) * 100
        plt.text(years[i], value + 4, f'{percentage_change:.2f}%', ha='center', va='bottom', color='green', fontsize=18)  # Adjust font size for percentage change

plt.ylim(top=max(installed_capacities) + 10)  # Adjust y-axis limit to accommodate text
plt.show()
