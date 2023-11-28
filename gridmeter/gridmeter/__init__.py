#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

   Copyright 2020 GRIDmeter™ contributors

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

from gridmeter.__version__ import *

from gridmeter._clustering import Clustering
from gridmeter._clustering import Clustering_Settings

from gridmeter._individual_meter_matching import IMM
from gridmeter._individual_meter_matching import IMM_Settings

from gridmeter._stratified_sampling import (
    Stratified_Sampling,
    SS_Settings,
    stratified_sampling_settings, 
    distance_stratified_sampling_settings
)

from gridmeter._utils import (
    Data,
    Data_Settings,
    DummyMeter,
    DummyPopulation,
    DummyTreatmentPoolPopulation,
)
