import torch
import numpy as np

# def mask(tgt_len):
#     mask = torch.zeros((tgt_len,tgt_len))
#     for i in range(tgt_len):
#         for j in range(tgt_len):
#             if i < j or i > j:
#                 mask[i][j] = False
#             else:
#                 mask[i][j] = True
#     return mask

def current_word_mask(size: int):
    """
    Mask out previous and subsequent positions (to prevent attending to past and future positions)
    Transformer helper function.

    :param size: size of mask (2nd and 3rd dim)
    :return: Tensor with 0s and 1s of shape (1, size, size)
    """
    mask = np.triu(np.ones((size, size)), k=0).astype('uint8') & np.tril(np.ones((size, size)), k=0).astype('uint8')
    return torch.from_numpy(mask) == 1


#add to padding mask

print(current_word_mask(10).unsqueeze(1))

        # mods

"""
        # extra ED attention
        # self.src_trg_att = MultiHeadedAttention(num_heads, size, dropout=dropout)
        # self.x_layer_norm = nn.LayerNorm(size, eps=1e-6)     

        # add CCG prediction - relu plus linear? Another linear?
        # self.tag_pred = nn.Linear(trg_embed + encoder_context + tag_embed, tag_vocab_size, dropout=dropout)
        # activation = nn.ReLU
        # no softmax, do this in model.py to go from logits to probs for loss

        # add linear transformation from 640 > 512
        # self.to_embed = nn.Linear(640, hidden_size, dropout=dropout)
        """

"""
        # ED attention between pred dec output and encoder output
        # context = self.src_trg_att(x=x, encoder_output)

        # CCG pred layer
        # tag_output_dist = self.tag_pred(x + context + prev_tag_output)

        # use predictions to make context vector (507 * 507)
        # need access to full tag_embeddings
        # tag_output = torch.bmm(tag_output_dist, tag_embeddings)

        # x = concat(x, tag_output)

        # linear transformation of output
        # x = self.to_embed(x)
        """

        #query = hidden[0][-1].unsqueeze(1)

            #compute embedding matrix
            # embs = torch.zeros(self.tag_vocab_size, self.tag_embed_dim)
            # for i in range(self.tag_vocab_size):
            #     torch.cat((embs, tag_embed(torch.tensor([i]))), 0)

            # emb = embs.detach().clone()
            
            # #duplicate by batches
            # for i in range(batch_size-1):
            #     embs = torch.cat((embs, emb), 0)

                        # print(x.size(1), trg_mask1.size(1))

            # x = x[1][-1].unsqueeze(1)
            # print(x.size())
