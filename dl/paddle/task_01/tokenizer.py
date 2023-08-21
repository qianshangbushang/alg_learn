import jieba
import paddle
import numpy as np

from collections import defaultdict
from paddlenlp.data import JiebaTokenizer, Vocab, Pad, Stack, Tuple

class Tokenizer(object):
    def __init__(self) -> None:
        self.vocab = {}
        self.tokenizer=jieba,
        self.UNK_TOKEN='[UNK]'
        self.PAD_TOKEN='[PAD]'
        self.vocab_path = 'vocab.txt'
    

    def set_vocab(self, vocab):
        self.vocab = vocab
        self.tokenizer = JiebaTokenizer(vocab)
        return
    

    def build_vocab(self, sentences):
        word_count = defaultdict(lambda: 0)
        for line in sentences:
            words = jieba.cut(line)
            for word in words:
                word = word.strip()
                if len(word) == 0:
                    continue
                word_count[word] += 1
        word_id = 0
        for word, num in word_count.items():
            if num < 5:
                continue

            self.vocab[word] = word_id
            word_id += 1
        
        self.vocab[self.UNK_TOKEN] = word_id
        self.vocab[self.PAD_TOKEN] = word_id + 1
        self.vocab = Vocab.from_dict(self.vocab, unk_token=self.UNK_TOKEN, pad_token=self.PAD_TOKEN)
        self.dum_vocab(self.UNK_TOKEN, self.PAD_TOKEN)
        self.tokenizer = JiebaTokenizer(self.vocab)
        return self.vocab

    def dump_vocab(self, unk_token, pad_token):
        with open(self.vocab_path, 'w', encoding='utf8') as f:
            for word in self.vocab._token_to_idx:
                f.write(word + "\n")
        return

    def text_to_ids(self, text):
        input_ids = []
        unk_token_id = self.vocab[self.UNK_TOKEN]
        for token in self.tokenizer.cut(text):
            token_id = self.vocab.token_to_idx.get(token, unk_token_id)
            input_ids.append(token_id)
        return input_ids
    

    def convert_example(self, example, is_test=False):
        input_ids = self.text_to_ids(example['text'])

        if not is_test:
            label = np.array(example['label'], dtype='int64')
            return input_ids, label
        else:
            return input_ids
    

def create_dataloader(dataset, trans_fn=None, mode='train', batch_size=1, pad_token_id = 0):
    if trans_fn:
        dataset = dataset.map(trans_fn, lazy=True)
    
    shuffle = True if mode=='train' else False
    sampler = paddle.io.BatchSampler(
        dataset=dataset, batch_size=batch_size, shuffle=shuffle
    )
    batchify_fn=lambda samples, fn=Tuple(
        Pad(axis=0, pad_val=pad_token_id),
        Stack(dtype='int64'),
    ): [data for data in fn(samples)]

    dataloader = paddle.io.DataLoader(
        dataset,
        batch_sampler = sampler,
        return_list=True,
        collate_fn=batchify_fn,
    )
    return dataloader
    
    