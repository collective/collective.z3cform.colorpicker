FROM abstracttechnology/plone:5.0
MAINTAINER Giorgio Borelli <giorgio@giorgioborelli.it>

USER root

COPY docker-buildout.cfg buildout.cfg
COPY . src/collective.z3cform.colorpicker
RUN python bin/buildout -v
COPY docker-entrypoint.sh docker-entrypoint.sh

RUN chown -R webapp:webapp .

USER webapp

ENTRYPOINT ["/srv/webapp/docker-entrypoint.sh"]
CMD ["run"]
