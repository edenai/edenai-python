
# Add simplified classes

if grep -Fxq "from edenai.simplify import *"  edenai/__init__.py
then
    echo "Simplified classes already imported"
else
    echo "from edenai.simplify import *" >> edenai/__init__.py
fi

bash git_push.sh edenai edenai-python " $1 "
