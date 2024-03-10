# RAG-WIKI
Empowering knowledge exploration and generation through LLamaIndex and RAG on the full WIKI knowledge base.


https://github.com/lyyf2002/RAG-WIKI/assets/57008530/acbac812-6924-4d6d-9e4f-309871dfd211

# Startup 🚀

1. Clone this repo `git clone https://github.com/lyyf2002/RAG-WIKI`

2. Download [a subset of WIKI](https://drive.google.com/file/d/1L0MXCj6oWwkM6t454WBlDGAaJ8TF10ir/view?usp=sharing) processed by me which only has 200MB text.

3. Ensure those files satisfy the following file hierarchy: (`storage` is the path that stores the index)

   ```
   ROOT
   ├── wiki
   ├── storage
   └── RAG-WIKI
   ```

4. To process the full WIKI or other data, please follow the 5-7.

5. Download the full WIKI data you like from  [Wikipedia database backup dump](https://dumps.wikimedia.org/), e.g. https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2 for English.

6. use [wikiextractor](https://github.com/attardi/wikiextractor) to get the cleaned text for the wiki dataset.

   ```
   wikiextractor -o wiki --json --no-templates enwiki-latest-pages-articles.xml.bz2
   ```

7. `storage` will be created by the `app.py` when you first run it. You can change the path to get different index stored before.

8. cd `RAG-WIKI`

9. Update the `api_base` and `api_key` in `app.py`. You can get a free key for test at https://github.com/chatanywhere/GPT_API_free

10. install the Dependencies:

    ```
    pip install streamlit
    pip install llama-index
    pip install langchain
    ```

11.  run `streamlit run app.py` 
