# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Any, Optional, Union

import torch

from pytorch_lightning.plugins.collective import CollectivePlugin


class SingleDeviceCollective(CollectivePlugin):
    """Collective interface for single device training type plugins."""

    def barrier(self, name: Optional[str] = None, *args: Any, **kwargs: Any) -> None:
        pass

    def broadcast(self, obj: object, src: int = 0) -> object:
        return obj

    def all_gather(
        self, tensor: torch.Tensor, process_group: Optional[Any] = None, sync_grads: bool = False
    ) -> torch.Tensor:
        return tensor

    def reduce(self, tensor: Union[torch.Tensor, Any], *args: Any, **kwargs: Any) -> Union[torch.Tensor, Any]:
        return tensor
