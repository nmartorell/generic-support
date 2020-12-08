# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu


try:
    # Read recipe inputs
    avocado_transactions_partitioned2_prepared = dataiku.Dataset("avocado_transactions_partitioned2_prepared")
    avocado_transactions_partitioned2_prepared_df = avocado_transactions_partitioned2_prepared.get_dataframe()


    # Compute recipe outputs from inputs
    # TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
    # NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

    output2_df = avocado_transactions_partitioned2_prepared_df # For this sample code, simply copy input to output


    # Write recipe outputs
    output2 = dataiku.Dataset("output2")
    output2.write_with_schema(output2_df)
except:
    pass
