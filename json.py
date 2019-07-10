from googletrans import Translator
import json
#File I/O Open function for read data from JSON File
with open('C:/en.json') as file_object:
        # store file data in object using json.load
        data = json.load(file_object)
#Getting key and values of dictionary

conv_dict={}
for i in data:
        key=i
        value=data[i]
        #print("key:",key,"  value:",value)
        translator = Translator()
        translations = translator.translate(value, dest='hi')
        #print(translations.text)
        #convert value to desired language
        conv_value=translations.text
        conv_dict[key]=conv_value
        #code to convert dictionary to json file using json.dump
        with open('C:/Users/Root/Desktop/data1.json','w+', encoding='utf-8') as json_file:
            json.dump(conv_dict,json_file,indent=1,ensure_ascii=False)


