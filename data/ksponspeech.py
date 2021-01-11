import json
import argparse

parser = argparse.ArgumentParser(description='Preparing Ksponspeech for training and evaluating')
parser.add_argument('--path', default='/root/storage/dataset/kspon', type=str, help="dataset root directory")
args = parser.parse_args()

#===============Preparing Vocab===============
with open('data/kspon_labels.txt', 'rt') as f:
    lines = f.read().strip().split('\n')
    
vocab = list()

for line in lines:
    char, idx = line.split(' ')
    if char=="<space>":
        char = " "
    vocab.append(char)
    
with open('data/kspon_labels.json', 'w', encoding='utf-8') as f:
    json.dump(vocab, f, indent=4)
    
#===============Create manifest===============
