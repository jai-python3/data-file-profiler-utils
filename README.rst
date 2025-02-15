========================
Data File Profiler Utils
========================

A Python module for simple data file profiling.


Usage
-----

Installation
------------

.. code-block:: shell

    pip install data-file-profiler-utils


Integration
-----------

.. code-block:: python

    from import data_file_profiler_utils import Manager as ProfileManager

    pm = ProfileManager()
    pm.profile_file("/tmp/patient002.vcf")


Exported Console Script
-----------------------

Contents of sample data file:

.. code-block:: shell

    cat -n sample.tsv                      
    1  #CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO
    2  1       12345   rs567   A       G       50      PASS    DP=30;AF=0.2;AN=1000;CSQ=missense_variant|HIGH|GeneA|ENSG00000112345|transcriptA|ENST00000234567|protein_coding|1/10|c.123C>T|p.Arg41Trp|123/1000|ensembl
    3  2       56789   rs890   T       C       44      PASS    DP=25;AF=0.1;AN=1200;CSQ=synonymous_variant|MEDIUM|GeneB|ENSG00000123456|transcriptB|ENST00000345678|protein_coding|5/20|c.567A>G|p.Ala189Ala|567/1200|ensembl
    4  3       98765   rs123   G       T       60      PASS    DP=40;AF=0.3;AN=800;CSQ=splice_acceptor_variant|HIGH|GeneC|ENSG00000134567|transcriptC|ENST00000456789|protein_coding|2/15|c.987+1G>T|p.?|987/800|ensembl
    5  1       34567   rs456   C       A       55      PASS    DP=35;AF=0.15;AN=900;CSQ=frameshift_variant|HIGH|GeneX|ENSG00000145678|transcriptX|ENST00000567890|protein_coding|8/25|c.345_346insT|p.Leu116Phefs*12|345/900|ensembl


Invocation of the exported console script:

.. code-block:: shell
  
    profile-data-file --infile /tmp/demo-data-file-profiler-utils/sample.tsv --verbose --outdir /tmp/demo-data-file-profiler-utils/
    --logfile was not specified and therefore was set to '/tmp/demo-data-file-profiler-utils/profile_data_file.log'
    Wrote profile metadata file '/tmp/demo-data-file-profiler-utils/sample.tsv.profile.txt'
    The log file is '/tmp/demo-data-file-profiler-utils/profile_data_file.log'
    Execution of '/tmp/data-file-profiler-utils/venv/lib/python3.10/site-packages/data_file_profiler_utils/profile_data_file.py' completed


Contents of the profile report:

.. code-block:: shell

    cat -n /tmp/demo-data-file-profiler-utils/sample.tsv.profile.txt
    1  ## method-profiled: /tmp/data-file-profiler-utils/venv/lib/python3.10/site-packages/data_file_profiler_utils/manager.py
    2  ## date-profiled: 2025-02-15-142732
    3  ## profiled-by: sundaram
    4  file: /tmp/demo-data-file-profiler-utils/sample.tsv
    5  md5sum: 786b82b2414d3acf7af34c068e358759
    6  date_created: 2025-02-15 14:06:37.202165
    7  file_size: 776
    8  line_count: 5
