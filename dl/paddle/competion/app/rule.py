
from data import load_dataset
import pandas as pd
import numpy as np


def popular_goods(train_user:pd.DataFrame, topn:int):
    pop_df = train_user.groupby('goods_id', as_index=False)[['is_clk', 'is_like', 'is_addcart', 'is_order']].sum()
    pop_weight = {
        "is_clk": 1.0,
        "is_like": 1.0,
        "is_addcart": 1.0,
        "is_order": 0.5,
    }
    pop_df["pop"] = 0
    for col, weight in pop_weight.items():
        pop_df['pop'] += pop_df[col] * weight

    print(pop_df)
    pop_df = pop_df.sort_values('pop',ascending=False)
    result = pop_df["goods_id"][:topn]
    return result


def high_order_user(train_user: pd.DataFrame):
    user_order = train_user.groupby('user_id')['is_order'].sum().reset_index(name='order_num')
    user_order = user_order[[user_order['order_num'] >= 1]]
    return user_order



def recommend_by_hot(train_user:pd.DataFrame, train_goods, testa_user, testa_goods):
    hot_weight = {
        "is_clk": 1.0,
        "is_like": 1.0,
        "is_addcart": 1.0,
        "is_order": 0.5,
    }

    df = train_user.copy()
    df = df[df['user_id'].isin(testa_user['user_id'])]
    df = df[df['goods_id'].isin(testa_goods['goods_id'])]

    print(f"before hot: {df['user_id'].nunique()}")

    df['hot'] = 0
    for col, weight in hot_weight.items():
        df['hot'] += df[col] * weight

    idx = df.groupby('user_id')['hot'].idxmax()
    result = df.iloc[idx]
    print(f"rule hot result: {result['user_id'].nunique()}/{len(testa_user)}")
    result = result[['user_id', 'goods_id']]
    result["rank"] = 1
    return result

def recommend_by_addcart(train_user, train_goods, testa_user, testa_goods):
    print("user in train dataset: ", np.mean(testa_user['user_id'].isin(train_user['user_id'])))
    print("item in train dataset: ", np.mean(testa_goods['goods_id'].isin(train_goods['goods_id'])))
    print("unique user: ", train_user['user_id'].nunique())
    print("unique item: ", train_user['goods_id'].nunique())
    print("user desc: \n", train_user.describe().round(2))
    print("user count: \n", train_user['user_id'].value_counts())


    train_data = pd.merge(train_user.iloc[:], train_goods.iloc[:], on='goods_id')
    print("unqiue cate: ", train_data['cat_id'].nunique())
    print("unique brand: ", train_data['brandsn'].nunique())


    train_agg_feat = train_data.loc[
        (train_data['is_order'] == 0) & (train_data['is_addcart'] != 0) 
    ]

    train_agg_feat = train_agg_feat[train_agg_feat['user_id'].isin(testa_user['user_id'])]
    train_agg_feat = train_agg_feat[train_agg_feat['goods_id'].isin(testa_goods['goods_id'])]
    result =  train_agg_feat[['user_id', 'goods_id']].copy()

    print("num of testa user: ", testa_user["user_id"].nunique())
    print("num of result: ", len(result))
    print("num of result user: ", result["user_id"].nunique())
    print("num of result item: ", result["goods_id"].nunique())
    result["rank"] = 2
    return result



def recommend(path:str):
    train_user, testa_user, train_goods, testa_goods = load_dataset(path)
    ret_addcart = recommend_by_addcart(train_user, train_goods, testa_user, testa_goods)
    rec_hot = recommend_by_hot(train_user, train_goods, testa_user, testa_goods)
    result = pd.concat([ret_addcart, rec_hot], axis=0).reset_index()
    idx = result.groupby(['user_id'])['rank'].idxmax()
    result = result.iloc[idx]
    result = result[result['user_id'].isin(high_order_user(train_user)['user_id'])]
    print(f"rule result: {result['user_id'].nunique()}/5000")
    return  result[['user_id', 'goods_id', 'rank']]


if __name__ == "__main__":
    df = recommend(".")