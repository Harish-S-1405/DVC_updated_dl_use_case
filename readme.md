# DVC DL _ AIOPS_ DEMO

## commands - 

### create new environment

```bash
conda create -n dvc_dl python=3.7 -y
source activate base
conda activate dvc_dl
```
### initialilizing git and dvc

```bash
git init
dvc init
```

### created empty files

```bash

touch readme.md
touch .gitignore setup.py dvc.yaml params.yaml
mkdir -p  config src/utils
touch config/config.yaml
touch config/secrets.yaml
touch src/__init__.py src/utils/__init__.py
touch src/stage_01_load_save
touch src/utils/all_utils.py
pip freeze > requirements.txt
```