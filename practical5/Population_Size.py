import matplotlib.pyplot as plt
# Original data
uk_countries = [57.11, 3.13, 1.91, 5.45]
uk_labels = ['England', 'Wales', 'Northern Ireland', 'Scotland']
china_province = [65.77, 41.88, 45.28, 61.27, 85.15]
china_labels = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']
# Sort data while keeping labels synchronized
def sort_data(values, labels):
    # Pair values with labels and sort by value (descending)
    sorted_pairs = sorted(zip(values, labels), key=lambda x: x[0], reverse=True)
    # Unpack into separate lists
    sorted_values = [x[0] for x in sorted_pairs]
    sorted_labels = [x[1] for x in sorted_pairs]
    return sorted_values, sorted_labels
# Sort both datasets
uk_sorted, uk_labels_sorted = sort_data(uk_countries, uk_labels)
china_sorted, china_labels_sorted = sort_data(china_province, china_labels)
# Print sorted lists
print("UK Countries (Sorted):", uk_sorted)
print("China Provinces (Sorted):", china_sorted)
# Function to create standardized pie charts
def create_pie_chart(values, labels, title, highlight_max=True):
    # Highlight the largest segment if enabled
    explode = [0.1 if (i == 0 and highlight_max) else 0 for i in range(len(values))]
    # Create figure with consistent style
    plt.figure(figsize=(8, 6))
    wedges, _, autotexts = plt.pie(values,explode=explode,labels=labels,autopct='%1.1f%%',startangle=90,shadow=True,colors=plt.cm.tab20.colors,textprops={'fontsize': 10})
    # Improve label readability
    plt.setp(autotexts, size=10, weight="bold")
    plt.title(title, pad=20, fontweight='bold')
    plt.legend(wedges, labels, loc="upper right", bbox_to_anchor=(1.3, 1))
    plt.tight_layout()  # Prevent label clipping
    plt.show()
# Generate visualizations
create_pie_chart(uk_sorted, uk_labels_sorted,"UK Population Distribution (Sorted)")
create_pie_chart(china_sorted, china_labels_sorted,"Zhejiang-Neighboring Provinces Population (Sorted)")