import faiss
import numpy as np
import logging
from sentence_transformers import SentenceTransformer

# Load Lightweight Enterprise Semantic Encoder immediately holding matrices inside Local Memory strictly!
# 'all-MiniLM-L6-v2' maps Unstructured Policy Dictionaries explicitly onto 384-dimensional Deep Vector arrays safely cleanly.
try:
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
except Exception as e:
    logging.error(f"Failed to load HuggingFace models locally: {e}")
    embedder = None

class FAISSRagEngine:
    def __init__(self):
        self.dimension = 384
        # IndexFlatL2 strictly guarantees High-Speed Euclidean Distance similarities natively inside CPU parameters intelligently!
        if embedder:
            self.index = faiss.IndexFlatL2(self.dimension)
        self.document_chunks = []
        
    def ingest_document(self, text: str, chunk_size=300):
        """Dissects Unstructured OCR maps into strictly sized contextual payloads mapping exact deep tensors natively."""
        if not embedder or not text:
            return 0
            
        words = text.split()
        chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]  # type: ignore
        
        if not chunks:
            return 0
            
        assert embedder is not None
        # Encode chunks into Vector Arrays
        embeddings = embedder.encode(chunks)
        # Typecast parameters dynamically enforcing native Float32 matrix intersections accurately!
        faiss_array = np.array(embeddings).astype('float32')
        
        # Inject exact parameters generating actual Vector Database entries inherently!
        self.index.add(faiss_array)
        self.document_chunks.extend(chunks)
        
        return len(chunks)

    def query_policy(self, query: str, top_k=3):
        """Intercepts specific AICTE/National queries extracting explicit Dense Overlaps automatically flawlessly!"""
        if not embedder or self.index.ntotal == 0:
            return ["Dense Vector Indices not initialized. Ingest RAG documents first."]
            
        assert embedder is not None
        query_vector = embedder.encode([query])
        faiss_query = np.array(query_vector).astype('float32')
        
        # Pull Top-K semantic matches directly isolating exact Euclidean matrix differences perfectly natively!
        distances, indices = self.index.search(faiss_query, min(top_k, self.index.ntotal))
        
        results = []
        for idx in indices[0]:  # type: ignore
            if idx != -1 and idx < len(self.document_chunks):
                results.append(self.document_chunks[idx])
                
        return results

# Expose Singleton Controller globally resolving physical Vector Databases inherently cleanly safely!
faiss_engine = FAISSRagEngine()
