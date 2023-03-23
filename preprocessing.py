import preprocessor as p
import pandas as pd
import csv
def process(filename):
    
    df = pd.read_csv(filename, header=None)
    tw_list = pd.DataFrame(df[1])
    s_list = pd.DataFrame(df[2])
    new_list = []
    new_s_list = []
    for x in range(len(tw_list)):
        if tw_list[1][x] not in new_list:
            new_list.append(tw_list[1][x])
            new_s_list.append(s_list[2][x])
    with open(f'{filename[:-4]}_cleaned.csv', 'w') as f:
        for tweet in new_list:
            new_tweet = p.clean(tweet).replace(',','')
            f.write(f'{new_tweet},')
    with open(f'{filename[:-4]}_sentiments_cleaned.csv', 'w') as f:
        writer = csv.writer(f)
        for s in new_s_list:
            f.write(f'{s},')

if __name__ == '__main__':
    process('smileannotationsfinal.csv')