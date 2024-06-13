# Mapping Science Through Editorial Board Interlocking

## Overview

This repository contains the source code and data used in the scientific paper:

de-Marcos, L., Goyanes, M. & Domínguez-Díaz, A. Mapping science through editorial board interlocking: connections and distance between fields of knowledge and institutional affiliations. Scientometrics (2024). https://doi.org/10.1007/s11192-024-05027-x

To generate the editorial board interlocking network ans calculate SNA metrics, follow these steps:

1. Run "generar_matriz_red_social.py": It will process the data file 1EBMembers_v5.0_FinalAffiliation_Fixed_Unified.xlsx, generating different files required to create a network connecting editorial board members with journals.

2. Run "bipartite_revistas_6fields.ipynb": It will load the network, calculate different SNA metrics, and generate different graphs in GEFX files.

The data files that are included or are generated in step 1 are the following:

* 1EBMembers_v5.0_FinalAffiliation_Fixed_Unified.xlsx: List of unified editorial board (EB) members and journals they participate in. EB members in multiple journals are represented with multiple rows, each one for a journal.
* 1EBMembers_v5.0_FinalAffiliation_Fixed_Unified_NoDuplicates.xlsx: Same as above with duplicated rows removed.
* 1EBMembers_v5.0_Final.xlsx: Same as above with journals removed, containing only unique EB members.
* 2Journals_v5.0_crosslisted.xlsx: List of journals with JCR details. Journals in more than one JCR category are marked as crosslisted.
* 3FieldsNJournals: Number of journals for each JCR SCIE and SSCI category.
* 0nodes_v5.0.xlsx: Nodes of the EB members and journals network. Contains a list of EB members and journals IDs, one per row.
* 0edges_v5.0.csv: Edges of the EB members and journals network. Contain a matrix that crosses EB members with journals, containing a 1 if certain EB member participates in the EB of certain journal.

