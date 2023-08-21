
import pandas as pd
import glob


def load_goods(mode='train', path='.'):
    if mode == 'train':
        train_goods = pd.concat([
            pd.read_csv(f'{path}/训练集/traindata_goodsid/part-00000', header=None, names=['goods_id', 'cat_id', 'brandsn']),
            pd.read_csv(f'{path}/训练集/traindata_goodsid/part-00001', header=None, names=['goods_id', 'cat_id', 'brandsn']),
            pd.read_csv(f'{path}/训练集/traindata_goodsid/part-00002', header=None, names=['goods_id', 'cat_id', 'brandsn'])
        ], axis=0)
        return train_goods
    else:
        testa_goods = pd.concat([
            pd.read_csv(f'{path}/测试集a/predict_goods_id/part-00000', header=None, names=['goods_id', 'cat_id', 'brandsn']),
            pd.read_csv(f'{path}/测试集a/predict_goods_id/part-00001', header=None, names=['goods_id', 'cat_id', 'brandsn']),
        ], axis=0)
        return testa_goods


def load_user(mode='train', path='.'):
    if mode == 'train':
        train_user = pd.concat([
        pd.read_csv(x, header=None, names=['user_id', 'goods_id', 'is_clk', 'is_like', 'is_addcart', 'is_order', 'expose_start_time', 'dt'], nrows=500000)
            for x in glob.glob(f'{path}/训练集/traindata_user/part*')
        ], axis=0)
        return train_user
    else:
        testa_user = pd.read_excel(f'{path}/测试集a/a榜需要预测的uid_5000.xlsx')
        return testa_user





def load_dataset(path:str, mode=''):
    if mode == '':
        return (
            load_user('train', path), 
            load_user('test', path), 
            load_goods('train', path), 
            load_goods("test", path)
        )
    else:
        return (load_user(mode, path), load_goods(mode, path))



