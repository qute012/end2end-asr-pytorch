import json

with open('kspon_labels.txt', 'rt') as f:
    lines = f.read().strip().split('\n')
    
vocab = list()

for line in lines:
    char, idx = line.split(' ')
    if char=="<space>":
        char = " "
    vocab.append(char)
    
with open('kspon_labels.json', 'w', encoding='utf-8') as f:
    json.dump(vocab, f, indent=4)