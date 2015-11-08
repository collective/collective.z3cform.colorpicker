FROM abstracttechnology/plone:5.0
MAINTAINER Giorgio Borelli <giorgio@giorgioborelli.it>

USER root

COPY docker-buildout.cfg buildout.cfg
COPY . src/collective.z3cform.colorpicker

RUN chown -R webapp:webapp src buildout.cfg

USER webapp
RUN python bin/buildout -v
