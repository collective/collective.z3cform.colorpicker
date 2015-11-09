#!/bin/bash
EGG_DIR=src/collective.z3cform.colorpicker
STATIC_DIR=src/collective.z3cform.colorpicker/src/collective/z3cform/colorpicker/static

set -e

args=("$@")

case $1 in
    run)

        cd $EGG_DIR
        if [ ! -d ./src/collective.z3cform.colorpicker.egg-info ]; then
             python setup.py egg_info
        fi

        /srv/webapp/bin/debuginstance fg
        ;;
    makepattern)
        cd $STATIC_DIR
        npm install;
        ./node_modules/bower/bin/bower --config.interactive=false  install
        make

        ;;
    servepattern)
        cd $STATIC_DIR
        python -m SimpleHTTPServer 8080
        ;;
    *)
        exec "$@"
        ;;
esac


