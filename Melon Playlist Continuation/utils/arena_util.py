# -*- coding: utf-8 -*-
import io
import os
import json
from collections import Counter
from pathlib import Path

import numpy as np

class Config:
    data_prefix = Path('./data')
    arena_data_prefix = Path('./arena_data')

def write_json(data, fname: str):
    def _conv(o):
        if isinstance(o, (np.int64, np.int32)):
            return int(o)
        raise TypeError

    file = Config.arena_data_prefix.joinpath(fname)
    file.parent.mkdir(exist_ok=True, parents=True)
    with io.open(str(file), "w", encoding="utf-8") as f:
        json_str = json.dumps(data, ensure_ascii=False, default=_conv)
        f.write(json_str)


def load_json(fname):
    with open(fname, encoding="utf-8") as f:
        json_obj = json.load(f)

    return json_obj


def debug_json(r):
    print(json.dumps(r, ensure_ascii=False, indent=4))


def remove_seen(seen, l):
    seen = set(seen)
    return [x for x in l if not (x in seen)]


def most_popular(playlists, col, topk_count):
    c = Counter()

    for doc in playlists:
        c.update(doc[col])

    topk = c.most_common(topk_count)
    return c, [k for k, v in topk]
