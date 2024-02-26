import matplotlib.pyplot as plt

def calculate_moving_average(data, window_size):
    moving_avg = data['Close'].rolling(window=window_size).mean()
    return moving_avg

def plot_moving_average(data, moving_avg):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label='Close Price')
    plt.plot(moving_avg.index, moving_avg, label='Moving Average', color='red')
    plt.title('Moving Average (30-Day)')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

# Example usage:
window_size = 30
moving_avg = calculate_moving_average(stock_data, window_size)
plot_moving_average(stock_data, moving_avg)
