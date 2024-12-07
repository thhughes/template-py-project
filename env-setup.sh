#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: setup.sh env-name"
    exit 1
fi

script_dir=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")

private_dir="${script_dir}/Private"

if [ ! -d "$private_dir" ]; then
    mkdir "$private_dir"
    echo "[INFO]: Creating [$private_dir]"
fi

venv_name="$1"
venv_path="${private_dir}/${venv_name}"

if [ ! -d "$venv_path" ]; then
    echo "[WARNING] Virtual environment [${venv_name}] does not exist."
    echo "[INFO] Creating Virtual Environment."
    python3 -m venv ${venv_path}
fi
echo "[INFO] Activating Virtual Environment" 
source "${venv_path}/bin/activate"
if [ $? -ne 0 ]; then 
    echo "[ERROR] Failed to activate Virtual Environment"
    exit 1 
fi 
echo "source ${venv_path}/bin/activate" >> ${private_dir}/source-env.sh
pip3 install -r "${script_dir}/requirements.txt"
deactivate 
ln -s "${venv_path}/bin/python" "${private_dir}/python"


echo "[INFO] Setup Complete"
echo "To start Environment, run 'source private/source-env.sh" > "${script_dir}/env.txt"
echo "Optional direct shebang usage is [#!${private_dir}/python]" >> "${script_dir}/env.txt"