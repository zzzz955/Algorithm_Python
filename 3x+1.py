import pandas as pd
import matplotlib.pyplot as plt


def showcase(num):
    index = 1
    result = {
        'index': [],
        'value': [],
    }
    if num >= 1 and isinstance(num, int):
        while num != 1:
            if num % 2 != 0:
                num *= 3
                num += 1
            elif num % 2 == 0:
                num //= 2
            else:
                return None
            result['index'].append(index)
            result['value'].append(num)
            index += 1
        to_data_frame(result)
    else:
        pass


def to_data_frame(data):
    df = pd.DataFrame(data, index=None)
    max_value = max(df['value'])
    len_index = len(df['index'])
    draw_graph(df, max_value, len_index)


def draw_graph(df, max_value, len_index):
    plt.plot(df['index'], df['value'], linestyle='-', color='b', label=f'max : {max_value}')
    plt.title('3x+1 result')
    plt.xlabel('index')
    plt.ylabel('value')
    if len_index > 10:
        range_val = 10 ** (len(str(len_index))-2)
    else:
        range_val = 1
    plt.xticks(range(min(df['index']), max(df['index']), range_val), rotation=45)

    plt.legend()
    plt.show()


showcase(51)