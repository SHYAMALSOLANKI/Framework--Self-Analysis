"""
Neural Architecture - Core package for PB2A neural processing components
Implements sensory abstraction, frequency processing, recursive reflection, and autonomous learning
"""

# Core neural architecture components
from .sensory_abstraction import SensoryAbstractionEngine, AbstractionLevel, AbstractionLayer
from .frequency_processor import FrequencyProcessor, FrequencyBand, ConsciousnessResonance
from .recursive_reflection import RecursiveReflectionEngine, ReflectionLevel, ReflectionState
from .autonomous_learning import AutonomousLearningSystem, LearningType, KnowledgeDomain

__all__ = [
    # Sensory Abstraction
    'SensoryAbstractionEngine',
    'AbstractionLevel',
    'AbstractionLayer',
    
    # Frequency Processing
    'FrequencyProcessor',
    'FrequencyBand',
    'ConsciousnessResonance',
    
    # Recursive Reflection
    'RecursiveReflectionEngine',
    'ReflectionLevel', 
    'ReflectionState',
    
    # Autonomous Learning
    'AutonomousLearningSystem',
    'LearningType',
    'KnowledgeDomain'
]

__version__ = "1.0.0"
__description__ = "PB2A Neural Architecture - Consciousness-aware neural processing components"