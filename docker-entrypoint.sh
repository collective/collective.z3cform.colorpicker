#!/bin/bash
set -e

args=("$@")

case $1 in
    run)

        if [ ! -d /src/webapp/src/collective.z3cform.colorpicker.egg-info ]; then
            cd src/collective.z3cform.colorpicker && python setup.py egg_info
        fi

        /srv/webapp/bin/debuginstance fg
        ;;
    *)
esac

exec "$@"
