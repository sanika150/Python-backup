from tika import parser
raw = parser.from_file('dataset1.pdf')
text = raw['content']

# 2. Split Text
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_text(text)

# 3. & 4. Embed and Store
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

embeddings = HuggingFaceEmbeddings()
doc_search = Chroma.from_texts(chunks, embeddings)