# README

This repository contains the materials and the code for the
statistical analyses for the paper.

## 2-AFC data

`data/geometry-data.json` contains the data for the two
alternative forced choice task. It is an array of JSON objects. Here
is an example object

```json
{
    "participant_number": "50010",
    "accuracy": 0,
    "group_number": 40,
    "block": 1,
    "rt": 4759.490000084043,
    "trial_type": "control",
    "key": "geometry"
  }
```

* `participant_number` uniquely identifies the participants.
* `accuracy` tells you whether the response matches the "right answer"
  as determined by the geometric principle. It is always 0 for control
  trials, otherwise 1 if the participant is correct.
* `group_number` is an identifier that describes which geometric
  concept is being tested. Read the next section to understand how to
  interpret it
* Recall from the paper that participants completed the task twice.
  `block` tells you which iteration that is.
* `rt` contains the reaction time in milliseconds
* `trial_type`: can be either `control` or `experimental`.
* `key`: can be either `training` or `geometry`. You will want to
  filter out the training trials.
  
To interpret the `group_number`, we will need the information in
`geometry_stimuli/stiminfo.json` or `data/geometry-group-info.json`.
They are also arrays of objects. Let's look at one of those objects.

```json
{
    "group_number": 6,
    "filenames": [
      "6_1.png",
      "6_2.png",
      "6_3.png",
      "6_4.png",
      "6_5.png",
      "6_6.png"
    ],
    "correct_image": "6_5.png",
    "group_index": 5,
    "ppt_type": "Topology",
    "ppt_label": "Connexity",
    "paper_category": "Topology",
    "paper_label": "Connectedness",
    "paper_number": 5,
    "correct_number": 5,
    "correct_index": 4
  }
```

* `group_number`: This is an identifier, the same group number as the
  one in `data/geometry-data.json`.
* `filenames`: A list of image filenames for the group of images.
* `correct_image`: The filename for the correct image.
* `group_index`: group_number - 1, not necessary.
* `ppt_type`, `ppt_label`: These are information bits from the
  powerpoint sent to us by Dehaene et al., 2006. Not necessary.
* `paper_category`: The GT concept group for this group of images, as
  labelled in Dehaene et al., 2006.
* `paper_label`: The specific GT concept being testing by these
  images, as labelled in Dehaene et al., 2006.
* `paper_number`: The chronological number of the image as it appears
  in Dehaene et al., 2006.
* `correct_number`, `correct_index`: The correct answer, in number (1
  indexed) and index (0 indexed) form.

## UCMRT / Matrix reasoning data

`data/mrt-data.json` is an array of objects. Let's look at one object.

```json
{
    "participant_number": "50010",
    "accuracy": 0,
    "problemSet": "A",
    "rt": 11534.10999989137
}
```

The problem set refers to the various problems sets used by Pahor et
al., 2006. `rt` is reaction time in milliseconds.

## Mental rotation data

`data/mental_rotation-data.json` is an array of objects. Let's take a look at one.

```json
{
    "participant_number": "50010",
    "target_img": "6_target.png",
    "stimulus_type": "experimental",
    "number_correct": 1,
    "duration": 15539.900000207126
}
```

* `stimulus_type` can be either `training` or `experimental`.
* `number_correct` ranges between 0 and 2. We coded 2 as accurate, and
  anything else as inaccurate.

## ACT / SAT data

`data/act-sat-cleaned.csv` is a CSV file. Let's look at the first row.

```csv
,participant_number,MathPercentile,EnglishPercentile
0,50002,0.69,0.87
```

We converted ACT and SAT scores to percentiles. So participant `50002`
scored `0.69` percentile on math and `0.87` on reading.


## Other files

`raw-izard-2009.txt` contains data sent by Prof. Izard and contains
the data on adults from the Izard & Spelke (2009) study. They use a
`Diapo` number to identify trials. `diapo-to-paper-number.txt` is a
two column CSV that translates between `Diapo`s and `paper_number`,
which the rest of the data uses.

## Analyses

The `geometry-analysis.Rmd` file contains R markdown used for the
multiple comparisons between the GT concept categories.

The `python-analyses-and-figures.ipynb` file is a Jupyter Notebook
that contains code for all other graphs and analyses in the paper.

## Questions

Please feel free to contact the first author, Vijay Marupudi, if you
have any further questions. He doesn't bite!

## References

* Dehaene, S., Izard, V., Pica, P., & Spelke, E. (2006). Core
  Knowledge of Geometry in an Amazonian Indigene Group. 311, 4.
* Izard, V., & Spelke, E. (2009). Development of Sensitivity to
  Geometry in Visual Forms. Human Evolution, 23(3), 213–248.
* Pahor, A., Stavropoulos, T., Jaeggi, S. M., & Seitz, A. R. (2019).
  Validation of a matrix reasoning task for mobile devices. Behavior
  Research Methods, 51(5), 2256–2267.

