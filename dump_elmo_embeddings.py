import argparse

from bilm import dump_token_embeddings

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input-file')
parser.add_argument('--weights-file')
parser.add_argument('--options-file')
parser.add_argument('-o', '--output-file', default='elmo_token_embeddings.hdf5')

args = parser.parse_args()

vocab_file = 'elmo_vocab.txt'
with open(args.input_file, 'r') as fin:
    with open(vocab_file, 'w') as fout:
        for line in fin:
            token = line.strip()
            if token == '[UNK]':
                token = '<UNK>'
            elif token == '[START]':
                token = '<S>'
            elif token == '[STOP]':
                token = '</S>'
            elif token == '[PAD]':
                token = '<PAD>'

            fout.write(token)
            fout.write('\n')

dump_token_embeddings(
    vocab_file, args.options_file, args.weights_file, args.output_file
)
