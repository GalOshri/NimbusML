# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand

import json

loss_table_json = json.loads('''
{
  "ClassificationLossFunction": {
    "exp": "classificationlossfunction_exploss",
    "hinge": "classificationlossfunction_hingeloss",
    "log": "classificationlossfunction_logloss",
    "smoothed_hinge": "classificationlossfunction_smoothedhingeloss"
  },
  "RegressionLossFunction": {
    "poisson": "regressionlossfunction_poissonloss",
    "squared": "regressionlossfunction_squaredloss",
    "tweedie": "regressionlossfunction_tweedieloss"
  },
  "SDCAClassificationLossFunction": {
    "hinge": "sdcaclassificationlossfunction_hingeloss",
    "log": "sdcaclassificationlossfunction_logloss",
    "smoothed_hinge": "sdcaclassificationlossfunction_smoothedhingeloss"
  },
  "SDCARegressionLossFunction": {
    "squared": "sdcaregressionlossfunction_squaredloss"
  }
}
''')