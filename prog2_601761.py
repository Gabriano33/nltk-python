#Gabriele Pergola, 601761

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from collections import Counter
from nltk.util import ngrams
import os

# da decommentare solo la prima volta che si esegue il codice; inoltre installa il modulo numpy tramite "pip install numpy"
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

# Funzione di preprocessamento del testo
def preprocess_text(text):
    sentences = sent_tokenize(text)
    tokens = [word.lower() for sent in sentences for word in word_tokenize(sent) if word.isalnum()]
    return tokens, sentences

# Funzione per ottenere le parole più frequenti per determinate categorie grammaticali
def get_frequent_words(pos_tagged_tokens, pos_list, top_n=50):
    filtered_words = [word for word, tag in pos_tagged_tokens if tag in pos_list]
    word_counts = Counter(filtered_words)
    return word_counts.most_common(top_n)

# Funzione per ottenere i n-grammi più frequenti
def get_ngrams(tokens, n, top_n=20):
    ngrams_list = list(ngrams(tokens, n))
    ngrams_counts = Counter(ngrams_list)
    return ngrams_counts.most_common(top_n)

# Funzione per ottenere i n-grammi di PoS più frequenti
def get_pos_ngrams(pos_tagged_tokens, n, top_n=20):
    pos_sequences = list(ngrams([pos for word, pos in pos_tagged_tokens], n))
    pos_counts = Counter(pos_sequences)
    return pos_counts.most_common(top_n)

# Funzione per estrarre bigrammi composti da aggettivo e sostantivo
def extract_adj_noun_bigrams(pos_tagged_tokens, adjective_tags, noun_tags):
    bigrams = []
    for i in range(len(pos_tagged_tokens) - 1):
        word1, tag1 = pos_tagged_tokens[i]
        word2, tag2 = pos_tagged_tokens[i + 1]
        if tag1 in adjective_tags and tag2 in noun_tags:
            bigrams.append((word1, word2))
    return bigrams

# Funzione per calcolare le frequenze dei bigrammi
def get_bigram_frequencies(bigrams):
    bigram_counts = Counter(bigrams)
    return bigram_counts.most_common(10)

# Funzione per calcolare misure di associazione per i bigrammi
def calculate_bigram_measures(bigram_freq, token_freq):
    bigram_measures = {}
    total_tokens = sum(token_freq.values())
    for bigram, freq in bigram_freq.items():
        word1, word2 = bigram
        p_word1 = token_freq[word1] / total_tokens
        p_word2 = token_freq[word2] / total_tokens
        p_bigram = freq / total_tokens
        cond_prob = freq / token_freq[word1]
        joint_prob = p_bigram
        mi = p_bigram / (p_word1 * p_word2)
        lmi = freq * (mi)
        bigram_measures[bigram] = {
            'freq': freq,
            'cond_prob': cond_prob,
            'joint_prob': joint_prob,
            'mi': mi,
            'lmi': lmi
        }
    return bigram_measures

# Funzione per ordinare i bigrammi per una misura specifica
def sort_bigrams_by_measure(bigram_measures, measure):
    sorted_bigrams = []
    for bigram in bigram_measures:
        sorted_bigrams.append((bigram, bigram_measures[bigram][measure]))
    sorted_bigrams.sort(key=lambda x: x[1], reverse=True)
    return sorted_bigrams[:10]

# Funzione per trovare frasi con condizioni specifiche
def find_sentences_with_conditions(sentences, token_freq):
    valid_sentences = []
    for sentence in sentences:
        tokens = word_tokenize(sentence)
        if 10 <= len(tokens) <= 20:
            non_hapax_tokens = [token for token in tokens if token_freq[token] > 1]
            if len(non_hapax_tokens) >= len(tokens) // 2:
                valid_sentences.append(sentence)
    return valid_sentences

# Funzione per trovare le frasi con la media della distribuzione di frequenza più alta e più bassa
def find_extreme_avg_freq_sentences(valid_sentences, token_freq):
    max_avg_freq = 0
    min_avg_freq = float('inf')
    max_avg_freq_sentence = ""
    min_avg_freq_sentence = ""

    for sentence in valid_sentences:
        tokens = word_tokenize(sentence)
        avg_freq = sum(token_freq[token] for token in tokens) / len(tokens)

        if avg_freq > max_avg_freq:
            max_avg_freq = avg_freq
            max_avg_freq_sentence = sentence

        if avg_freq < min_avg_freq:
            min_avg_freq = avg_freq
            min_avg_freq_sentence = sentence

    return max_avg_freq_sentence, min_avg_freq_sentence

