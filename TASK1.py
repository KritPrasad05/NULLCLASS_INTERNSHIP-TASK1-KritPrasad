from transformers import MarianMTModel, MarianTokenizer
import streamlit as st

stl.set_page_config(page_title="Task-1",layout="wide", initial_sidebar_state="auto", menu_items=None)

model_name = 'Helsinki-NLP/opus-mt-en-fr'
#loading Pre-trained model and tokenizer
model_en_fr = MarianMTModel.from_pretrained(model_name)
tokenizer_en_fr = MarianTokenizer.from_pretrained(model_name)

st.title("Translation English to French")

#Creating an english sentence to translate
sentence = st.text_input("Enter the Text to translate to French")

if sentence:
    # Tokenize the input sentence
    encoded_sentence = tokenizer_en_fr(sentence, return_tensors='pt')
    
    generated_tokens = model_en_fr.generate(**encoded_sentence)
    translated_sentence = tokenizer_en_fr.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    
    st.write("English Sentence:",sentence)
    st.write("Translated French Sentence:",translated_sentence)
