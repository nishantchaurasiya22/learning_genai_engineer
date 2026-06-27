# LangChain Components – Quick Notes

LangChain is a framework to build GenAI apps easily using LLMs.

## 1. Models
- Common interface to use any LLM (OpenAI, Gemini, Claude, etc.)
- No need to write different code for each provider
- Just change model name, rest of code stays same

## 2. Prompts
- Reusable templates with variables
- Example: "Translate {text} to {language}"

## 3. Chains
- Connects multiple steps together
- Output of one step → Input of next step
- Example: User input → Prompt → LLM → Output

## 4. Memory
- LLM has no memory by default (stateless)
- Memory stores past chat history
- Helps bot remember previous conversation

## 5. Tools & Agents
- **Tools** = external functions LLM can use
  - Example: weather API, calculator, web search
- **Agents** = LLM decides which tool to use and when
- Agent = "smart decision maker" + tools

## 6. Document Processing
- Used to load and prepare data (PDF, text, website, etc.)
- Steps:
  1. Load document
  2. Split into small chunks
  3. Send for embedding

## 7. Vector Stores
- Database to store embeddings (number form of text)
- Used for fast similarity search
- Example: Pinecone, Chroma, FAISS

## 8. Retriever
- Fetches most relevant chunks from vector store
- Based on user's question
- Sends relevant data to LLM for accurate answer

## Simple Flow (RAG Example)
```
Document → Split → Embed → Vector Store
User Question → Retriever → Relevant Chunks → LLM → Final Answer
```

## Why LangChain is useful
- One common code for all LLMs
- Easy memory handling
- Easy tool/agent integration
- Easy RAG (chat with your own data) setup
- Saves development time