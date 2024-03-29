# <p align="center">Investigating Information Complexity and Compression in Personal and Public Recollections</p>
$${\color{Salmon}Final\space Project\space for\space Computational\space Content\space Analysis\space (Winter\space 2024)}$$
<p align="center">Erika P. Zhang</p>

This project explores the perceived challenges faced by a student in recounting and recording the nature, behavior, history, and identity of both the individual and groups of people. The nuance of daily decisions and actions often get obscured when information is compressed into concise formats for communication. In this realm of collective human records, I investigate these ideas by comparing the types of information people share when reflecting on events in private, versus when sharing them with others. These explorations rely upon embeddings, discovered themes, and LLMs.

## Primary RQ: <br>
- RQ1: How do Holocaust survivors articulate their lived experiences in personal interviews compared to scholarly interviews?
- RQ2: To what extent has the story of a famous individual been preserved in collective memory in ways that diverge from that individual's recollection, if at all?


## Data: <br>
Part One
- [Holocaust survivor eyewitness testimonies](https://www.testifyingtothetruth.co.uk/viewer/)
- [Academic paper abstracts](https://github.com/allenai/s2orc)

Part Two
- Francis Willards' personal journals
- Digital archive pages collected from first two pages of google search results

All data files: [Here](https://drive.google.com/drive/folders/10RSqaGkyg5z5LLoW8gD6HJfaNwtmvJ2D?usp=sharing) 

## How To Navigate This Repo:
1. Data Collection
   * [s2orc_apidata.ipynb](https://github.com/erikaz1/text_memory_and_identity/blob/main/data_collection/s2orc_apidata.ipynb): First, we start with data collection tasks. This file retrieves paper abstracts from S2ORC using their API.
   * [webscraping_eyewitness.ipynb](https://github.com/erikaz1/text_memory_and_identity/blob/main/data_collection/webscraping_eyewitness.ipynb): Next, construct a scraper for gathering eyewitness testimonies from [this site](https://www.testifyingtothetruth.co.uk/viewer/).
   * [eyewitness_testimonies_subcollection](https://github.com/erikaz1/text_memory_and_identity/blob/main/data_collection/embed_eyewitness.ipynb): Raw eyewitness data.
   * [s2orc_abstracts_subcollection](https://github.com/erikaz1/text_memory_and_identity/blob/main/data_collection/embed_eyewitness.ipynb): Raw abstracts data.
   * [frames.ipynb](https://github.com/erikaz1/text_memory_and_identity/blob/main/data_collection/frames.ipynb): Generate frames.
   * [embed_eyewitness.ipynb](https://github.com/erikaz1/text_memory_and_identity/blob/main/data_collection/embed_eyewitness.ipynb): Generate embeddings with v3 Small.
   * [eyewitness_abstracts_frame_list](eyewitness_abstracts_frame_list): Completed data, ready for analysis.
2. Exploration
   * [explore_embeddings2.ipynb](https://github.com/erikaz1/text_memory_and_identity/blob/main/exploration/explore_embeddings2.ipynb): Generate visualizations of embeddings.
   * [explore_frames.ipynb](https://github.com/erikaz1/text_memory_and_identity/blob/main/exploration/explore_frames.ipynb): Investigate frames, generate frame definitions and projections.
   * [antonym_projections.ipynb](https://github.com/erikaz1/text_memory_and_identity/blob/main/exploration/antonym_projections.ipynb): Generate antonym word-pairs and visualize.
4. FW - Part Two
   * [embed_fw.ipynb](https://github.com/erikaz1/text_memory_and_identity/blob/main/fw_part_two/embed_fw.ipynb): Generate embeddings with v3 Small.
   * [dn_text_all_clean_0310.csv](dn_text_all_clean_0310.csv): Completed fw data, ready for analysis.
   * [fw_llm_exploded_doclvl.csv](fw_llm_exploded_doclvl.csv): Expanded df for embedding.
   * [fw_embeddings_0214-1.ipynb](https://github.com/erikaz1/text_memory_and_identity/blob/main/fw_part_two/fw_embeddings_0214-1.ipynb): Visualizations using TF-IDF sparse embeddings.
