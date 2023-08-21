import paddle
import json
from paddlenlp.embeddings import TokenEmbedding
from util import ChineseAndPunctuaionExtractor

class DuIEDataset(paddle.io.Dataset):
    def __init__(self, data, label_map, tokenizer:TokenEmbedding, 
                 max_length=512, pad_to_max_length=False):
        super().__init__()

        self.data = data
        self.chn_punc_extractor = ChineseAndPunctuaionExtractor()
        self.tokenizer = tokenizer
        self.max_seq_length = max_length
        self.pad_to_max_length = pad_to_max_length
        self.label_map = label_map
        return
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, item):
        example = json.loads(self.data[item])
        input_feature = convert
