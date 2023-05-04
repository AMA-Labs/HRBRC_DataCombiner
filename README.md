# Template Python Project
> *Briefly describe the purpose and functionality of your project, script, or tool*  

This is a boilerplate TEMPLATE for Python projects. It's a starting point that (hopefully) helps cut down on the repetitive project setup tasks and helps keep AMA-Labs project file structures consistent.

Included are...
 - A boilerplate `main.py` script with logging, cli arguments, and a few other things to help you get started
 - `.env` and `.config` files to help keep secrets secret and simplify configuring your script to run by other users
 - An `environment.yml` file for configuring and setting up environments for your tool
 - Initial test framework and Travis CI integration already setup and ready to rock and roll
 - VSCode `.vscode/` dir with configs for your project to utilize `unittest` and speed up 

### Usage
> *This should be a quick/small instruction set for how to run the script, with more a detailed instructions below*
1. Create a project from this template and alter as you need.
2. Install dependancies (see _Setup the environment_ below)
2. Run the project via its' entry-point, `main.py`, passing in any required arguments
```bash
python main.py <args>
```

## Details
- **Project Owner:** *name*
- **Project's Confluence Page:** [https://ama.atlassian.net/wiki/space/space-id](https://ama.atlassian.net/wiki/space/space-id)

## Contributors
* [@author](Author)

---
## Getting Started
> *Describe how to quickly get started running your project.*

Clone this repository to your local machine, create a VENV and install the project's requirements, then run `main.py`.

### 1. Setup the environment
- Create the conda VENV for the project and install the required packages
```bash
conda env create -f environment.yml -n <new-environment-name>
```
- Activate the new VENV
```bash
conda activate <new-environment-name>
```

### 2. Configure the project
- Rename `.config.TEMPLATE` to `.config`. Edit values to work with your local machine.
- Rename `.env.TEMPLATE` to `.env` and update it with any required secrets

### 3. Run
5. Activate the VENV in your terminal and test the project
```bash
conda activate project_name
python main.py test_argument
```

## Development Environment
> *List any requirements or additional setup as needed to develop/contribute to this project.*

### Configuring the Environment
> *List any development-specific environment settings or steps here.

### Running Tests
```bash
# from project tld..
python -m unittest tests
```

### Contributing
> *Detail how to contribute to this project*

---

## ⚠️ IMPORTANT CONSIDERATIONS ⚠️
> *Add more notes here if needed, or feel free remove from the README*
- Store secrets, credentials, or confidential information in `.env`.
  - Use them in the script with `os.environ`.  (e.g. `os.environ['GITHUB_TOKEN']`)
- Store any configuration variables (information that changes from machine to machine) in `.config`
  - Reference them in the script with `cfg`. (e.g. `cfg.LABLIB_PATH`)

**Please try your best to adhere to the following standards:**
- Use `snake_case` for variable names
- Use `camelCase` for function names
  - The first word (lowercase) should be a verb that describes the action it takes. (e.g. `parseData()`)
- Define constants near the top of the file, below imports/setup, with `UPPER_CASE_LIKE_THIS`
