from abc import ABC, abstractmethod
from typing import Dict, Any


class ContentBoosterContract(ABC):
    """
    Public Architectural Contract

    This interface demonstrates the public capabilities of the
    Nexus Content Booster platform while keeping the production
    implementation private.
    """

    @abstractmethod
    def analyze(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze content for optimization."""
        raise NotImplementedError

    @abstractmethod
    def optimize(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Route content through the optimization pipeline."""
        raise NotImplementedError

    @abstractmethod
    def generate_metadata(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Generate SEO-ready metadata."""
        raise NotImplementedError
