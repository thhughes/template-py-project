# template-py-project
This is a setup project. Not intended for direct use. It's intended to be a bootstrapper so that development can just start happening and you can expect the same results/behaviors. 

# Setup
* Clone repo 
* Run `env-setup` while passing in the project name you plan to work on e.g. `env-setup cat-simulator`. 
* Run `deploy-env` while passing in the directory your working repo is in: e.g. `deploy-env cat-sim-repo`. This will copy over all the required content for execution/use. 

# Usage
Somewhat of a basic build tooling, intended to just bootstrap things. Can extend as necessary. Built in tooling: 
- lint 
    - Linting is not a REQUIRED thing in software development, but it's a thing every developer should be familiar with and use. For every 1 line of code you write, you'll read 10. Having coding standards makes that easier to digest. 
    - This project uses the default `pylint` library and standards. Feel free to update those requirements in `root/config/.pylintrc`
- testing
    - Without tests, how do you know your code works? What if it changes? test runs `pytest` against the `src/tests` subdirectory. Just because it doesn't error doesn't mean you don't have bugs. 
- clean 
    - I don't like caches sitting around, command cleans them up. 
- run
    - Runs `src/main.py` which is considered to be the actual script in the repo. You can have multiple 'main' scripts in the repo, but the setup doesn't really support that - you'd need to extend. 
    - `src/main.py` is passed in a config file `root/config/main.ini`. You're welcome to update this to a JSON or something more modern, I was just going for default support without caring to pass in all the contents over commandline and handle that via build script. 
- All
    - Runs things in the order of: Lint -> Test -> Run. 
    - Skips clean to unclutter stdout. 