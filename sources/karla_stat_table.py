#!/usr/bin/env python3
# Copyright 2020 Google Sans Authors

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fontTools.otlLib.builder import buildStatTable
from fontTools.ttLib import TTFont

UPRIGHT_AXES = [
    dict(
        tag="wght",
        name="Weight",
        ordering=0,
        values=[
            dict(nominalValue=200, rangeMinValue=150, rangeMaxValue=250, name="ExtraLight"),
            dict(nominalValue=300, rangeMinValue=250, rangeMaxValue=350, name="Light"),
            dict(nominalValue=400, rangeMinValue=350, rangeMaxValue=450, name="Regular", flags=0x2, linkedValue=700),
            dict(nominalValue=500, rangeMinValue=450, rangeMaxValue=650, name="Medium"),
            dict(nominalValue=700, rangeMinValue=650, rangeMaxValue=750, name="Bold"),
            dict(nominalValue=800, rangeMinValue=750, rangeMaxValue=850, name="ExtraBold"),
            # dict(value=400, name="Regular", flags=0x2, linkedValue=700),  # Regular
            # dict(value=400, name="Regular", flags=0x2, linkedValue=700),  # Regular
            # dict(value=500, name="Medium"),  # Medium
            # dict(value=600, name="SemiBold"),  # SemiBold
            # dict(value=700, name="Bold"),  # Bold
        ],
    ),
    dict(
        tag="ital",
        name="Italic",
        ordering=1,
        values=[dict(value=0, name="Roman", flags=0x2, linkedValue=1)],  # Regular
    ),
]

ITALIC_AXES = [
    dict(
        tag="wght",
        name="Weight",
        ordering=0,
        values=[
            dict(nominalValue=200, rangeMinValue=150, rangeMaxValue=250, name="ExtraLight"),
            dict(nominalValue=300, rangeMinValue=250, rangeMaxValue=350, name="Light"),
            dict(nominalValue=400, rangeMinValue=350, rangeMaxValue=450, name="Regular", flags=0x2, linkedValue=700),
            dict(nominalValue=500, rangeMinValue=450, rangeMaxValue=650, name="Medium"),
            dict(nominalValue=700, rangeMinValue=650, rangeMaxValue=750, name="Bold"),
            dict(nominalValue=800, rangeMinValue=750, rangeMaxValue=850, name="ExtraBold"),
            # dict(value=400, name="Regular", flags=0x2, linkedValue=700),  # Regular
            # dict(value=500, name="Medium"),  # Medium
            # dict(value=600, name="SemiBold"),  # SemiBold
            # dict(value=700, name="Bold"),  # Bold
        ],
    ),
    dict(
        tag="ital",
        name="Italic",
        ordering=1,
        values=[dict(value=1, name="Italic")],  # Italic
    ),
]

VARIABLE_DIR = "../fonts/ttf"
KAR_UPRIGHT = f"{VARIABLE_DIR}/Karla[wght].ttf"
KAR_ITALIC = f"{VARIABLE_DIR}/Karla-Italic[wght].ttf"


def main():
    # process upright files
    filepath = KAR_UPRIGHT
    tt = TTFont(filepath)
    buildStatTable(tt, UPRIGHT_AXES)
    tt.save(filepath)
    print(f"[STAT TABLE] Added STAT table to {filepath}")

    # process italics files
    filepath = KAR_ITALIC
    tt = TTFont(filepath)
    buildStatTable(tt, ITALIC_AXES)
    tt.save(filepath)
    print(f"[STAT TABLE] Added STAT table to {filepath}")


if __name__ == "__main__":
    main()