# Funzione per costruire un modello di Markov di ordine 2
def build_markov_model(tokens):
    model = {}
    for i in range(len(tokens) - 2):
        trigram = (tokens[i], tokens[i + 1], tokens[i + 2])
        bigram = (tokens[i], tokens[i + 1])
        if bigram not in model:
            model[bigram] = Counter()
        model[bigram][tokens[i + 2]] += 1

    # Convertire i contatori in probabilità
    for bigram in model:
        total_count = float(sum(model[bigram].values()))
        for word in model[bigram]:
            model[bigram][word] /= total_count

    return model

# Funzione per calcolare la probabilità di una frase secondo un modello di Markov di ordine 2
def calculate_sentence_probability(sentence, model):
    tokens = word_tokenize(sentence)
    prob = 1.0

    for i in range(len(tokens) - 2):
        bigram = (tokens[i], tokens[i + 1])
        next_word = tokens[i + 2]
        if bigram in model and next_word in model[bigram]:
            prob *= model[bigram][next_word]
        else:
            prob *= 0.0

    return prob

# Funzione per trovare la frase con la probabilità più alta secondo un modello di Markov di ordine 2
def find_max_prob_sentence(valid_sentences, tokens):
    model = build_markov_model(tokens)
    max_prob = 0.0
    max_prob_sentence = None

    for sentence in valid_sentences:
        prob = calculate_sentence_probability(sentence, model)
        if prob > max_prob:
            max_prob = prob
            max_prob_sentence = sentence

    return max_prob_sentence if max_prob_sentence else valid_sentences[0] if valid_sentences else "Nessuna frase trovata"

