# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
avocado_transactions_partitioned = dataiku.Dataset("avocado_transactions_partitioned")
avocado_transactions_partitioned_df = avocado_transactions_partitioned.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

output_df = avocado_transactions_partitioned_df # For this sample code, simply copy input to output


# Write recipe outputs
output = dataiku.Dataset("output")
output.write_with_schema(output_df)
