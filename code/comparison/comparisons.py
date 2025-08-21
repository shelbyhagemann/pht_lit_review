## References:

## Import modules here
import pandas as pd
import json
from sklearn.metrics import cohen_kappa_score

## Declare global variables here

# list of all papers being compared
papers = ["alankus11", "alaseem19", "asakawa21", "baloian02", "bandukdta20", "brule16", "butler19",
          "carrington18", "cavasosquero18", "chibaudel20", "dragomir18", "fan12", "fell03", "franz21",
          "galbraith14", "gerling13", "gizatdinova22", "gleason20", "hoey10", "hossain22", "hossain23",
          "india19", "jack00", "jiang23", "keate94", "kim13", "koushik17", "kuwahara06", "lobo21", "lu22",
          "madeo11", "mahmud06", "mai22", "miao17", "montague", "myers02", "nair22", "obryen12", "oretega15",
          "payne23", "piper10", "raman98", "ravers23", "rello15", "rubin16", "sanchez10", "sharma18", "strangl15",
          "sturm17", "torrente12", "uchida18", "valencia19", "wilson17", "ye12", "zhang23"]

## Delcare functions here

## Name: load_file
## Inputs: file_path, path to a json file
## Outputs: pandas df of file
## Dependencies:
## Description:
def load_file(file_path, status):
    # load file
    with open(file_path, "r") as f:
        data = json.load(f)
    # convert to pandas df
    if status == 0:
        df = pd.DataFrame([data["Framework"]])
    elif status == 1:
        df = pd.json_normalize(data["StudyCharacteristics"], sep="_")
    # return df
    return df

## Name: whole_cohens_kappa
## Inputs: two pandas dfs, one for human annotations and one for llm annotations
## Outputs: double value, cohen's kappa score for entire dataset
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

## Name: metric_cohens_kappa
## Inputs: two pandas dfs, one for human annotations and one for llm annotations, column for specific metric
## Outputs: 2 col pandas df containing cohens kappa value and metric
## Dependencies:
## Description:
def metric_cohens_kappa(df1, df2, column):
    # make container for results
    results_df = pd.DataFrame(columns = ["metric", "cohens_kappa"])
    # calculate cohens kappa
    kappa = cohen_kappa_score(df1[column], df2[column])
    # add values to df
    results_df.loc[len(results_df)] = [column, kappa]
    # return results
    return results_df

## Name: generate_results
## Inputs: paper (name of paper), results_list (list of results)
## Outputs:
## Dependencies:
## Description:
def generate_results(paper, results_list):
    results_list.to_dict(orient="records")
    with open(f"{paper}_cohens_kappa.json", "w") as f:
        json.dump(results_list.to_dict(orient="records"), f, indent=4)


## Main function
def main():
    for paper in papers:
        results_list = pd.DataFrame(columns = ["metric", "cohens_kappa"])
        # review framework annotations first
        status = 0
        human_annotations_fr = load_file(f"comparison_human/{paper}_framework.json", status)
        gpt_annotations_fr = load_file(f"comparison_gpt/{paper}_framework.json", status)
        #entire_cohens_kappa = whole_cohens_kappa(human_annotations, gpt_annotations)
        for col in human_annotations_fr:
            cohens_kappa_results = metric_cohens_kappa(human_annotations_fr, gpt_annotations_fr, col)
            kappa_value = cohens_kappa_results["cohens_kappa"].iloc[0]
            results_list.loc[len(results_list)] = [col, kappa_value]
        # review study characteristic annotations
        status = 1
        human_annotations_sc = load_file(f"comparison_human/{paper}_characteristics.json", status)
        gpt_annotations_sc = load_file(f"comparison_gpt/{paper}_characteristics.json", status)
        #entire_cohens_kappa = whole_cohens_kappa(human_annotations, gpt_annotations)
        for col in human_annotations_sc:
            cohens_kappa_results = metric_cohens_kappa(human_annotations_sc, gpt_annotations_sc, col)
            kappa_value = cohens_kappa_results["cohens_kappa"].iloc[0]
            results_list.loc[len(results_list)] = [col, kappa_value]
        generate_results(paper, results_list)

if __name__ == '__main__':
    main()