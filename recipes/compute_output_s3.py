# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
out = dataiku.Dataset("out")
out_df = out.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

output_s3_df = out_df # For this sample code, simply copy input to output


# Write recipe outputs
output_s3 = dataiku.Dataset("output_s3")
output_s3.write_with_schema(output_s3_df)
