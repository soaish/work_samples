import json
import os
import sys

initial = json.load(sys.stdin)

final = []


def ensure_files_exist(filenames):
    assert all([os.path.isfile(f) for f in filenames])


def rename(dict_, key, newkey):
    value = dict_[key]
    del dict_[key]
    dict_[newkey] = value


for idx, item in enumerate(initial):
    group_number = idx + 1
    group_index = idx
    filenames = [str(group_number) + "_" + str(i + 1) + ".png" for i in range(6)]
    ensure_files_exist(filenames)
    correct_image = filenames[item["correct"] - 1]
    rename(item, "correct", "correct_number")
    item["correct_index"] = item["correct_number"] - 1
    item_dict = dict(
        group_number=group_number,
        filenames=filenames,
        correct_image=correct_image,
        group_index=group_index,
    )
    item_dict.update(item)
    final.append(item_dict)

print(json.dumps(final))
