import math
from sklearn.utils import Bunch
import pandas as pd

def get_data_normalized():
    data = Bunch()
    data.samples = []
    data.s4 = []
    min_svid = 999999
    max_svid = -1
    min_az = 999999
    max_az = -1
    min_elev = 999999
    max_elev = -1
    cont = 0
    with open('data/STMC_2022-10-09_2022-10-13_1565c7edca35bc66bdc4a6c85625daee_EDITADO.txt', 'r') as file:
        file.readline()     # reads first line with titles
        while True:
            cont += 1
            # if cont > 10000:
            #     break
            line = file.readline()
            if not line:
                break
            line = line.strip().split('\t')
            
            # oc_time = time.mktime(datetime.strptime((line[0]), '%d/%m/%Y %H:%M').timetuple())
            hour = line[0].split()[1].split(':')[0]
            hour = int(hour)

            per = ''
            if hour < 6:
                per = 0 #'mad'
            elif hour < 12:
                per = 1 # 'man'
            elif hour < 18:
                per = 2 # 'tar'
            else:
                per = 3  #'noi'


            svid = int(line[1])
            
            try: az = int(line[2])
            except: continue
            
            try: elev = int(line[3])
            except: continue

            try: s4 = float(line[4].replace(',', '.'))
            except: continue
            if math.isnan(s4):
                continue
            
            classification = -1 if s4 > 0.6 else 1
            
            min_az = min(min_az, az)
            max_az = max(max_az, az)
            min_elev = min(min_elev, elev)
            max_elev = max(max_elev, elev)
            min_svid = min(min_svid, svid)
            max_svid = max(max_svid, svid)

            data.samples.append([per, svid, az, elev])
            data.s4.append(classification)

        # Normalization
        for sample in data.samples:
            sample[0] = (sample[0]-min_svid)/(max_svid-min_svid)
            sample[1] = (sample[1]-min_az)/(max_az-min_az)
            sample[2] = (sample[2]-min_elev)/(max_elev-min_elev)

    return data

def get_data_normalized_csv(file_path, data=None):
    if not data:
        data = Bunch()
        data.samples = []
        data.s4 = []
    min_svid = 999999
    max_svid = -1
    min_az = 999999
    max_az = -1
    min_elev = 999999
    max_elev = -1
    cont = 0
    with open(file_path, 'r') as file:
        file.readline()     # reads first line with titles
        while True:
            cont += 1
            # if cont > 10000:
            #     break
            line = file.readline()
            if not line:
                break
            line = line.strip().split(', ')
            
            # oc_time = time.mktime(datetime.strptime((line[0]), '%d/%m/%Y %H:%M').timetuple())
            hour = line[0].split()[1].split(':')[0]
            hour = int(hour)

            per = ''
            if hour < 6:
                per = 0 #'mad'
            elif hour < 12:
                per = 1 # 'man'
            elif hour < 18:
                per = 2 # 'tar'
            else:
                per = 3  #'noi'


            svid = int(line[1])
            
            try: az = int(line[2])
            except: continue
            
            try: elev = int(line[3])
            except: continue

            try: s4 = float(line[4].replace(',', '.'))
            except: continue
            if math.isnan(s4):
                continue
            
            classification = -1 if s4 > 0.6 else 1
            
            min_az = min(min_az, az)
            max_az = max(max_az, az)
            min_elev = min(min_elev, elev)
            max_elev = max(max_elev, elev)
            min_svid = min(min_svid, svid)
            max_svid = max(max_svid, svid)

            data.samples.append([per, svid, az, elev])
            data.s4.append(classification)

        # Normalization
        for sample in data.samples:
            sample[0] = (sample[0]-min_svid)/(max_svid-min_svid)
            sample[1] = (sample[1]-min_az)/(max_az-min_az)
            sample[2] = (sample[2]-min_elev)/(max_elev-min_elev)

    return data

