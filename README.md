Here's the information about the files that this repo contains.

As per the assignment the "first task" was to generate the chunks using the transcript provided.
for this the access the file named "Chunk_generation.ipynb" . Directly run the ipynb file on either jupyter notebook or colab. 
Add the path to the folder variable where the transcipts are present and path where you want to save the chunks to variable chunk_folder.
the folder named chunks have the sample files of the output of Chunk_generation.ipynb

for the "second task" the file "metrics for the evaluation of chunks" contains the strategies that could be suitable for chunks evaluation and 
file named evaluation_metrics.py contains the code to implement those strategies.

for the "third" and the final task access the file named LLM_agents.ipynb provide your own groq api key and path to the folder where chunks are saved.
Embedding_model -> huggingface hkunlp/instructor-xl
llm used -> llama-3.1-70b-versatile
vectorstore -> Faiss 
