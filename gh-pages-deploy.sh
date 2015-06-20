#!/bin/bash
mkdir build; cp index.html build/; cd build
git init
git config user.name "Travis-CI"
git config user.email "travis@email.com"
git add .
git commit -m "Deployed to Github Pages"
git push --force --quiet "https://${GH_TOKEN}@github.com/bhanuvrat/popular-web-frameworks" master:gh-pages > /dev/null 2>&1
