# HW- 1: Maheen Naqvi
# CSCI 381 - Prof. Alla
#Models:
def unigram(input_dictionary):
  unigram_dictionary = {}
  input_dictionary = dict(input_dictionary)
  input_dictionary.pop('<s>')
  total_number_of_tokens = sum(input_dictionary.values())
  for word in input_dictionary:
    unigram_dictionary[word] = (input_dictionary[word] / total_number_of_tokens)
  return unigram_dictionary

def bigram(input_dictionary, input_file, is_smoothing):
  bigram_tokens = make_bigram_tokens_dictionary(input_file)
  input_dictionary = dict(input_dictionary)
  bigram_dictionary = {}
  sentence = input_file.split()
  for i in range(len(sentence)-1):
    two_tokens = sentence[i] + ' ' + sentence[i+1]
    if is_smoothing:
      bigram_dictionary[two_tokens] = (bigram_tokens[two_tokens] + 1)/(input_dictionary[sentence[i]]+ len(input_dictionary))
    else:
      bigram_dictionary[two_tokens] = (bigram_tokens[two_tokens])/(input_dictionary[sentence[i]])
  return bigram_dictionary

def make_bigram_tokens_dictionary(input_file):
  bigram_tokens = {}
  sentence = input_file.split()
  for i in range(len(sentence)-1):
    two_tokens = sentence[i] + ' ' + sentence[i+1]
    if two_tokens in bigram_tokens:
      bigram_tokens[two_tokens] += 1
    else:
      bigram_tokens[two_tokens] = 1
  return bigram_tokens

def find_percentage_tokens(test_input, train_input):
  num_of_tokens_not_occurred = 0
  num_of_types_not_occurred = 0

  for word in test_input:
    if word not in train_input:
      num_of_tokens_not_occurred += test_input[word]
      num_of_types_not_occurred += 1

  percentage_tokens_not_occurred = (num_of_tokens_not_occurred/(sum(test_input.values()))) 
  percentage_types_not_occurred = (num_of_types_not_occurred/len(test_input))
  return [percentage_tokens_not_occurred, percentage_types_not_occurred]
