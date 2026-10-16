print("Welcome to the text analyser!")
print("This program will help you analyze the text you provide.")
print("The benefits of using this program include:")
print("- Identifying key themes and topics")
print("- Analyzing sentiment and emotional tone")
print("- Understanding writing style and structure")
print("Let's get started!")

print("Please enter the text you want to analyze:")
text = input()
print(f"You entered: {text}")

total_words=len(text.split())
print("The total number of words in the text is:", total_words)

total_characters=len(text)
print("The total number of characters in the text is:", total_characters)

clean_words = [word.strip(".,!?;:\"'()[]{}") for word in text.lower().split()]
frequency = {}
for word in clean_words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("The frequency of each word in the text is:", frequency)

vowel_count = sum(1 for char in text.lower() if char in "aeiou")
print("The total number of vowels in the text is:", vowel_count)

vocabulary_diversity=len(set(clean_words)) / total_words
print("The vocabulary diversity of the text is:", vocabulary_diversity)

vocabulary_diversity_percentage=vocabulary_diversity * 100
print("The vocabulary diversity percentage of the text is:", vocabulary_diversity_percentage, "%")

longest_word=max(clean_words, key=len)
print("The longest word in the text is:", longest_word)

shortest_word=min(clean_words, key=len)
print("The shortest word in the text is:", shortest_word)

average_word_length=total_characters / total_words
print("The average word length in the text is:", average_word_length)

punctuation_count=sum(1 for char in text if char in ".,!?;:\"'()[]{}")
print("The number of punctuation marks in the text is:", punctuation_count)

print("Writing Style Analysis:")
print("In this section, we will analyze the writing style of the text based on sentence structure, word choice, and overall readability.")

readability=0
if total_words > 0:
    average_sentence_length = total_words / text.count('.') if text.count('.') > 0 else total_words
    if average_sentence_length < 12:
        readability += 1
    elif average_sentence_length < 20:
        readability += 2
    else:
        readability += 3

    if vocabulary_diversity_percentage > 50:
        readability += 1
    elif vocabulary_diversity_percentage > 30:
        readability += 2
    else:
        readability += 3

print("The readability score of the text is:", readability)

capitalization_count=sum(1 for char in text if char.isupper())
print("The number of capitalized letters in the text is:", capitalization_count)

lowercase_count=sum(1 for char in text if char.islower())
print("The number of lowercase letters in the text is:", lowercase_count)

uppercase_count=sum(1 for char in text if char.isupper())
print("The number of uppercase letters in the text is:", uppercase_count)

tonality_score=0
if "good" in clean_words or "great" in clean_words or "excellent" in clean_words:
    tonality_score += 1
if "bad" in clean_words or "poor" in clean_words or "terrible" in clean_words:
    tonality_score -= 1
print("The tonality score of the text is:", tonality_score)

word_choice_score=0
if average_word_length>5:
    word_choice_score += 1
elif average_word_length>3:
    word_choice_score += 2
else:
    word_choice_score += 3
print("The word choice score of the text is:", word_choice_score)

print("Overall Writing Style Score:", readability + tonality_score + word_choice_score)

print("Summary of the analysis:")
print("- The frequency of each word in the text is:", frequency)
print("- The total number of vowels in the text is:", vowel_count)
print("- The vocabulary diversity of the text is:", vocabulary_diversity)
print("- The vocabulary diversity percentage of the text is:", vocabulary_diversity_percentage, "%")
print("- The longest word in the text is:", longest_word)
print("- The shortest word in the text is:", shortest_word)
print("- The average word length in the text is:", average_word_length)
print("- The number of punctuation marks in the text is:", punctuation_count)
print("- The number of capitalized letters in the text is:", capitalization_count)
print("- The number of lowercase letters in the text is:", lowercase_count)
print("- The number of uppercase letters in the text is:", uppercase_count)
print("- The readability score of the text is:", readability)
print("- The tonality score of the text is:", tonality_score)
print("- The word choice score of the text is:", word_choice_score)
print("- Overall Writing Style Score:", readability + tonality_score + word_choice_score)

print("Thank you for using the text analyser! We hope this analysis helps you improve your writing skills and gain insights into your text.")