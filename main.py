# HW- 1: Maheen Naqvi
# CSCI 381 - Prof. Alla

from preProcessing import *
from models import *

testfile = open("test.txt").read().splitlines()
trainSpring2023file = open("train-Spring2023.txt").read().splitlines()

# 1.1
# pre-processing:
preprocessedTestFileA = add_padding_lowercase(testfile)
preprocessedTrainFileA = add_padding_lowercase(trainSpring2023file)

# dictionary in training data
TrainingWordDictionary = count_words_in_train_file(preprocessedTrainFileA)

# replace training words
preprocessedTrainFile = replace_one_word_occurrance(preprocessedTrainFileA, TrainingWordDictionary)
preprocessedTestFile = replace_words_not_in_training(preprocessedTestFileA, preprocessedTrainFile)

# testing models
unigramDictionary = unigram(TrainingWordDictionary)
bigram_dictionary = bigram(count_words_in_train_file(preprocessedTestFile), preprocessedTestFile, False)

question1 = count_words_in_train_file(preprocessedTrainFile)
question1_A= len(question1)
print (f"question 1: {question1_A} \n")

print ("*************************")
question2 = sum(question1.values()) - question1["<s>"]
print(f"question 2: {question2} \n")

print ("*************************")
dictionaryTest = unigram(count_words_in_train_file(preprocessedTestFileA))
dictionaryTrain = unigram(count_words_in_train_file(preprocessedTrainFileA))
question3 = find_percentage_tokens(dictionaryTest, dictionaryTrain)
print(f"question 3: percentage of word tokens that did not occurred:  {question3[0]}")
print(f"question 3: percentage of word types that did not occurred: {question3[1]}")

print ("\n*************************")
testFileWithout_s = preprocessedTestFile.replace('<s>', "")
trainFileWithout_s = preprocessedTrainFile.replace('<s>', "")
dictionaryTest = bigram(count_words_in_train_file(testFileWithout_s), testFileWithout_s, False)
dictionaryTrain = bigram(count_words_in_train_file(trainFileWithout_s), trainFileWithout_s, False)
question4 = find_percentage_tokens(dictionaryTest, dictionaryTrain)
print(f"question 4| percentage of bigrams tokens that did not occurred:  {question4[0]}")
print(f"question 4| percentage of bigrams types that did not occurred: {question4[1]}")

print ("\n*************************")
processedUnigram = unigram(count_words_in_train_file(preprocessedTrainFile))
sentence = "I look forward to hearing you reply ."
q5Andq6Unigram = unigram_log_perplexity(sentence, processedUnigram)
print(f"question 5| unigram total log probability:  {q5Andq6Unigram[1]}")
print(f"question 6| unigram perplexity: {q5Andq6Unigram[0]} \n")

bigramDictionary = count_words_in_train_file(trainFileWithout_s)
bigramWithoutSmoothing = bigram(bigramDictionary, trainFileWithout_s, False)
bigramWithSmoothing = bigram(bigramDictionary, trainFileWithout_s, True)
q5Andq6BigramWithoutSmoothing= bigram_log_perplexity(sentence, bigramWithSmoothing, processedUnigram, False)

print(f"Question 5| total log probability bigram without smoothing: {q5Andq6BigramWithoutSmoothing[0]}")
print(f"parameters with zero probability: {q5Andq6BigramWithoutSmoothing[1]}")
print(f"Question 6| perplexity for bigram without smoothing: {q5Andq6BigramWithoutSmoothing[2]} \n")

q5Andq6BigramWithSmoothing= bigram_log_perplexity(sentence, bigramWithSmoothing, processedUnigram, True)
print(f"Question 5| total log prob. bi-gram with smoothing: {q5Andq6BigramWithSmoothing[0]}")
print(f"parameters with zero probability: {q5Andq6BigramWithSmoothing[1]}")
print(f"Question 6| perplexity for bigram withsmoothing: {q5Andq6BigramWithSmoothing[2]} \n")

print ("*************************")
processedUnigram = unigram(count_words_in_train_file(preprocessedTrainFile))
q7UnigramPerplexity = perplexity_unigram(preprocessedTestFile, processedUnigram)
print(f"Question 7| unigram perplexity: {q7UnigramPerplexity}")

preprocessedTestFile = preprocessedTestFile.replace('<s>', "")
q7PerplexityBigramWithoutSmoothing = perplexity_bigram(preprocessedTestFile, bigramWithoutSmoothing, processedUnigram, False)
print(f"Question 7| bigram without smoothing perplexity: {q7PerplexityBigramWithoutSmoothing}")

preprocessedTestFile = preprocessedTestFile.replace('<s>', "")
q7PerplexityBigramWithSmoothing = perplexity_bigram(preprocessedTestFile, bigramWithSmoothing, processedUnigram, True)
print(f"Question 7| bigram with smoothing perplexity: {q7PerplexityBigramWithSmoothing} \n")
print ("*************************")