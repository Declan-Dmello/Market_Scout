from transformers import BertTokenizer, BertForSequenceClassification, AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline


tokenizer1 = AutoTokenizer.from_pretrained("mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")
model1 = AutoModelForSequenceClassification.from_pretrained("mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")

pipe = pipeline("text-classification", model=model1,tokenizer=tokenizer1)

sentences = ["Operating profit rose to EUR 13.1 mn from EUR 8.7 mn in the corresponding period in 2007 representing 7.7 % of net sales.",
             " Bids or offers include at least 1,000 shares and the value of the shares must correspond to at least EUR 4,000.",
             " Raute reported a drop per share of EUR 0.86 for the first half of 2009 , against EPS of EUR 0.74 in the corresponding period of 2008.Rupee falls 5 paise to 83.18 against US dollar in early trade.",
             "Gold prices fall Rs 250 to Rs 51,350 per 10 gram; silver declines Rs 550 . Sensex, Nifty end lower on profit-booking; IT, metal stocks drag. DGGI detects Rs 1.36 lakh crore tax evasion in H1 of FY24"
             ]

#a803244bb35c4f4d81a3883e28f60cc2 

res = pipe(sentences)
print("----------------------------")

print(res)
#PIECHART,LABEL , SCORE

