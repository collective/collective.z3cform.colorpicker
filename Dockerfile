FROM abstracttechnology/plone:4.3
MAINTAINER Giorgio Borelli

USER root

COPY docker-buildout.cfg buildout.cfg
COPY . src/collective.z3cform.colorpicker
RUN python bin/buildout -v
COPY docker-entrypoint.sh docker-entrypoint.sh

RUN chown -R webapp:webapp .

USER webapp

ENTRYPOINT ["/srv/webapp/docker-entrypoint.sh"]
CMD ["run"]
