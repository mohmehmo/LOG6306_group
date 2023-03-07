import pandas as pd

def main():
    keras_repos = pd.read_csv("data/keras/keras_repo_100.csv", low_memory=False)
    pytorch_repos = pd.read_csv("data/pyTorch/pytorch_repo_100.csv", low_memory=False)
    tensorflow_repos = pd.read_csv("data/tensorflow/tensorflow_repo_100.csv", low_memory=False)

    all_repos = pd.concat([keras_repos,pytorch_repos]).drop_duplicates().reset_index(drop=True)
    all_repos = pd.concat([all_repos,tensorflow_repos]).drop_duplicates().reset_index(drop=True)



if __name__ == '__main__':
    main()