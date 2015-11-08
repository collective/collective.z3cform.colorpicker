#!/bin/bash
set -e

args=("$@")

case $1 in
    run)

        cd src/collective.z3cform.colorpicker
        if [ ! -d ./src/collective.z3cform.colorpicker.egg-info ]; then
             python setup.py egg_info
        fi

        /srv/webapp/bin/debuginstance fg
        ;;
    *)
esac

exec "$@"
