#Gabriele Pergola, 601761

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string
import os

# Scarica i dataset necessari nltk (scommenta queste righe solo la prima volta che esegui il codice)
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('vader_lexicon')

# Funzione per leggere il testo da un file
def read_text_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        text = file.read()
    return text

# Funzione per pre-processare il testo: tokenizzazione e pulizia
def preprocess_text(text):
    # Tokenizza il testo in frasi
    sentences = sent_tokenize(text)
    # Tokenizza le frasi in parole, rimuove la punteggiatura e trasforma in minuscolo
    tokens = [word.lower() for sent in sentences for word in word_tokenize(sent) if word.isalnum()]
    return tokens, sentences

# Funzione per ottenere hapax (parole che appaiono una sola volta) dai primi n token
def get_hapax(tokens, n):
    freq_dist = FreqDist(tokens[:n])
    hapax = freq_dist.hapaxes()
    return hapax

# Funzione per calcolare il Type-Token Ratio (TTR) in incrementi di step token
def calculate_ttr(tokens, step=200):
    ttr_values = []
    for i in range(step, len(tokens) + 1, step):
        unique_tokens = set(tokens[:i])
        ttr = len(unique_tokens) / i
        ttr_values.append((i, ttr))
    return ttr_values

# Funzione per calcolare la distribuzione delle frasi positive e negative
def sentiment_distribution(sentences):
    sia = SentimentIntensityAnalyzer()
    positive = 0
    negative = 0
    
    for sentence in sentences:
        score = sia.polarity_scores(sentence)
        if score['compound'] >= 0.05:
            positive += 1
        elif score['compound'] <= -0.05:
            negative += 1
    return positive, negative

# Funzione per calcolare le statistiche del testo
def calculate_statistics(tokens, sentences, lemmatizer):
    num_tokens = len(tokens)
    num_sentences = len(sentences)
    avg_sentence_length = sum(len(word_tokenize(sent)) for sent in sentences) / num_sentences
    filtered_tokens = [token for token in tokens if token not in string.punctuation]
    avg_token_length = sum(len(token) for token in filtered_tokens) / len(filtered_tokens)
    hapax_500 = get_hapax(tokens, 500)
    hapax_1000 = get_hapax(tokens, 1000)
    hapax_3000 = get_hapax(tokens, 3000)
    hapax_total = get_hapax(tokens, len(tokens))
    vocab_size = len(set(tokens))
    ttr = calculate_ttr(tokens)
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    distinct_lemmas = len(set(lemmas))
    positive_sentences, negative_sentences = sentiment_distribution(sentences)

    return {
        "num_sentences": num_sentences,
        "num_tokens": num_tokens,
        "avg_sentence_length": avg_sentence_length,
        "avg_token_length": avg_token_length,
        "hapax_500": len(hapax_500),
        "hapax_1000": len(hapax_1000),
        "hapax_3000": len(hapax_3000),
        "hapax_total": len(hapax_total),
        "vocab_size": vocab_size,
        "ttr": ttr,
        "distinct_lemmas": distinct_lemmas,
        "positive_sentences": positive_sentences,
        "negative_sentences": negative_sentences
    }

# Funzione per stampare i risultati dell'analisi
def results_printing(results, corpus_title):
    print(f"\nAnalisi del testo: {corpus_title}")
    print("================================")
    print(f"Numero di frasi nel corpus: {results['num_sentences']}")
    print(f"Numero di token nel corpus: {results['num_tokens']}")
    print(f"Lunghezza media delle frasi nel corpus: {results['avg_sentence_length']}")
    print(f"Lunghezza media dei token nel corpus: {results['avg_token_length']}")
    print(f"Numero di hapax nei primi 500 token: {results['hapax_500']}")
    print(f"Numero di hapax nei primi 1000 token: {results['hapax_1000']}")
    print(f"Numero di hapax nei primi 3000 token: {results['hapax_3000']}")
    print(f"Numero di hapax nel corpus: {results['hapax_total']}")
    print("Dimensioni del vocabolario per porzioni incrementali di 200 tokens:")
    for (i, ttr) in results['ttr']:
        print(f"  {i} tokens: {ttr}")
    print(f"Numero di lemmi distinti nel corpus: {results['distinct_lemmas']}")
    print(f"Numero di frasi con polarità negativa nel corpus: {results['negative_sentences']}")
    print(f"Numero di frasi con polarità positiva nel corpus: {results['positive_sentences']}")

# Funzione per scrivere i risultati dell'analisi su un file
def results_writing_on_file(results, corpus_title):
    # Ottiene la directory corrente del file script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Imposta il percorso del file di output
    output_file_path = os.path.join(current_directory, 'risultati_prog1_601761.txt')
    
    with open(output_file_path, 'a', encoding='utf-8') as file:
        file.write(f"\nAnalisi del corpus: {corpus_title}\n")
        file.write("================================" + "\n")
        file.write(f"Numero di frasi nel corpus: {results['num_sentences']}\n")
        file.write(f"Numero di token nel corpus: {results['num_tokens']}\n")
        file.write(f"Lunghezza media delle frasi nel corpus: {results['avg_sentence_length']}\n")
        file.write(f"Lunghezza media dei token nel corpus: {results['avg_token_length']}\n")
        file.write(f"Numero di hapax nei primi 500 token: {results['hapax_500']}\n")
        file.write(f"Numero di hapax nei primi 1000 token: {results['hapax_1000']}\n")
        file.write(f"Numero di hapax nei primi 3000 token: {results['hapax_3000']}\n")
        file.write(f"Numero di hapax nel corpus: {results['hapax_total']}\n")
        file.write("Dimensioni del vocabolario per porzioni incrementali di 200 tokens:\n")
        for (i, ttr) in results['ttr']:
            file.write(f"  {i} tokens: {ttr}\n")
        file.write(f"Numero di lemmi distinti nel corpus: {results['distinct_lemmas']}\n")
        file.write(f"Numero di frasi con polarità negativa nel corpus: {results['negative_sentences']}\n")
        file.write(f"Numero di frasi con polarità positiva nel corpus: {results['positive_sentences']}\n")

# Funzione principale che esegue tutte le operazioni
def main():
    # Richiede i percorsi dei file di testo all'utente
    file1 = input("Inserisci il percorso del primo file di testo (.txt): ")
    file2 = input("Inserisci il percorso del secondo file di testo (.txt): ")

    # Legge i testi dai file
    text1 = read_text_file(file1)
    text2 = read_text_file(file2)

    # Pre-processa i testi
    tokens1, sentences1 = preprocess_text(text1)
    tokens2, sentences2 = preprocess_text(text2)

    # Crea un lemmatizzatore
    lemmatizer = WordNetLemmatizer()

    # Calcola le statistiche per entrambi i testi
    stats1 = calculate_statistics(tokens1, sentences1, lemmatizer)
    stats2 = calculate_statistics(tokens2, sentences2, lemmatizer)

    # Stampa e scrive i risultati dell'analisi del primo testo
    results_printing(stats1, "Primo Corpus, The Trap by H.P. Lovecraft")
    results_writing_on_file(stats1, "Primo Corpus, The Trap by H.P. Lovecraft")

    # Stampa e scrive i risultati dell'analisi del secondo testo
    results_printing(stats2, "Secondo Corpus, The Inequality of Human Races by Arthur de Gobineau")
    results_writing_on_file(stats2, "Secondo Corpus, The Inequality of Human Races by Arthur de Gobineau")

# Esegui la funzione principale se il file viene eseguito come script
if __name__ == "__main__":
    main()
