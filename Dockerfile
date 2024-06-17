# Description: Dockerfile for basic demo of r4m dashboard
# Author: Thanasis Argyriou, argythana[at]gmail.com
# Docker version: 24.0.7, build 24.0.7-0ubuntu2~22.04.1

# Use a light python image
FROM python:3.11.9-slim

# Set working directory to /src
WORKDIR /src

ADD README.md /src/README.md

# Add python files for basic streanlit app.
ADD src/public_dashboard.py /src/public_dashboard.py
ADD src/streamlit_auth.py /src/streamlit_auth.py
ADD src/utils/__init__.py /src/utils/__init__.py
ADD src/utils/all_plots_from_df.py /src/utils/all_plots_from_df.py
ADD src/utils/dashboard_plot_configs.py /src/utils/dashboard_plot_configs.py
ADD src/utils/demo_site_colors.py /src/utils/demo_site_colors.py

# Add only main requirements file. Not the dev dependencies
ADD requirements/requirements.txt /src/requirements/requirements.txt

# Add only static data file
ADD src/data/acts_by_date_trend.feather /src/data/acts_by_date_trend.feather

# Add streamlit configuration files
ADD src/.streamlit/config.toml /src/.streamlit/config.toml
ADD src/.streamlit/secrets.toml /src/.streamlit/secrets.toml

# Install python packages
RUN pip install --upgrade pip wheel setuptools
RUN pip install --no-cache-dir -r requirements/requirements.txt

# Expose port 8555
EXPOSE 8555

# Run public_dashboard.py when container launches
ENTRYPOINT ["streamlit", "run", "public_dashboard.py", "--server.port=8555"]
