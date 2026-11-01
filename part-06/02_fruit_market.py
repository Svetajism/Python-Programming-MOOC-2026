def read_fruits():
    fruit_prices = {}
    with open("fruits.csv") as prices:
        for line in prices:
            parts = line.split(";")
            fruit = parts[0]
            price = float(parts[1])
            fruit_prices[fruit] = price
    return fruit_prices

if __name__ == "__main__":
    read_fruits()