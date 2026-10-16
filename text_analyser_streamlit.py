
import streamlit as st
import pandas as pd
import re
from collections import Counter

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Text DNA Analyzer",
    page_icon="🧬",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
    .stApp {
        background-color: #f7f7f3;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    .hero {
        text-align: center;
        padding: 25px 0 30px 0;
    }

    .hero h1 {
        font-size: 3.2rem;
        font-weight: 750;
        letter-spacing: -2px;
        color: #181818;
        margin-bottom: 5px;
    }

    .hero p {
        font-size: 1.05rem;
        color: #666666;
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #222222;
        margin-top: 20px;
        margin-bottom: 12px;
    }

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #e5e5df;
        padding: 18px;
        border-radius: 14px;
    }

    div[data-testid="stMetricLabel"] {
        color: #666666;
    }

    .report-card {
        background: white;
        border: 1px solid #e5e5df;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 12px;
    }

    .footer {
        text-align: center;
        color: #888888;
        font-size: 0.85rem;
        padding-top: 35px;
    }

    div.stButton > button[kind="primary"] {
        background-color: #202020;
        border: none;
        border-radius: 10px;
        min-height: 45px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown("""
<div class="hero">
    <h1>🧬 Text DNA</h1>
    <p>Discover the patterns, structure and vocabulary hidden in your writing.</p>
</div>
""", unsafe_allow_html=True)


# ---------------- TEXT INPUT ----------------

st.markdown(
    '<div class="section-title">Your text</div>',
    unsafe_allow_html=True
)

text = st.text_area(
    "Enter text",
    placeholder="Paste your paragraph, essay, story or other writing here...",
    height=220,
    label_visibility="collapsed"
)

col1, col2 = st.columns([1, 5])

with col1:
    analyze = st.button(
        "🧬 Analyze Text",
        type="primary",
        use_container_width=True
    )

with col2:
    st.caption("Your analysis runs locally in this Streamlit app.")


# ---------------- ANALYSIS ----------------

if analyze:

    if not text.strip():
        st.warning("Please enter some text before analyzing it.")

    else:
        # Basic statistics
        total_characters = len(text)
        original_words = text.split()
        total_words = len(original_words)

        # Normalize words and remove surrounding punctuation
        clean_words = [
            word.strip(".,!?;:\"'()[]{}")
            for word in text.lower().split()
        ]

        # Ignore empty tokens, such as standalone punctuation
        clean_words = [word for word in clean_words if word]

        if not clean_words:
            st.warning("Please enter some actual words to analyze.")

        else:
            # Word frequency
            frequency = Counter(clean_words)
            unique_words = set(clean_words)

            vocabulary_size = len(unique_words)

            vocabulary_diversity = (
                vocabulary_size / len(clean_words)
            )

            diversity_percentage = vocabulary_diversity * 100

            # Word length analysis
            longest_word = max(clean_words, key=len)
            shortest_word = min(clean_words, key=len)

            total_letters = sum(len(word) for word in clean_words)
            average_word_length = total_letters / len(clean_words)

            # Punctuation analysis
            punctuation_symbols = ".,!?;:\"'()[]{}"

            punctuation_count = sum(
                1 for char in text
                if char in punctuation_symbols
            )

            punctuation_frequency = {
                symbol: text.count(symbol)
                for symbol in ".,!?;"
            }

            # Character analysis
            vowel_count = sum(
                1 for char in text.lower()
                if char in "aeiou"
            )

            uppercase_count = sum(
                1 for char in text
                if char.isupper()
            )

            lowercase_count = sum(
                1 for char in text
                if char.islower()
            )

            digit_count = sum(
                1 for char in text
                if char.isdigit()
            )

            # Approximate sentence analysis
            sentences = [
                sentence.strip()
                for sentence in re.split(r'[.!?]+', text)
                if sentence.strip()
            ]

            sentence_count = len(sentences)

            average_sentence_length = (
                len(clean_words) / sentence_count
                if sentence_count > 0
                else len(clean_words)
            )

            # Custom readability heuristic
            readability = 0

            if average_sentence_length < 12:
                readability += 1
            elif average_sentence_length < 20:
                readability += 2
            else:
                readability += 3

            if diversity_percentage > 50:
                readability += 1
            elif diversity_percentage > 30:
                readability += 2
            else:
                readability += 3

            # Simple keyword-based tonality heuristic
            positive_words = {
                "good", "great", "excellent"
            }

            negative_words = {
                "bad", "poor", "terrible"
            }

            tonality_score = 0

            if positive_words.intersection(clean_words):
                tonality_score += 1

            if negative_words.intersection(clean_words):
                tonality_score -= 1

            # Word-choice heuristic
            if average_word_length > 5:
                word_choice_score = 1
            elif average_word_length > 3:
                word_choice_score = 2
            else:
                word_choice_score = 3

            overall_score = (
                readability
                + tonality_score
                + word_choice_score
            )

            # ---------------- RESULTS ----------------

            st.divider()

            st.markdown(
                '<div class="section-title">Your text at a glance</div>',
                unsafe_allow_html=True
            )

            m1, m2, m3, m4 = st.columns(4)

            m1.metric("Characters", f"{total_characters:,}")
            m2.metric("Words", f"{len(clean_words):,}")
            m3.metric("Unique Words", f"{vocabulary_size:,}")
            m4.metric("Vocabulary Diversity", f"{diversity_percentage:.1f}%")

            # Word analysis
            st.markdown(
                '<div class="section-title">Word DNA</div>',
                unsafe_allow_html=True
            )

            c1, c2, c3 = st.columns(3)

            c1.metric("Longest Word", longest_word)
            c2.metric("Shortest Word", shortest_word)
            c3.metric("Average Word Length", f"{average_word_length:.2f}")

            # Frequency chart and table
            st.markdown(
                '<div class="section-title">Word Frequency</div>',
                unsafe_allow_html=True
            )

            frequency_df = pd.DataFrame(
                frequency.most_common(10),
                columns=["Word", "Frequency"]
            )

            chart_col, table_col = st.columns([3, 2])

            with chart_col:
                st.bar_chart(
                    frequency_df.set_index("Word"),
                    horizontal=True
                )

            with table_col:
                st.dataframe(
                    frequency_df,
                    hide_index=True,
                    use_container_width=True
                )

            # Character and punctuation analysis
            st.markdown(
                '<div class="section-title">Character DNA</div>',
                unsafe_allow_html=True
            )

            c1, c2, c3, c4 = st.columns(4)

            c1.metric("Vowels", vowel_count)
            c2.metric("Uppercase", uppercase_count)
            c3.metric("Lowercase", lowercase_count)
            c4.metric("Digits", digit_count)

            punctuation_df = pd.DataFrame(
                list(punctuation_frequency.items()),
                columns=["Punctuation", "Count"]
            )

            with st.expander("View punctuation breakdown"):
                st.dataframe(
                    punctuation_df,
                    hide_index=True,
                    use_container_width=True
                )

                st.write(
                    "Total punctuation marks:",
                    punctuation_count
                )

            # Writing style
            st.markdown(
                '<div class="section-title">Writing DNA</div>',
                unsafe_allow_html=True
            )

            if diversity_percentage >= 80:
                vocabulary_label = "Highly Diverse"
            elif diversity_percentage >= 60:
                vocabulary_label = "Moderately Diverse"
            else:
                vocabulary_label = "Repetitive"

            if average_word_length >= 7:
                word_choice_label = "Long-word-heavy"
            elif average_word_length >= 5:
                word_choice_label = "Moderate"
            else:
                word_choice_label = "Short-word-heavy"

            if tonality_score > 0:
                tone_label = "Positive keywords detected"
            elif tonality_score < 0:
                tone_label = "Negative keywords detected"
            else:
                tone_label = "No net sentiment keywords detected"

            c1, c2 = st.columns(2)

            with c1:
                st.markdown('<div class="report-card">', unsafe_allow_html=True)
                st.subheader("Vocabulary")
                st.write(vocabulary_label)
                st.write(f"Vocabulary size: {vocabulary_size}")
                st.write(f"Type-token ratio: {vocabulary_diversity:.2f}")
                st.markdown('</div>', unsafe_allow_html=True)

                st.markdown('<div class="report-card">', unsafe_allow_html=True)
                st.subheader("Sentence Structure")
                st.write(f"Sentences detected: {sentence_count}")
                st.write(
                    f"Average words per sentence: "
                    f"{average_sentence_length:.2f}"
                )
                st.markdown('</div>', unsafe_allow_html=True)

            with c2:
                st.markdown('<div class="report-card">', unsafe_allow_html=True)
                st.subheader("Word Choice")
                st.write(word_choice_label)
                st.write(f"Average word length: {average_word_length:.2f}")
                st.markdown('</div>', unsafe_allow_html=True)

                st.markdown('<div class="report-card">', unsafe_allow_html=True)
                st.subheader("Keyword-based Tone")
                st.write(tone_label)
                st.caption(
                    "This basic method checks a small set of keywords; "
                    "it does not understand context or reliably detect emotion."
                )
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown(
                '<div class="section-title">Analysis Scores</div>',
                unsafe_allow_html=True
            )

            s1, s2, s3 = st.columns(3)

            s1.metric("Readability Heuristic", f"{readability}/6")
            s2.metric("Tone Score", f"{tonality_score:+d}")
            s3.metric("Combined Score", overall_score)

            st.caption(
                "These are custom educational heuristics, not validated "
                "readability or writing-quality scores."
            )

            # Download report
            report = f"""TEXT DNA ANALYZER REPORT

Characters: {total_characters}
Words: {len(clean_words)}
Unique words: {vocabulary_size}
Vocabulary diversity: {diversity_percentage:.2f}%

Longest word: {longest_word}
Shortest word: {shortest_word}
Average word length: {average_word_length:.2f}

Vowels: {vowel_count}
Punctuation marks: {punctuation_count}
Uppercase characters: {uppercase_count}
Lowercase characters: {lowercase_count}
Digits: {digit_count}

Sentences detected: {sentence_count}
Average words per sentence: {average_sentence_length:.2f}

Vocabulary assessment: {vocabulary_label}
Word choice assessment: {word_choice_label}
Keyword-based tone: {tone_label}

Readability heuristic: {readability}
Tone score: {tonality_score}
Combined score: {overall_score}

WORD FREQUENCY
""" + "\n".join(
                f"{word}: {count}"
                for word, count in frequency.most_common()
            )

            st.download_button(
                "⬇ Download Analysis Report",
                data=report,
                file_name="text_dna_report.txt",
                mime="text/plain",
                use_container_width=True
            )

            st.success("Text analysis completed successfully!")


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    TEXT DNA ANALYZER · Built with Python and Streamlit
</div>
""", unsafe_allow_html=True)
