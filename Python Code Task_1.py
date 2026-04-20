# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:49:27 2026

@author: Mugeri Khethani

"""

#  Load & Clean Data
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Anaconda3\Sales_Project\Superstore.csv', encoding='latin1')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month_Year'] = df['Order Date'].dt.to_period('M')
df = df.drop_duplicates()

print(" Data loaded and cleaned!") 

# ANALYSIS 
# ============================================================

# --- 1. TOTAL KEY METRICS ---
print("\n========== KEY BUSINESS METRICS ==========")
print(f"Total Revenue:   ${df['Sales'].sum():,.2f}")
print(f"Total Profit:    ${df['Profit'].sum():,.2f}")
print(f"Total Orders:    {df['Order ID'].nunique():,}")
print(f"Profit Margin:   {(df['Profit'].sum() / df['Sales'].sum()) * 100:.1f}%")

# --- 2. SALES BY CATEGORY ---
print("\n========== SALES BY CATEGORY ==========")
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales)

# --- 3. SALES BY REGION ---
print("\n========== SALES BY REGION ==========")
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(region_sales)

# --- 4. TOP 10 PRODUCTS BY REVENUE ---
print("\n========== TOP 10 PRODUCTS BY REVENUE ==========")
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_products)

# --- 5. PROFIT BY CATEGORY ---
print("\n========== PROFIT BY CATEGORY ==========")
category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
print(category_profit)

# --- 6. YEARLY SALES TREND ---
print("\n========== YEARLY SALES TREND ==========")
yearly_sales = df.groupby('Year')['Sales'].sum()
print(yearly_sales)



#  DASHBOARD 
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

fig = plt.figure(figsize=(18, 11))
fig.patch.set_facecolor('#f5f7fb')


# TITLE 
# ============================================================

fig.suptitle("Business Sales Performance Dashboard",
             fontsize=20, fontweight='bold', y=0.98)


# KPI CARDS
# ============================================================

kpis = [
    ("Total Sales", f"${df['Sales'].sum():,.0f}"),
    ("Total Profit", f"${df['Profit'].sum():,.0f}"),
    ("Total Orders", f"{df['Order ID'].nunique():,}"),
    ("Profit Margin", f"{(df['Profit'].sum()/df['Sales'].sum())*100:.1f}%")
]

x_pos = [0.1, 0.3, 0.5, 0.7]

for (title, value), x in zip(kpis, x_pos):
    fig.text(x, 0.90,
             f"{value}\n{title}",
             ha='center', va='center',
             fontsize=14, fontweight='bold',
             bbox=dict(facecolor='#ffffff',
                       edgecolor='#dddddd',
                       boxstyle='round,pad=0.6'))


# CHART 1: SALES BY CATEGORY 
# ============================================================

ax1 = fig.add_axes([0.05, 0.55, 0.4, 0.25])

category_sales = df.groupby('Category')['Sales'].sum()

ax1.bar(category_sales.index, category_sales.values, color='#1f77b4')

ax1.set_title('Total Sales by Category', fontsize=13, fontweight='bold')

for i, v in enumerate(category_sales.values):
    ax1.text(i, v + 1000, f'${v:,.0f}', ha='center', fontsize=9)


# CHART 2: SALES BY REGION 
# ============================================================

ax2 = fig.add_axes([0.5, 0.55, 0.2, 0.25])

region_sales = df.groupby('Region')['Sales'].sum()

ax2.bar(region_sales.index, region_sales.values, color='#1f77b4')

ax2.set_title('Sales by Region', fontsize=13, fontweight='bold')

for i, v in enumerate(region_sales.values):
    ax2.text(i, v + 1000, f'${v:,.0f}', ha='center', fontsize=8)


# CHART 3: YEARLY TREND 
# ============================================================

ax3 = fig.add_axes([0.75, 0.55, 0.2, 0.25])

yearly_sales = df.groupby('Year')['Sales'].sum()

ax3.plot(yearly_sales.index, yearly_sales.values,
         marker='o', linewidth=3, color='#1f77b4')

ax3.fill_between(yearly_sales.index,
                 yearly_sales.values,
                 alpha=0.2,
                 color='#1f77b4')

ax3.set_title('Yearly Sales Trend', fontsize=13, fontweight='bold')


# CHART 4: PROFIT BY CATEGORY 
# ============================================================
ax4 = fig.add_axes([0.05, 0.2, 0.4, 0.25])

category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)

# All bars blue
ax4.bar(category_profit.index, category_profit.values, color='#1f77b4')

ax4.set_title('Profit by Category', fontsize=13, fontweight='bold')

# Value labels
for i, v in enumerate(category_profit.values):
    ax4.text(i, v + (500 if v > 0 else -1500),  # adjust for negative values
             f'${v:,.0f}',
             ha='center',
             fontsize=9)



# CHART 5: TOP 10 PRODUCTS 
# ============================================================


ax5 = fig.add_axes([0.55, 0.2, 0.42, 0.25])

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

# Shorten long product names to max 30 characters
top_products.index = [name[:30] + '...' if len(name) > 30 else name for name in top_products.index]

ax5.barh(top_products.index, top_products.values, color= '#1f77b4' )

ax5.set_title('Top 10 Products by Revenue', fontsize=13, fontweight='bold')
ax5.tick_params(axis='y', labelsize=7)






# CLEANUP
# ============================================================

for ax in [ax1, ax2, ax3, ax4, ax5]:
    ax.spines[['top', 'right']].set_visible(False) 

# Save
plt.savefig(r'C:\Anaconda3\Sales_Project\Sales_Dashboard_2026.pdf',
            bbox_inches='tight', dpi=150)

plt.show()


#  BUSINESS INSIGHTS
# ============================================================

print("\n========== FINAL BUSINESS INSIGHTS ==========")
print(f"💰 Total Revenue:     ${df['Sales'].sum():,.2f}")
print(f"📈 Total Profit:      ${df['Profit'].sum():,.2f}")
print(f"🛒 Total Orders:      {df['Order ID'].nunique():,}")
print(f"📊 Profit Margin:     {(df['Profit'].sum() / df['Sales'].sum()) * 100:.1f}%")
print(f"\n🏆 Best Category:     {category_sales.index[0]} (${category_sales.values[0]:,.2f})")
print(f"🌍 Best Region:       {region_sales.index[0]} (${region_sales.values[0]:,.2f})")
print(f"📦 Best Product:      {top_products.index[0]}")