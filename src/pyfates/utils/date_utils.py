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

from datetime import datetime

def parse_date(input, format="%Y-%m-%d"):
    """
    Converts a string or value into a datetime object using the provided format.
    
    Args:
        input (str | datetime): A string or datetime object.
        format (str): Expected format for date strings. Default: "%Y-%m-%d".
    
    Returns:
        datetime: Corresponding datetime object.
    
    Raises:
        ValueError: If the input is invalid or does not match the expected format.
    """
    if isinstance(input, datetime):
        return input
    try:
        return datetime.strptime(input, format)
    except ValueError:
        raise ValueError(f"Invalid date format. Expected: {format}. Received: {input}")

def format_date(date, style="default"):
    """
    Formats a datetime object into a string using a specific style.
    
    Args:
        date (datetime): The datetime object to format.
        style (str): Formatting style. Examples: 'default', 'iso', 'us', 'br'.
    
    Returns:
        str: The formatted date as a string.
    
    Raises:
        ValueError: If the style is not supported or the input is not a datetime object.
    """
    if not isinstance(date, datetime):
        raise ValueError("The provided value is not a datetime object.")
    
    styles = {
        "default": "%Y-%m-%d",
        "iso": "%Y-%m-%dT%H:%M:%S",
        "us": "%m/%d/%Y",
        "br": "%d/%m/%Y",
    }
    
    if style not in styles:
        raise ValueError(f"Unsupported formatting style: {style}")
    
    return date.strftime(styles[style])
