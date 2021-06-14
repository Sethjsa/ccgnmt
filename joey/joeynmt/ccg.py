# # coding: utf-8

# """
# Various decoders
# """
# from typing import Optional

# import torch
# import torch.nn as nn
# from torch import Tensor
# from joeynmt.attention import BahdanauAttention, LuongAttention
# from joeynmt.encoders import Encoder
# from joeynmt.helpers import freeze_params, ConfigurationError, subsequent_mask
# from joeynmt.transformer_layers import PositionalEncoding, \
#     TransformerDecoderLayer, MultiHeadedAttention


# # pylint: disable=abstract-method
# class CCG_Layer(nn.Module):
#     """
#     Base decoder class
#     """

#     @property
#     def output_size(self):
#         """
#         Return the output size (size of the target vocabulary)

#         :return:
#         """
#         return self._output_size



# # pylint: disable=arguments-differ,too-many-arguments
# # pylint: disable=too-many-instance-attributes, unused-argument
# class CCGDecoder(Decoder):
#     """
#     A transformer decoder with N masked layers.
#     Decoder layers are masked so that an attention head cannot see the future.
#     """

#     def __init__(self,
#                  num_layers: int = 4,
#                  num_heads: int = 8,
#                  hidden_size: int = 512,
#                  ff_size: int = 2048,
#                  dropout: float = 0.1,
#                  emb_dropout: float = 0.1,
#                  vocab_size: int = 1,
#                  freeze: bool = False,
#                  tag_embeddings = None,
#                  **kwargs):
#         """
#         Initialize a Transformer decoder.

#         :param num_layers: number of Transformer layers
#         :param num_heads: number of heads for each layer
#         :param hidden_size: hidden size
#         :param ff_size: position-wise feed-forward size
#         :param dropout: dropout probability (1-keep)
#         :param emb_dropout: dropout probability for embeddings
#         :param vocab_size: size of the output vocabulary
#         :param freeze: set to True keep all decoder parameters fixed
#         :param kwargs:
#         """
#         super().__init__()

#         self._hidden_size = hidden_size
#         self._output_size = vocab_size

#         self.tag_embeddings = tag_embeddings # size s_dim, embed_dim
#         self.to_embed = nn.Linear(hidden_size, embed_dim)
#         self.to_out = nn.Linear(embed_dim, hidden_size)
#         self.tag_dec_att = LuongAttention(hidden_size=hidden_size, key_size=encoder.output_size)

#         if freeze:
#             freeze_params(self)

#     def forward(self,
#                 trg_embed: Tensor = None,
#                 # mods
#                 # tag_embed: Tensor = None,
#                 encoder_output: Tensor = None,
#                 encoder_hidden: Tensor = None,
#                 src_mask: Tensor = None,
#                 unroll_steps: int = None,
#                 hidden: Tensor = None,
#                 trg_mask: Tensor = None,
#                 **kwargs):
#         """
#         Transformer decoder forward pass.

#         :param trg_embed: embedded targets
#         :param encoder_output: source representations
#         :param encoder_hidden: unused
#         :param src_mask:
#         :param unroll_steps: unused
#         :param hidden: unused
#         :param trg_mask: to mask out target paddings
#                          Note that a subsequent mask is applied here.
#         :param kwargs:
#         :return:
#         """

#         x = dec_input

#         x = self.to_embed(dec_input)

#         x = self.src_trg_att(x=x, tag_embeddings)

#         # compute context vector using attention mechanism
#         context, att_probs = self.attention(query=x, values=tag_embeddings, mask=src_mask)

#         x = self.to_out(context)

#         out = dec_input + x

#         return out, att_probs, None, None

#     def __repr__(self):
#         return "%s(num_layers=%r, num_heads=%r)" % (
#             self.__class__.__name__, len(self.layers),
#             self.layers[0].trg_trg_att.num_heads)
