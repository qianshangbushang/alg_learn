import paddle
import paddle.nn as nn
from paddle.io import Dataset

EMBEDDING_SIZE = 256


# 定义深度学习模型
class RecommenderNet(nn.Layer):
    def __init__(self, num_users, num_goods, embedding_size, numeric_size):
        super(RecommenderNet, self).__init__()
        self.num_users = num_users
        self.num_goods = num_goods
        self.embedding_size = embedding_size

        weight_attr_user = paddle.ParamAttr(
            regularizer=paddle.regularizer.L2Decay(1e-6),
            initializer=nn.initializer.KaimingNormal()
        )
        self.user_embedding = nn.Embedding(
            num_users,
            embedding_size,
            # weight_attr=weight_attr_user
        )

        weight_attr_movie = paddle.ParamAttr(
            regularizer=paddle.regularizer.L2Decay(1e-6),
            initializer=nn.initializer.KaimingNormal()
        )
        self.goods_embedding = nn.Embedding(
            num_goods,
            embedding_size,
            # weight_attr=weight_attr_movie
        )

        self.linear = nn.Linear(
            2 * embedding_size, 2
        )

    def forward(self, data):
        user, goods, feat = data[0], data[1], [data[idx] for idx in [2, 3, 4]]
        feat = paddle.stack(feat, 1).astype(paddle.float32)

        user_vector = self.user_embedding(user)
        goods_vector = self.goods_embedding(goods)
        x = paddle.concat([user_vector, goods_vector], 1)
        return self.linear(x)


class SelfDefinedDataset(Dataset):
    def __init__(self, df, mode='train'):
        super(SelfDefinedDataset, self).__init__()
        self.df = df
        self.mode = mode

    def __getitem__(self, idx):
        if self.mode == 'predict':
            return (
                self.df['user_id'].iloc[idx],
                self.df['goods_id'].iloc[idx],
                self.df['is_clk_max'].iloc[idx], self.df['is_like_max'].iloc[idx],
                self.df['is_addcart_max'].iloc[idx],
            )
        else:
            return (
                self.df['user_id'].iloc[idx],
                self.df['goods_id'].iloc[idx],
                self.df['is_clk_max'].iloc[idx],
                (self.df['is_like_max'].iloc[idx] != 0).astype(int),
                (self.df['is_addcart_max'].iloc[idx] != 0).astype(int),
                (self.df['is_order_max'].iloc[idx] != 0).astype(int)
            )

    def __len__(self):
        return len(self.df)
