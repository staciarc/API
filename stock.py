import matplotlib.pyplot as plt
import yfinance as yf
from matplotlib.dates import DateFormatter, MonthLocator, WeekdayLocator

class Stock():

    def __init__(self, m):
        self.m = m

    def info(self):
        tick = yf.Ticker(self.m)
        info_list = f"Рыночная капитализация: ${tick.info['marketCap']}\n" \
            f"Количество работников : {tick.info['fullTimeEmployees']}\n" \
            f"Краткая информация о бизнесе : \n{tick.info['longBusinessSummary']}"
        return info_list

    def div(self):
        tick = yf.Ticker(self.m)
        return tick.dividends.tail(10)

    def history(self):
        tick = yf.Ticker(self.m)
        df = tick.history(period="3mo")

    def plot(self):
        tick = yf.Ticker(self.m)
        df = tick.history(period="3mo")
        plot = df['Close'].plot()
        # настраиваем метки промежуточных делений
        weekday_locator = WeekdayLocator(byweekday=(0), interval=1)
        plot.xaxis.set_minor_locator(weekday_locator)
        plot.xaxis.set_minor_formatter(DateFormatter("%d\n%a"))
        # настраиваем метки основных делений
        plot.xaxis.set_major_locator(MonthLocator())
        plot.xaxis.set_major_formatter(DateFormatter('\n\n\n%b\n%Y'))
        pict = plt.savefig('saved_figure.png')
        return pict
