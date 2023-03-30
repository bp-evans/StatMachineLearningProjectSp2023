#detect language of tweets
from langdetect import detect
import pandas as pd
import matplotlib.pyplot as plt
from googletrans import Translator
import csv

# label text by language
def detect_textlang(text):
    try:
        src_lang = detect(text)
        if src_lang =='en':
            return 'en'
        else:
        #return "NA"    
            return src_lang
    except:
        return "NA"

#Translate to English
def translate_text(text,lang):
    translator = Translator(service_urls=['translate.googleapis.com'])
    trans_text = translator.translate(text,src = lang, dest ='en').text
    
    trans_text_fixed = trans_text.replace("\u200b",'')
    trans_text_fixed_2 = trans_text_fixed.replace('&amp','').lower()
    return trans_text_fixed_2
    
if __name__ == '__main__':
    filename ='smileannotationsfinal_cleaned.csv'
    df = pd.read_csv(filename, header =None).T
    df['plain_text'] = df

    # Detect and label language
    df['text_lang']=df.plain_text.apply(detect_textlang)

    # Plot Bar chart with the occurances of top 10 languages detected
    plt.figure(figsize=(4,3))
    df.groupby(df.text_lang).plain_text.count().sort_values(ascending=False).head(10).plot.bar()
    plt.show() 

    # Translate the text to englsih using google translator
    df['translated_text']=df.apply(lambda x: x.plain_text if x.text_lang == 'en'or x.text_lang =='NA' else translate_text(x.plain_text, x.text_lang), axis=1)

    #save in new file
    with open(f'{filename[:-4]}_translated.csv', 'w') as f:
        writer = csv.writer(f)
        for s in df.translated_text:
            f.write(f'{s},')

