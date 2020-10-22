## Building the Fonts

The fonts are built using fontmake and post-processed with gftools scripts. The tools are all Python based. 

First, is necessary to create a python3 virtual environment in the folder and then install the tools into it. This would only be needed once.

```
# Create a new virtualenv
python3 -m venv venv
# Activate env
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt
```


From the Sources folder run the build script in the terminal:

```
# Activate env
source venv/bin/activate
cd Sources
sh build.sh
```