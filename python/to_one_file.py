import os
import zipfile

import numpy as np
import pandas as pd

paths = "data/spot/monthly/klines/BTCUSDT/5m/", "data/spot/monthly/klines/ETHUSDT/5m/"


for path in paths:
    dirs = os.listdir(path)
    print(dirs)
    all_data_array = []
    for file in dirs:
        print(path + file)
        if 'zip' in file:
            archive = zipfile.ZipFile(path + file, 'r')
            str_csv = file.replace("zip", "csv")
            file_data = pd.read_csv(archive.open(str_csv), header=None)
            all_data_array.append(file_data)

    result_data = pd.concat(all_data_array)
    print(result_data)
    result_data.to_csv(path + 'sum.csv', header=False, index=False, sep=';')
    train, test = np.split(result_data,
                  [int(.675 * len(result_data))])
    print(train)
    print(test)
    train.to_csv(path + 'train.csv', header=False, index=False, sep=';')
    test.to_csv(path + 'test.csv', header=False, index=False, sep=';')

