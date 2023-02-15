# install instructions

## install docker
https://docs.docker.com/desktop/install/mac-install/

## clone repo
`git clone https://github.com/jpfon/csv-mr.git`

## build image
`docker build . -t csv-mr`

## merge files
- cd into parent directory of files to merge
- `docker run --rm -v $PWD:/app/ csv-mr python main.py`
- by default it will look for files in `./inputs`, merge on `protocol title` and output `output.csv`
- if those need to be changed, then:
    - `docker run --rm -v $PWD:/app/ csv-mr python main.py --merge-on [COLUMN_NAME] --inputs_folder [INPUTS_FOLDER] --output [OUTPUT.CSV]`