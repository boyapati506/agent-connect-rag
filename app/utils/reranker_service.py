from sentence_transformers import CrossEncoder


class RerankerService:

    def __init__(self):
        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(self, query: str, candidates: list[dict]) -> list[dict]:
        pairs = []

        for candidate in candidates:
            pairs.append([
                query,
                candidate["text"]
            ])

        scores = self.model.predict(pairs)

        results = []

        for candidate, score in zip(candidates, scores):
            results.append({
                **candidate,
                "rerank_score": float(score)
            })

        results.sort(
            key=lambda x: x["rerank_score"],
            reverse=True
        )

        return results