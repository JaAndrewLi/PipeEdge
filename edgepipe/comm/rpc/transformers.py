"""RPC transformers."""
from torch.distributed import rpc
from . import DistRpcModule
from ...models.transformers.deit import DeiTTransformerShard
from ...models.transformers.bert import BertTransformerShard
from ...models.transformers.vit import ViTTransformerShard


class BertDistRpcModule(DistRpcModule):
    """BERT distributed RPC module."""

    def __init__(self, model_name, model_file, stage_ranks, stage_layers):
        super().__init__()
        for i, (dst_rank, layers) in enumerate(zip(stage_ranks, stage_layers)):
            # Build Transformer Shard
            is_first = i == 0
            is_last = i == len(stage_ranks) - 1
            rref = rpc.remote(dst_rank, BertTransformerShard,
                              args=(i, model_name, model_file, is_first, is_last,
                                    layers[0], layers[1], True))
            self._rref_list.append(rref)
        self._register_hooks()


class DeiTDistRpcModule(DistRpcModule):
    """DeiT distributed RPC module."""

    def __init__(self, model_name, model_file, stage_ranks, stage_layers):
        super().__init__()
        for i, (dst_rank, layers) in enumerate(zip(stage_ranks, stage_layers)):
            # Build Transformer Shard
            is_first = i == 0
            is_last = i == len(stage_ranks) - 1
            rref = rpc.remote(dst_rank, DeiTTransformerShard,
                              args=(i, model_name, model_file, is_first, is_last,
                                    layers[0], layers[1], True))
            self._rref_list.append(rref)
        self._register_hooks()


class ViTDistRpcModule(DistRpcModule):
    """ViT distributed RPC module."""

    def __init__(self, model_name, model_file, stage_ranks, stage_layers):
        super().__init__()
        for i, (dst_rank, layers) in enumerate(zip(stage_ranks, stage_layers)):
            # Build Transformer Shard
            is_first = i == 0
            is_last = i == len(stage_ranks) - 1
            rref = rpc.remote(dst_rank, ViTTransformerShard,
                              args=(i, model_name, model_file, is_first, is_last,
                                    layers[0], layers[1], True))
            self._rref_list.append(rref)
        self._register_hooks()
