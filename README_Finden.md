# Finden Version of nlm-ingestor 

## Setup
1. Clone the repo
```
git clone https://github.com/DulanOrganization/nlm-ingestor
```
2. Create conda environment
```
conda create -n nlm_ingestor python=3.10
```
3. Activate conda env
```
conda activate nlm_ingestor
```
4. Install the package
```
pip install .
```
5. Install 'libmagic' - libmagic is a C library that provides routines for identifying the type of data contained in a file.
```
conda install -c conda-forge python-magic
```
6. Command to run tika server
```
java -jar ./jars/tika-server-standard-nlm-modified-2.9.2_v2.jar
```
7. Start the backend server [ONLY FOR LOCAL DEV]
```
python -m nlm_ingestor.ingestion_daemon
```