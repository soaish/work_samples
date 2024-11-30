import json
import sys
from dataclasses import dataclass, asdict
import copy
from typing import List, Optional
import random
import uuid

DIRECTION_TO_INDEX = dict(left=0, right=1)


@dataclass
class Trial:
    main_stim: dict
    display_stims: List[dict]
    trial_type: str
    unique_trial_id: str
    base_trial_id: str
    correct_answer: Optional[str]
    flipped: bool

    def flip(self) -> "Trial":
        trial = copy.deepcopy(self)
        trial.unique_trial_id = str(uuid.uuid4())
        if trial.trial_type == "experimental":
            assert trial.correct_answer is not None
            old_correct_index = DIRECTION_TO_INDEX[trial.correct_answer]
            flippable_index = 1 if old_correct_index == 0 else 0
            ## swap this two
            trial.main_stim, trial.display_stims[flippable_index] = (
                trial.display_stims[flippable_index],
                trial.main_stim,
            )
            old_correct_stim = trial.display_stims[old_correct_index]
            random.shuffle(trial.display_stims)
            correct_changed = old_correct_stim == trial.display_stims[old_correct_index]
            if correct_changed:
                trial.correct_answer = (
                    "left" if trial.correct_answer == "right" else "right"
                )
        else:
            randindex = random.choice([0, 1])
            trial.main_stim, trial.display_stims[randindex] = (
                trial.display_stims[randindex],
                trial.main_stim,
            )

        trial.flipped = True
        return trial


def gen_trials(list_of_groups):

    trials: List[Trial] = []

    for group in list_of_groups:
        filenames = group["filenames"]
        fset = set(filenames)

        assert len(filenames) == 6

        # make the experimental trial
        fset.remove(group["correct_image"])
        normal_images = random.sample(tuple(fset), 2)
        random.shuffle(normal_images)
        for img in normal_images:
            fset.remove(img)
        main_stim = normal_images[0]
        display_stims = [group["correct_image"], normal_images[1]]
        random.shuffle(display_stims)

        experimental_trial = Trial(
            main_stim=main_stim,
            display_stims=display_stims,
            trial_type="experimental",
            correct_answer="left"
            if group["correct_image"] == display_stims[0]
            else "right",
            unique_trial_id=str(uuid.uuid4()),
            base_trial_id=str(uuid.uuid4()),
            flipped=False,
        )

        remaining = list(fset)
        random.shuffle(remaining)
        main_stim = remaining[0]
        display_stims = remaining[1:]

        control_trial = Trial(
            main_stim=main_stim,
            display_stims=display_stims,
            trial_type="control",
            correct_answer=None,
            unique_trial_id=str(uuid.uuid4()),
            base_trial_id=str(uuid.uuid4()),
            flipped=False,
        )

        trials.append(experimental_trial)
        trials.append(control_trial)

    random.shuffle(trials)
    return trials


def main():

    stiminfo = json.load(sys.stdin)

    non_training_groups = filter(lambda x: x["paper_category"] != "Training", stiminfo)
    training_groups = filter(lambda x: x["paper_category"] == "Training", stiminfo)

    experimental_trials = gen_trials(non_training_groups)
    training_trials = gen_trials(training_groups)

    jsonize = lambda x: [asdict(y) for y in x]

    output = dict(
        training=jsonize(training_trials),
        experimental=[
            jsonize(experimental_trials),
            [asdict(trial.flip()) for trial in experimental_trials],
        ],
    )

    print(json.dumps(output))

    print(
        "{} training trials, {} experimental trials, x2 when flipped.".format(
            len(training_trials), len(experimental_trials)
        ),
        file=sys.stderr,
    )


main()
