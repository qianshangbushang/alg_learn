
from paddlenlp.embeddings import TokenEmbedding

import paddle
import paddle.nn as nn
import paddlenlp


class BowModel(nn.Layer):
    def __init__(self, embedder:TokenEmbedding):
        super().__init__()
        self.embedder = embedder
        self.encoder = paddlenlp.seq2vec.BoWEncoder(self.embedder.embedding_dim)
        self.cos_sim_fn = nn.CosineSimilarity(axis=-1)
        return
    
    def forward(self, text):
        # batch_size, num_tokens, embedding_dim
        embed_text = self.embedder(text)

        # batch_size, embedding_dim
        sumed = self.encoder(embed_text)
        return sumed

    def get_cos_sim(self, text_a, text_b):
        emb_a = self.forward(text_a)
        emb_b = self.forward(text_b)
        return self.cos_sim_fn(emb_a, emb_b)



def run():
    # 初始化TokenEmbedding， 预训练embedding未下载时会自动下载并加载数据
    token_embedding = TokenEmbedding(embedding_name="w2v.baidu_encyclopedia.target.word-word.dim300")

    # 查看token_embedding详情
    print(token_embedding)

    return


if __name__ == "__main__":
    run()