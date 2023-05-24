FROM registry.fedoraproject.org/fedora:latest

# Install dependencies for building ITSx
RUN dnf install -y wget dnf-plugins-core bzip2 perl perl-CPAN make gcc git which
RUN dnf install -y https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
RUN dnf install -y nvidia-driver

# Clone the ITSx repository
RUN git clone --branch 1.1.3-fixed --depth 1 https://github.com/ncbi/ITSx.git /opt/ITSx

# Install HMMER
RUN wget http://eddylab.org/software/hmmer/hmmer.tar.gz &&\
    tar zxf hmmer.tar.gz &&\
    cd hmmer-3.3.2 &&\
    ./configure &&\
    make &&\
    make install

# Set the working directory
WORKDIR /app

# Set the PATH environment variable to include /ITSx and HMMER installation directory
ENV PATH="/opt/ITSx:/opt/ont-guppy/bin:${PATH}"

# Copy the Python script to the container
COPY entry_script.py /app/entry_script.py

# Download Guppy tarball
RUN curl -fsSL https://cdn.oxfordnanoportal.com/software/analysis/ont-guppy_6.5.7_linux64.tar.gz -o guppy.tar.gz

# Extract Guppy tarball
RUN tar -xzvf guppy.tar.gz -C /opt

# Cleanup: remove the tarball and extracted files
RUN rm guppy.tar.gz

# Set the entry point to execute the Python script with provided arguments
ENTRYPOINT ["python3", "/app/entry_script.py"]