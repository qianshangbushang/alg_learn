

from typing import Optional, List, Union, Dict

import numpy as np
import paddle
from tqdm import tqdm

from paddlenlp.transformers import ErnieTokenizer
from paddlenlp.utils.log import logger

from data_loader import parse_label, DataCollator, convert_example_to_feature
from extract_chinese_and_punct import ChineseAndPunctuationExtractor


class DuIEDataset(paddle.io.Dataset):
    def __init__(self, data, label_map, tokenizer, max_length=512, pad_to_max_length=False):
        super(DuIEDataset, self).__init__()

        self.data = data
        self.chn_punc_extractor = ChineseAndPunctuationExtractor()
        self.tokenizer = tokenizer
        self.max_seq_length = max_length
        self.pad_to_max_length = pad_to_max_length
        self.label_map = label_map

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):

        example = json.loads(self.data[item])
        input_feature = convert_example_to_feature(
            example, self.tokenizer, self.chn_punc_extractor,
            self.label_map, self.max_seq_length, self.pad_to_max_length)
        return {
            "input_ids": np.array(input_feature.input_ids, dtype="int64"),
            "seq_lens": np.array(input_feature.seq_len, dtype="int64"),
            "tok_to_orig_start_index":
            np.array(input_feature.tok_to_orig_start_index, dtype="int64"),
            "tok_to_orig_end_index": 
            np.array(input_feature.tok_to_orig_end_index, dtype="int64"),
            # If model inputs is generated in `collate_fn`, delete the data type casting.
            "labels": np.array(input_feature.labels, dtype="float32"),
        }


    @classmethod
    def from_file(cls,
                  file_path,
                  tokenizer,
                  max_length=512,
                  pad_to_max_length=None):
        assert os.path.exists(file_path) and os.path.isfile(
            file_path), f"{file_path} dose not exists or is not a file."
        label_map_path = os.path.join(
            os.path.dirname(file_path), "predicate2id.json")
        assert os.path.exists(label_map_path) and os.path.isfile(
            label_map_path
        ), f"{label_map_path} dose not exists or is not a file."
        with open(label_map_path, 'r', encoding='utf8') as fp:
            label_map = json.load(fp)

        with open(file_path, "r", encoding="utf-8") as fp:
            data = fp.readlines()
            return cls(data, label_map, tokenizer, max_length, pad_to_max_length)

