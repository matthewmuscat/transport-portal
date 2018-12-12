FROM heavysaturn/transport-portal-base:latest

# Move the new files into the right folder
COPY . /portal
WORKDIR /portal

# Set up the virtual environment
RUN pipenv clean
RUN pipenv sync

# Open the port that nginx will communicate through
EXPOSE 10013

# Make tini the default command handler, and run the pipenv script called start.
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["pipenv", "run", "collectstatic"]
CMD ["pipenv", "run", "start"]
