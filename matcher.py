import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    doc = nlp(text.lower())
    tokens = [token.text for token in doc if not token.is_stop and token.is_alpha]
    return ' '.join(tokens)

def calculate_similarity(resume_text, jd_text):
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(jd_text)

    vectorizer = CountVectorizer().fit_transform([cleaned_resume, cleaned_jd])
    vectors = vectorizer.toarray()

    return cosine_similarity([vectors[0]], [vectors[1]])[0][0]
