import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_sales(file_path):
    df = pd.read_csv(file_path)
    print(df.info(), "\n", df.head(), "\n")
    sns.set(style="whitegrid")
    
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df.sort_values(by='Date', inplace=True)
        sns.lineplot(x='Date', y='Sales', data=df, marker='o')
        plt.xticks(rotation=45)
        plt.show()
    
    sns.histplot(df['Sales'], bins=20, kde=True, color='blue')
    plt.show()
    
    if 'Category' in df.columns:
        sns.barplot(x='Category', y='Sales', estimator=sum, ci=None, palette='viridis', data=df)
        plt.xticks(rotation=45)
        plt.show()

if __name__ == "__main__":
    visualize_sales("pra8.csv")
