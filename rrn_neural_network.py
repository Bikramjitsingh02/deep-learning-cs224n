import sys

import numpy as np
import torch
import torch.nn as nn

class SimpleRNNLanguageModel(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size):
        super().__init__()

        self.hidden_size = int (hidden_size)

        self.embedding = nn.Embedding(vocab_size, embed_size)

        # x_t -> hidden state
        self.W_x = nn.Parameter(torch.empty(embed_size, hidden_size))

        # previous hidden state -> new hidden state
        self.W_h = nn.Parameter(torch.empty(hidden_size, hidden_size))

        self.hidden_bias = nn.Parameter(
            torch.zeros(hidden_size)
        )

        self.W_output = nn.Parameter(torch.empty(hidden_size, vocab_size))

        self.output_bias = nn.Parameter(
            torch.zeros(vocab_size)
        )

        nn.init.xavier_uniform_(self.W_x)
        nn.init.xavier_uniform_(self.W_h)
        nn.init.xavier_uniform_(self.W_output)

    def forward(self, token_ids):
        batch_size = token_ids.size(0)
        sequence_length = token_ids.size(1)

        # Initial memory h_0
        h = torch.zeros(batch_size,
                        self.hidden_size,
                        device=token_ids.device,)

        all_logits = []

        for t in range(sequence_length):

            current_tokens = token_ids[:, t]

            #Token IDS -> embeddings
            x_t = self.embedding(current_tokens)

            h = torch.tanh(
                x_t @ self.W_x
                + h @ self.W_h
                + self.hidden_bias
            )

            logits = (
                    h @ self.W_output
                    + self.output_bias
            )

            all_logits.append(logits)

        return torch.stack(all_logits, dim=1)



if __name__ == "__main__":

    with open("corpus.txt", "r") as f:
        lines = f.readlines()
        vocab = set([word for line in lines for word in line.split()])

        word_to_id = {word : i for i, word in enumerate(vocab)}

        for i in word_to_id.keys():
            print(f"{i} -> {word_to_id[i]}")




