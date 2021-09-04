#!/bin/sh

set -e

# Initialize submodules
git submodule init
git submodule update --init

# Update shenango
# echo Updating shenango
# cd shenango
# git pull origin main
# cd ..

# Update mvfst
echo Updating mvfst
cd mvfst
git pull origin master
cd ..

# Cloudlab patches to Shenango
echo Applying patch to Shenango
cd shenango
git apply ../connectx-4.patch
git apply ../cloudlab_xl170.patch
# git apply ../xl170_cloudlab_sep3.patch
cd ..

echo Done.
