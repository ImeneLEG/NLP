

# Mise en minuscules
df['text_cleaned'] = df['text'].str.lower()

# Suppression des ponctuations, des émojis, des émoticônes, des URL et des balises HTML
def remove_special_characters(text):
    text = re.sub(r'http\S+', '', text)  # Supprimer les URL
    text = re.sub(r'<.*?>', '', text)  # Supprimer les balises HTML
    text = re.sub(r'[^\w\s]', '', text)  # Supprimer la ponctuation
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Supprimer les caractères non ASCII (émojis, etc.)
    return text

df['text_cleaned'] = df['text_cleaned'].apply(remove_special_characters)

# Tokenization
df['tokens'] = df['text_cleaned'].apply(word_tokenize)

# Suppression des mots vides (stopwords)
stop_words = set(stopwords.words('english'))
df['tokens'] = df['tokens'].apply(lambda x: [word for word in x if word not in stop_words])

# Comptage des mots pour la suppression des mots rares
word_freq = Counter()
for tokens in df['tokens']:
    word_freq.update(tokens)

# Définition du seuil pour les mots rares
threshold_rare = 10  # Vous pouvez ajuster ce seuil en fonction de votre corpus et de vos besoins

# Suppression des mots rares
rare_words = set([word for word, freq in word_freq.items() if freq <= threshold_rare])
df['tokens'] = df['tokens'].apply(lambda x: [word for word in x if word not in rare_words])

# Stemming
stemmer = PorterStemmer()
df['stemmed_tokens'] = df['tokens'].apply(lambda x: [stemmer.stem(word) for word in x])

# Lemmatisation
lemmatizer = WordNetLemmatizer()
df['lemmatized_tokens'] = df['tokens'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])

# Affichage du DataFrame avec les colonnes nettoyées
print(df.head())

# Enregistrement du DataFrame dans un fichier CSV
df[['tweet_id', 'text', 'text_cleaned']].to_csv('preprocessed_data.csv', index=False)
