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







"""
# predict tags
        if self.use_tags:

            # dim = [batch x tgt_len x embed_dim]
            y = self.to_embed(x)

            # dim = [tag_vocab x embed_dim] = [511 x 128]     
            embs = self.tag_embeddings

            # dim = [1 x tag_vocab x embed_dim] = [1 x 511 x 128]
            #embs = embs.unsqueeze(0)

            # precompute keys
            #self.tag_dec_att.compute_proj_keys(keys=embs)

            # compute context vector using attention mechanism

            # zero out all words + padding except current word
            # dim = [1 x tgt_len x embed_dim]
            #x_mask = current_word_mask(x.size(1)) & trg_mask

            #print(embs.size(), x.size(), x_mask.size(), trg_mask.size())

            # not sure we actually need a mask, if x is just the predicted hidden state for each word
            # x = x.masked_fill(x_mask, float('-inf'))
            
            # context: dim = [batch x tgt_len x embed_dim]
            # att_probs: dim = [batch x tgt_len x tag_vocab]
            #context, att_probs = self.tag_dec_att(query=x, values=embs, mask=x_mask)

            # dim = [batch x tgt_len x tag_vocab]
            att_probs = F.softmax(y @ embs.transpose(0,1), dim=2)
            #print(att_probs.size(), embs.unsqueeze(0).shape)
            #print(att_probs[0][0])

            # elementwise multiplication, maybe some squeeze and unsqueeze
            # context = att_probs.unsqueeze(2) @ embs.unsqueeze(0)
            # context = att_probs @ embs
            
            # print(embs[0], att_probs[0][0][0])

            # print(att_probs.shape, embs.shape)

            # dim = [1 x 1 x tag_vocab x embed_dim]
            embs = embs.unsqueeze(0).unsqueeze(0)  #expand(att_probs.size(0), embs.size(0), embs.size(1))

            # dim = [batch x trg_len x tag_vocab x 1]
            att_probs = att_probs.unsqueeze(3)

            # print(att_probs.shape, embs.shape)

            # elementwise hadamard product - attention scaling
            # dim = [batch x tgt_len x tag_vocab x embed_dim]
            context_weights = att_probs * embs # torch.mul(att_probs, embs)

            # print(context_weights.shape)

            # print(context_weights[0][0][0])

            # weighted sum of scaled embeddings
            # dim = [batch x tgt_len x embed_dim]
            context = torch.sum(context_weights, dim=2)

            # print(context.shape)
            # print(context[0][0])

            # dim = [batch x tgt_len x hidden_size]
            out = self.to_out(context)

            # dim = [batch x tgt_len x hidden_size]
            x = x + out
"""