# Funzione per scrivere i risultati su un file di testo nella stessa cartella del programma
def write_results_to_file(results, output_file):
    script_dir = os.path.dirname(__file__)  # Ottiene il percorso della cartella del programma
    output_path = os.path.join(script_dir, output_file)  # Unisce il percorso della cartella del programma con il nome del file
    with open(output_path, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(result + "\n\n\n\n")  # Aggiunge una riga vuota tra ciascun risultato

# Funzione per estrarre le entità nominate e contare le frequenze
def extract_named_entities(sentences):
    ne_list = []
    for sentence in sentences:
        chunks = ne_chunk(pos_tag(word_tokenize(sentence)))
        for chunk in chunks:
            if hasattr(chunk, 'label'):
                ne_list.append((chunk.label(), ' '.join(c[0] for c in chunk)))
    return ne_list

# Funzione per ottenere le 15 entità nominate più frequenti per ciascuna classe
def get_top_named_entities(ne_list, top_n=15):
    ne_counts = Counter(ne_list)
    ne_classes = {}
    for (ne_class, ne), count in ne_counts.items():
        if ne_class not in ne_classes:
            ne_classes[ne_class] = []
        ne_classes[ne_class].append((ne, count))
    
    for ne_class in ne_classes:
        ne_classes[ne_class].sort(key=lambda x: x[1], reverse=True)
        ne_classes[ne_class] = ne_classes[ne_class][:top_n]
    
    return ne_classes

def main():
    # Input del corpus di testo
    corpus_path = input("Inserisci il path del corpus da elaborare: ")
    with open(corpus_path, 'r', encoding='utf-8') as file:
        corpus = file.read()

    # Preprocessamento del testo
    tokens, sentences = preprocess_text(corpus)

    # Tagging delle parti del discorso (PoS)
    pos_tagged_tokens = pos_tag(tokens)

    # Creazione delle liste di categorie grammaticali
    noun_tags = ['NN', 'NNS', 'NNP', 'NNPS']
    adjective_tags = ['JJ', 'JJR', 'JJS']
    adverb_tags = ['RB', 'RBR', 'RBS']

    # Estrazione delle parole più frequenti per ogni categoria grammaticale
    top_nouns = get_frequent_words(pos_tagged_tokens, noun_tags)
    top_adjectives = get_frequent_words(pos_tagged_tokens, adjective_tags)
    top_adverbs = get_frequent_words(pos_tagged_tokens, adverb_tags)

    # Risultati delle parole più frequenti
    results = []
    results.append("Top 50 Sostantivi: " + str(top_nouns))
    results.append("Top 50 Avverbi: " + str(top_adverbs))
    results.append("Top 50 Aggettivi: " + str(top_adjectives))

    # Estrazione dei top-20 n-grammi per n = [2, 3, 4, 5, 6]
    for n in range(2, 7):
        top_ngrams = get_ngrams(tokens, n)
        results.append(f"Top 20 {n}-grammi: " + str(top_ngrams))

    # Estrazione dei top-20 n-grammi di PoS per n = [1, 2, 3]
    for n in range(1, 4):
        top_pos_ngrams = get_pos_ngrams(pos_tagged_tokens, n)
        results.append(f"Top 20 {n}-grammi di PoS: " + str(top_pos_ngrams))

    # Estrazione dei bigrammi aggettivo-sostantivo
    adj_noun_bigrams = extract_adj_noun_bigrams(pos_tagged_tokens, adjective_tags, noun_tags)
    bigram_freq = Counter(adj_noun_bigrams)

    # Calcolo delle misure di associazione per i bigrammi
    token_freq = Counter(tokens)
    bigram_measures = calculate_bigram_measures(bigram_freq, token_freq)

    # Ordina i bigrammi per le varie misure
    sorted_by_freq = sort_bigrams_by_measure(bigram_measures, 'freq')
    sorted_by_cond_prob = sort_bigrams_by_measure(bigram_measures, 'cond_prob')
    sorted_by_joint_prob = sort_bigrams_by_measure(bigram_measures, 'joint_prob')
    sorted_by_mi = sort_bigrams_by_measure(bigram_measures, 'mi')
    sorted_by_lmi = sort_bigrams_by_measure(bigram_measures, 'lmi')

    results.append("Top 10 bigrammi (aggettivo-sostantivo) per frequenza: " + str(sorted_by_freq))
    results.append("Top 10 bigrammi (aggettivo-sostantivo) per probabilità condizionata: " + str(sorted_by_cond_prob))
    results.append("Top 10 bigrammi (aggettivo-sostantivo) per probabilità congiunta: " + str(sorted_by_joint_prob))
    results.append("Top 10 bigrammi (aggettivo-sostantivo) per MI: " + str(sorted_by_mi))
    results.append("Top 10 bigrammi (aggettivo-sostantivo) per LMI: " + str(sorted_by_lmi))

    # Numero di elementi comuni tra top 10 per MI e LMI
    top_mi_set = set([bigram for bigram, _ in sorted_by_mi])
    top_lmi_set = set([bigram for bigram, _ in sorted_by_lmi])
    common_elements_mi_lmi = top_mi_set.intersection(top_lmi_set)
    results.append("Numero di elementi comuni tra top 10 per MI e LMI: " + str(len(common_elements_mi_lmi)))

    # Trovare frasi valide con condizioni
    valid_sentences = find_sentences_with_conditions(sentences, token_freq)

    # Trovare frasi con media distribuzione di frequenza più alta e più bassa
    max_avg_freq_sentence, min_avg_freq_sentence = find_extreme_avg_freq_sentences(valid_sentences, token_freq)
    results.append("Frase con media distribuzione di frequenza più alta: " + max_avg_freq_sentence)
    results.append("Frase con media distribuzione di frequenza più bassa: " + min_avg_freq_sentence)

    # Trovare frase con probabilità più alta secondo un modello di Markov di ordine 2
    max_prob_sentence = find_max_prob_sentence(valid_sentences, tokens)
    if max_prob_sentence:
        results.append("Frase con probabilità più alta secondo un modello di Markov di ordine 2: " + max_prob_sentence)
    else:
        results.append("Nessuna frase trovata.")

    # Estrazione delle entità nominate
    named_entities = extract_named_entities(sentences)
    top_named_entities = get_top_named_entities(named_entities)
    results.append("Top 15 entità nominate per ciascuna classe: " + str(top_named_entities))

    # Scrittura dei risultati su un file di testo
    output_file = "risultati_prog2_601761.txt"
    write_results_to_file(results, output_file)

# Esecuzione del programma principale
if __name__ == "__main__":
    main()
