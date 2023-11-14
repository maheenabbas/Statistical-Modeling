# HW- 1: Maheen Naqvi
# CSCI 381 - Prof. Alla
#preProcessing
import math

def add_padding_lowercase(input_file):
  padded_input = ""
  for sentence in input_file:
    padded_input += (' <s> ' + sentence.lower() + ' </s>')
  return padded_input

def count_words_in_train_file(input_file):
  word_dictionary = {}
  sentence = input_file.split()

  for word in sentence:
    if word in word_dictionary:
      word_dictionary[word] += 1
    else:
      word_dictionary[word] = 1
  return word_dictionary

def replace_one_word_occurrance(input_file, dictionary):
  return_input = ""
  sentence = input_file.split()
  is_previous_word_unk = False
  for word in sentence:
    if word in dictionary and dictionary[word] == 1:
      if is_previous_word_unk:
        return_input += ('<unk> ')
      else:
        return_input += (' <unk> ')
        is_previous_word_unk = True
    else:
      is_previous_word_unk = False
      return_input += (word + ' ')
  return return_input

def replace_words_not_in_training(input_file, dictionary):
  return_input = ""
  sentence = input_file.split()
  is_previous_word_unk = False
  for word in sentence:
    if word in dictionary:
      is_previous_word_unk = False
      return_input += (word + ' ')
    else:
      if is_previous_word_unk:
        return_input += ('<unk> ')
      else:
        return_input += (' <unk> ')
        is_previous_word_unk = True
  return return_input

def unigram_log_perplexity(sentence, unigram):
  unigram = dict(unigram)
  input = (sentence.lower() + "</s>")
  input = replace_one_word_occurrance(input, unigram)
  input = replace_words_not_in_training(input, unigram)
  input = input.split()
  probability = {}
  log_probability = {}
  total_log_prob = 0
  total_num_of_tokens = sum(unigram.values())
  m = len(input)

  for word in input:
    if word in unigram:
      probability[word] = unigram[word] 
  for word in probability:
    total_log_prob += math.log(probability[word], 2)

  avg_log_probability = total_log_prob/m
  perplexity = 2 ** (-avg_log_probability)
  return [perplexity,total_log_prob]

def bigram_log_perplexity(sentence, bigram, unique_words, is_smoothing):
  bigram = dict(bigram)
  input = (sentence.lower() + "</s>")
  input = replace_one_word_occurrance(input, bigram)
  input = replace_words_not_in_training(input, unique_words)
  input = input.split()
  probability = {}
  total_log_prob = 0
  is_prob_zero = False
  perplexity = 0
  m = len(input)
  for i in range(len(input)-1):
    two_token = input[i] + " " + input[i+1]
    given_word = input[i]
    if two_token in bigram:
      if given_word in unique_words:
        if is_smoothing:
          probability[two_token] = (bigram[two_token]+1)/(unique_words[given_word] + len(unique_words))
        else:
          probability[two_token] = (bigram[two_token]) / (unique_words[given_word])
        total_log_prob += math.log(probability[two_token], 2)
    else:
      if is_smoothing:
        probability[two_token] = 1/(unique_words[given_word] + len(unique_words))
        total_log_prob += math.log(probability[two_token], 2)
        # is_prob_zero = True
      else:
        probability[two_token] = 0
        is_prob_zero = True

  tokens_with_zero_prob = []
  if is_prob_zero:
    total_log_prob = 'N/A'
    perplexity = 'N/A'
    for two_token in probability:
      if probability[two_token] == 0:
        tokens_with_zero_prob.append(two_token)

  else:
    avg_log_probability = total_log_prob/m
    perplexity = 2 ** (-avg_log_probability)

  return [total_log_prob, tokens_with_zero_prob, perplexity]

def perplexity_unigram(input_file, unigram):
  unigram = dict(unigram)
  probability = {}
  total_log_prob = 0
  sentence = input_file.split()
  m = 0
  for word in sentence:
    if word != '<s>':
      if word in unigram:
        probability[word] = math.log(unigram[word], 2)
      if word not in unigram:
        probability['<unk>'] = math.log(unigram['<unk>'], 2)
  for word in sentence:
    if word != '<s>':
      if word in unigram:
        total_log_prob += probability[word]
        m += 1
      if word not in unigram:
        total_log_prob += probability['<unk>']
        m += 1

  average_log_prob = total_log_prob/m
  perplexity = 2 ** (-average_log_prob)
  return perplexity

def perplexity_bigram(input_file, bigram, unique_words, is_smoothing):
  probability = {}
  total_log_prob = 0
  is_zero_prob = False
  perplexity = 0
  input = input_file.split()
  m = 0
  for i in range(len(input)-1):
    two_token = input[i] + input[i+1]
    if two_token in bigram:
      if ((not is_smoothing) and (bigram[input[i]][input[i+1]] == 0)):
        is_zero_prob = True
      elif is_smoothing:
        prob = (bigram[two_token]+1)/ (unique_words[input[i]] + len(unique_words))
        total_log_prob += math.log(prob, 2)
      else:
        total_log_prob += math.log(bigram[input[i]][input[i+1]], 2)
    else:
      if is_smoothing:
        prob = 1/(unique_words['<unk>'] + len(unique_words))
        total_log_prob += math.log(prob, 2)
      else:
        is_zero_prob = True
    m += len(input[i])

  if is_zero_prob:
    perplexity = 'N/A'
  else:
    average_log_prob = total_log_prob/m
    perplexity = 2 **(-average_log_prob)
  return perplexity