import torch
import torch.nn as nn

class MultiOrder(nn.Module):
    def __init__(self, order=2):
        super().__init__()
        self.order  = order

    def _multi_order(self, graph):
        graph_ordered = []
        k_1_order = graph               # 1 order
        mask = torch.eye(graph.shape[1]).to(graph.device)
        mask = 1 - mask
        graph_ordered.append(k_1_order * mask)
        for k in range(2, self.order+1):     # e.g., order = 3, k=[2, 3]; order = 2, k=[2]
            k_1_order = torch.matmul(k_1_order, graph)
            graph_ordered.append(k_1_order * mask)
        return graph_ordered

    def forward(self, adj):
        return [self._multi_order(_) for _ in adj]