def get_data_normalized_under_sample():
    data = Bunch()
    data.samples = []
    data.s4 = []
    min_svid = 999999
    max_svid = -1
    min_az = 999999
    max_az = -1
    min_elev = 999999
    max_elev = -1
    cont = 0
    lin = 0
    with open('data/STMC_2022-10-09_2022-10-13_1565c7edca35bc66bdc4a6c85625daee_EDITADO.txt', 'r') as file:
        file.readline()     # reads first line with titles
        while True:
            cont += 1
            lin += 1
            # if cont > 10000:
            #     break
            line = file.readline()
            if not line:
                break
            line = line.strip().split('\t')
            
            # oc_time = time.mktime(datetime.strptime((line[0]), '%d/%m/%Y %H:%M').timetuple())
            hour = line[0].split()[1].split(':')[0]
            hour = int(hour)

            per = ''
            if hour < 6:
                per = 0 #'mad'
            elif hour < 12:
                per = 1 # 'man'
            elif hour < 18:
                per = 2 # 'tar'
            else:
                per = 3  #'noi'


            svid = int(line[1])
            
            try: az = int(line[2])
            except: continue
            
            try: elev = int(line[3])
            except: continue

            try: s4 = float(line[4].replace(',', '.'))
            except: continue
            if math.isnan(s4):
                continue
            
            classification = -1 if s4 > 0.6 else 1
            if lin%10<6:
                continue
            
            min_az = min(min_az, az)
            max_az = max(max_az, az)
            min_elev = min(min_elev, elev)
            max_elev = max(max_elev, elev)
            min_svid = min(min_svid, svid)
            max_svid = max(max_svid, svid)

            data.samples.append([per, svid, az, elev])
            data.s4.append(classification)

        # Normalization
        for sample in data.samples:
            sample[0] = (sample[0]-min_svid)/(max_svid-min_svid)
            sample[1] = (sample[1]-min_az)/(max_az-min_az)
            sample[2] = (sample[2]-min_elev)/(max_elev-min_elev)

    return data

def get_data():
    data = Bunch()
    data.samples = []
    data.s4 = []
    i = 0
    low = 0
    high = 0
    moderate = 0
    with open('data/STMC_2022-10-09_2022-10-13_1565c7edca35bc66bdc4a6c85625daee_EDITADO.txt', 'r') as file:
        file.readline()     # reads first line with titles
        while True:
            i+=1
            line = file.readline()
            if not line:
                break
            line = line.strip().split('\t')
            
            # oc_time = time.mktime(datetime.strptime((line[0]), '%d/%m/%Y %H:%M').timetuple())
            
            svid = int(line[1])
            
            try: az = int(line[2])
            except: continue
            
            try: elev = int(line[3])
            except: continue

            try: s4 = float(line[4].replace(',', '.'))
            except: continue
            if math.isnan(s4):
                continue
            
            classification = 'high' if s4 > 0.6 else 'low'
            data.samples.append([svid, az, elev])
            data.s4.append(classification)
    return data

get_data()

def get_data_normalized_regression():
    data = pd.read_csv('/home/lemateus/TCC/cintilacao/data/PRU2_2018-09-01_2018-09-15_9464c9cda8dce80d71af4c0f7524355bEDITADO.csv', na_values=[' ', ''])

    data['time_utc'] = pd.to_datetime(data['time_utc'], format='%Y-%m-%d %H:%M:%S')
    data = data.loc[data['time_utc']>='2018-09-04 14:10:00']
    data = data[data[' svid'] == 131]
    data = data[['time_utc', ' svid', ' azim', ' elev', ' s4']]
    data.columns = ['time', 'svid', 'azim', 'elev', 's4']
    data['s4'] = data['s4'].astype(float)
    # data.dropna(inplace=True)
    data.reset_index(drop=True, inplace=True)
    # print(data.dtypes)
    # data = data[:1000]
    # print(data)
    # data = data[:50]

    # train = data.loc[data['ds']<'2018-09-14 23:59:00']
    # test = data.loc[data['ds']>='2018-09-14 23:59:00']
    data.plot(x='time', y='s4')
    # data.to_csv('/home/lemateus/TCC/cintilacao/only_125.csv')
    data.interpolate('linear')
