## References:

## Import modules here

## Declare global variables here

## Delcare functions here

## Name: load_file
## Inputs: file_path, path to a csv or json file
## Outputs: pandas df of file
## Dependencies:
## Description:
def load_file(file_path):
    # if file is a csv
        # store in pandas df
    # else if file is a json file
        # store in pandas df
    # clean file
        # I think I just might manually remove exraneous cols from convidence docs first? not sure yet
    # return df
    pass

## Name: cohens_kappa
## Inputs: two pandas dfs, one for human annotations and one for llm annotations
## Outputs: double value, cohen's kappa score
## Dependencies:
## Description: calculates cohen's kappa for datasets
        ## plan to calculate on whole dataset and metric-by-metric basis
        ## for the latter, just convert cols from each dataset for a given metric to pandas df and pass into this function
def whole_cohens_kappa(df1, df2):
    pass

## Name: measure_accuracy
## Inputs: two pandas dfs, one for human annotations and one for llm annotations
## Outputs: double value, accuracy score
## Dependencies:
## Description: calculates number of correct annotations, computes proportion to total annotations
        ## planning to do on metric-by-metric and whole dataset scales
def measure_accuracy(df1, df2):
    pass

## Name:
## Inputs:
## Outputs:
## Dependencies:
## Description:

## Name:
## Inputs:
## Outputs:
## Dependencies:
## Description:

## Name:
## Inputs:
## Outputs:
## Dependencies:
## Description:

## Main function