import preprocessor as p
import pandas as pd

def process(filename):
    
    df = pd.read_csv(filename, header=None)
    tw_list = pd.DataFrame(df[1])
    with open(f'{filename}_cleaned.csv', 'w') as f:
        for tweet in tw_list[1]:
            new_tweet = p.clean(tweet).replace(',','')
            f.write(f'{new_tweet},')

if __name__ == '__main__':
    process('smile_annotations.csv')