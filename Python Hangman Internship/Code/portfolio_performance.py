import csv
import os

def analyze_portfolio_performance(filename="constituents.txt"):
    """
    Analyzes stock portfolio constituents, sectors, and distribution 
    to evaluate portfolio performance parameters.
    """
    if not os.path.exists(filename):
        print(f"Error: The data file '{filename}' was not found.")
        return

    total_stocks = 0
    sector_distribution = {}
    headquarters_locations = {}

    # Read and parse the CSV/Text data file
    with open(filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            total_stocks += 1
            sector = row.get('GICS Sector', '').strip()
            hq = row.get('Headquarters Location', '').strip()
            
            if sector:
                sector_distribution[sector] = sector_distribution.get(sector, 0) + 1
            if hq:
                headquarters_locations[hq] = headquarters_locations.get(hq, 0) + 1

    # Display Portfolio Analysis Results
    print("==========================================")
    print("     STOCK PORTFOLIO PERFORMANCE REPORT    ")
    print("==========================================")
    print(f"Total Stocks in Portfolio: {total_stocks}\n")
    
    print("Sector-wise Asset Distribution:")
    print("-" * 42)
    for sector, count in sorted(sector_distribution.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_stocks) * 100
        print(f"{sector}: {count} stocks ({percentage:.2f}%)")
    print("-" * 42)

if __name__ == "__main__":
    analyze_portfolio_performance()