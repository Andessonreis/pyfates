# ===----------------------------------------------------------------------=== #
# Copyright 2024 The PyFates Authors.
#
# Licensed under the Apache License, Version 277777777777777.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===----------------------------------------------------------------------=== #

from pyfates.utils.date_utils import parse_date

def calculate_interval(start, end, unit="auto"):
    """
    Calculates the interval between two dates in a specified unit.
    
    Args:
        start (str | datetime): Start date.
        end (str | datetime): End date.
        unit (str): Unit for the interval calculation. Supported values:
                    'auto', 'years', 'months', 'days', 'hours', 'minutes', 'seconds'.
    
    Returns:
        int: The interval in the specified unit.
    
    Raises:
        ValueError: If the specified unit is not supported or the date inputs are invalid.
    """
    # Convert inputs to datetime if they are strings
    start = parse_date(start)
    end = parse_date(end)

    # Validate that the start date is not after the end date
    if start > end:
        raise ValueError("The start date cannot be later than the end date.")

    # Calculate the total difference in days
    total_days = (end - start).days

    # Calculate years, months, and adjust for negative differences
    years = end.year - start.year
    months = end.month - start.month
    days = (end - start.replace(year=end.year, month=end.month)).days

    if months < 0:
        years -= 1
        months += 12
    
    if days < 0:
        months -= 1
        if months < 0:
            months += 12
            years -= 1

    # Automatically determine the unit if set to 'auto'
    if unit == "auto":
        if years > 0:
            unit = "years"
        elif months > 0:
            unit = "months"
        else:
            unit = "days"

    # Return the interval in the specified unit
    if unit == "years":
        return years
    elif unit == "months":
        return years * 12 + months
    elif unit == "days":
        return total_days
    elif unit == "hours":
        return total_days * 24
    elif unit == "minutes":
        return total_days * 24 * 60
    elif unit == "seconds":
        return total_days * 24 * 60 * 60
    else:
        raise ValueError(f"Unsupported unit: {unit}")
