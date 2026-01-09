import torch
import torch.nn as nn
from torch.nn import functional as F

with open("input.txt","r",encoding="utf-8") as f:
    text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)

stoi = {ch:i for i,ch in  enumerate(chars)}
iots = {i:ch for i,ch in enumerate(chars)}

encoder = lambda s: [stoi[c] for c in s]
decoder = lambda l: "".join([iots[i]for i in l ])

data = torch.tensor(encoder(text),dtype=torch.long)

n = int(len(data) * 0.9)

train_data = data[:n]
test_data = data[n:]

block_size = 8

x = train_data[:block_size]
y = train_data[1:block_size+1]

for t in range(block_size):
    context = x[:t+1]
    target = y[t]

torch.manual_seed(1337)

batch_size = 4
block_size = 8

def get_batch(split):
    data = train_data if split == "train" else test_data
    ix = torch.randint(len(data) - block_size , (batch_size,))
    x =torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    return x,y

xb, yb = get_batch('train')

torch.manual_seed(1337)

class BigramLanguageModel(nn.Module):

    def __init__(self,vocab_size):
        super().__init__()

        self.token_embeding_table = nn.Embedding(vocab_size,vocab_size)

    def forward(self,idx,targets = None):
        logits = self.token_embeding_table(idx)
        if targets is None:
            loss = None
        else:
            B,T,C = logits.shape
            logits = logits.view(B*T,C)
            targets = targets.view(B*T)

            loss = F.cross_entropy(logits,targets)

        return logits,loss

    def generate(self,idx,max_new_tokens):
        for _ in range(max_new_tokens):

            logits,loss = self(idx)
            logits = logits[:,-1,:]
            probs = F.softmax(logits,dim=-1)
            idx_next = torch.multinomial(probs,num_samples=1)
            idx = torch.cat((idx,idx_next),dim = 1)
        return idx

m = BigramLanguageModel(vocab_size)
out,loss = m(xb,yb)
print(out.shape)
print(loss)
print(decoder(m.generate(torch.zeros((1,1),dtype=torch.long), max_new_tokens=100)[0].tolist()))
