from dataclasses import dataclass, field
from typing import Any

@dataclass
class AgentState :
    query: str
    messages:list[dict] =field(default_factory=list)
    plan: list[str]= field(default_factory=list)
    observations = list[Any] = field(default_factory=list)
    steps: int = 0
    done: bool= False


