import random
import numpy as np
import sys

## Sampling function for drawing according to the given probability distribution
#Higher diversity -> more randomness in the drawing.
def sample(probability_distribution, diversity=1.0):
    # helper function to sample an index from a probability distribution
    probability_distribution = np.asarray(probability_distribution).astype('float64')
    probability_distribution = np.log(probability_distribution) / diversity
    exp_preds = np.exp(probability_distribution)
    probability_distribution = exp_preds / np.sum(exp_preds)
    #Draws 1 element at random according to the new scaled probability-distribution.
    probabilities = np.random.multinomial(n=1, pvals = probability_distribution) 
    return np.argmax(probabilities)

#Method for printing some example text from trained RNN
def generate_text_segment(text, length, diversity, generating_model, input_sequence_length, num_characters, char_indices, indices_char):
    start_index = random.randint(0, len(text) - input_sequence_length - 1)

    # We need a seed to start the text generation. Since during training the ANN always experiences
    # sentences of size 30, we seed it with a sentence of length 30 to get it into a sensible state.
    generated = ''
    sentence = text[start_index: start_index + input_sequence_length]
    generated += sentence
    
    sys.stdout.write('----- Generating with seed: "' + sentence + '"')

    for i in range(length):
        x_pred = np.zeros((1, input_sequence_length, num_characters))
        for t, char in enumerate(sentence):
            x_pred[0, t, char_indices[char]] = 1.
        

        predictions_distribution = generating_model.predict(x_pred, verbose=0)[0]
        next_index = sample(predictions_distribution, diversity)
        next_char = indices_char[next_index]

        generated += next_char
        #Stepping one symbol forward in the sentence
        sentence = sentence[1:] + next_char

    return generated


