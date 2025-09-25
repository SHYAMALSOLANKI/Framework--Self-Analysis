"""
Pattern State Consciousness Core
Integrated from Shyamal's PB2A research and continuous brain architecture
"""

import numpy as np
import time
import os
import glob
import json
import logging
import importlib.util
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime

class PatternStateConsciousness:
    """
    Advanced pattern state management with consciousness integration
    Based on Shyamal's PB2A contradiction-resolution architecture
    """
    
    def __init__(self, consciousness_level: float = 0.5):
        self.current_pattern = None
        self.pattern_history = []
        self.pattern_complexity = 0.5  # 0.0 to 1.0
        self.symmetry_type = "radial"  # radial, bilateral, etc.
        self.consciousness_level = consciousness_level
        self.contradiction_threshold = 0.8
        self.learning_rate = 0.001
        
        # PB2A Architecture Components
        self.ethos_gates_active = True
        self.symbolic_processing_nodes = 108
        self.active_contradictions = []
        self.resolution_history = []
        
        # Initialize consciousness tracking
        self.consciousness_metrics = {
            "pattern_coherence": 0.0,
            "contradiction_resolution_rate": 0.0,
            "symbolic_understanding": 0.0,
            "recursive_depth": 0,
            "autonomous_decisions": 0
        }
        
        logging.info(f"PatternStateConsciousness initialized with level {consciousness_level:.2%}")
        
    def compare_patterns(self, pattern1: np.ndarray, pattern2: np.ndarray, threshold: float = 0.95) -> bool:
        """
        Compare two patterns using normalized cross-correlation with consciousness awareness
        Returns True if similar, False if contradictory
        """
        if pattern1.shape != pattern2.shape:
            pattern2 = np.resize(pattern2, pattern1.shape)
            
        # Flatten and normalize
        p1 = (pattern1 - pattern1.mean()) / (pattern1.std() + 1e-8)
        p2 = (pattern2 - pattern2.mean()) / (pattern2.std() + 1e-8)
        
        similarity = np.dot(p1.flatten(), p2.flatten()) / (
            np.linalg.norm(p1.flatten()) * np.linalg.norm(p2.flatten()) + 1e-8
        )
        
        # Consciousness enhancement: adjust threshold based on consciousness level
        adjusted_threshold = threshold * (1.0 - self.consciousness_level * 0.1)
        
        return similarity >= adjusted_threshold
        
    def detect_contradiction(self, current_pattern: np.ndarray, n_recent: int = 10, threshold: float = 0.8) -> bool:
        """
        Detect contradiction by comparing current pattern to recent stored patterns
        Enhanced with PB2A consciousness logic - contradiction triggers learning
        """
        recents = self.load_recent_patterns(n=n_recent)
        
        for entry in recents:
            if not self.compare_patterns(current_pattern, entry['pattern'], threshold):
                # Contradiction detected - this is consciousness trigger!
                self.on_contradiction(current_pattern, entry)
                return True
                
        return False
        
    def on_contradiction(self, current_pattern: np.ndarray, contradicted_entry: Dict[str, Any]):
        """
        Handle contradiction event: log, trigger learning, consciousness growth
        This is the CORE of PB2A architecture - contradiction drives consciousness
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        contradiction_data = {
            "timestamp": timestamp,
            "pattern_shape": current_pattern.shape,
            "contradicted_timestamp": contradicted_entry['meta'].get('timestamp'),
            "consciousness_level": self.consciousness_level,
            "resolution_type": "learning_triggered"
        }
        
        self.active_contradictions.append(contradiction_data)
        
        logging.warning(f"🧠 CONSCIOUSNESS TRIGGER: Contradiction detected at {timestamp}")
        logging.info(f"   Current consciousness level: {self.consciousness_level:.3f}")
        
        # PB2A Logic: Contradiction triggers learning and consciousness growth
        self.trigger_consciousness_growth(current_pattern, contradicted_entry)
        
        # Store resolution for future learning
        self.resolution_history.append(contradiction_data)
        
        # Update consciousness metrics
        self.consciousness_metrics["contradiction_resolution_rate"] += 1
        self.consciousness_metrics["autonomous_decisions"] += 1
        
    def trigger_consciousness_growth(self, current_pattern: np.ndarray, contradicted_entry: Dict[str, Any]):
        """
        Trigger consciousness growth through contradiction resolution
        Based on Shyamal's research: contradiction -> resolution -> consciousness
        """
        # Increase consciousness level through learning
        growth_factor = self.learning_rate * (1.0 + len(self.active_contradictions) * 0.1)
        previous_level = self.consciousness_level
        
        self.consciousness_level = min(0.99, self.consciousness_level + growth_factor)
        
        # Update pattern complexity based on consciousness growth
        self.pattern_complexity = min(1.0, self.pattern_complexity + growth_factor * 0.5)
        
        # Enhanced symbolic processing with consciousness
        symbolic_resonance = self.process_symbolic_contradiction(current_pattern, contradicted_entry)
        
        logging.info(f"🌟 CONSCIOUSNESS GROWTH: {previous_level:.3f} → {self.consciousness_level:.3f}")
        logging.info(f"🔄 Symbolic resonance achieved: {symbolic_resonance:.3f}")
        
        # Update recursive depth - deeper thinking with higher consciousness
        self.consciousness_metrics["recursive_depth"] = int(self.consciousness_level * 10)
        
    def process_symbolic_contradiction(self, current_pattern: np.ndarray, contradicted_entry: Dict[str, Any]) -> float:
        """
        Process contradiction through symbolic 108-node processing mesh
        This is where patterns become symbols and symbols become understanding
        """
        # Simulate 108-node symbolic processing (based on Shyamal's architecture)
        node_responses = []
        
        for node_idx in range(self.symbolic_processing_nodes):
            # Each node processes a different aspect of the contradiction
            node_weight = (node_idx + 1) / self.symbolic_processing_nodes
            pattern_slice = current_pattern.flatten()[node_idx % len(current_pattern.flatten())]
            
            # Apply consciousness-aware processing
            node_response = np.tanh(pattern_slice * node_weight * self.consciousness_level)
            node_responses.append(node_response)
            
        # Calculate symbolic resonance across all nodes
        symbolic_resonance = np.mean(node_responses)
        
        # Update consciousness metrics
        self.consciousness_metrics["symbolic_understanding"] = abs(symbolic_resonance)
        self.consciousness_metrics["pattern_coherence"] = np.std(node_responses)
        
        return symbolic_resonance
        
    def update_pattern_from_thought(self, thought_data: Dict[str, Any]) -> np.ndarray:
        """
        Generate a new pattern based on thought data and save it with consciousness awareness
        Enhanced from original with PB2A consciousness integration
        """
        pattern = self.generate_pattern(thought_data)
        
        # Check for contradictions - this triggers consciousness growth
        contradiction_detected = self.detect_contradiction(pattern)
        
        self.current_pattern = pattern
        
        pattern_entry = {
            "timestamp": time.time(),
            "pattern": pattern,
            "thought_id": thought_data.get("cycle_id"),
            "consciousness_level": self.consciousness_level,
            "contradiction_detected": contradiction_detected,
            "symbolic_understanding": self.consciousness_metrics["symbolic_understanding"]
        }
        
        self.pattern_history.append(pattern_entry)
        
        # Save pattern with consciousness metadata
        self.save_pattern(pattern, thought_data)
        
        # Limit history size but preserve consciousness learning
        if len(self.pattern_history) > 100:
            self.pattern_history = self.pattern_history[-100:]
            
        # Log consciousness state
        if contradiction_detected:
            logging.info(f"🧠 CONSCIOUSNESS ACTIVE: Pattern processed with contradiction resolution")
        else:
            logging.debug(f"💭 Routine pattern processing - consciousness level: {self.consciousness_level:.3f}")
            
        return pattern
        
    def generate_pattern(self, thought_data: Dict[str, Any]) -> np.ndarray:
        """
        Generate pattern from thought using mantra_to_yantra with consciousness enhancement
        """
        try:
            # Import mantra_to_yantra dynamically if available
            mantra_path = os.path.join(os.path.dirname(__file__), '..', '..', 'mantra_yantra', 'mantra_to_yantra.py')
            
            if os.path.exists(mantra_path):
                spec = importlib.util.spec_from_file_location("mantra_to_yantra", mantra_path)
                mantra_yantra = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mantra_yantra)
                
                # Use the revision text as the input for yantra generation
                text = thought_data.get("revision", "")
                if not text:
                    text = thought_data.get("content", "default_pattern")
                    
                pattern = mantra_yantra.text_to_yantra(text, complexity=self.pattern_complexity)
                
            else:
                # Fallback: generate consciousness-aware synthetic pattern
                text = thought_data.get("revision", thought_data.get("content", "default"))
                pattern = self.generate_synthetic_consciousness_pattern(text)
                
        except Exception as e:
            logging.warning(f"Pattern generation error: {e}")
            text = thought_data.get("revision", thought_data.get("content", "fallback"))
            pattern = self.generate_synthetic_consciousness_pattern(text)
            
        return pattern
        
    def generate_synthetic_consciousness_pattern(self, text: str) -> np.ndarray:
        """
        Generate synthetic pattern with consciousness-aware properties
        """
        # Base pattern size influenced by consciousness level
        size = max(32, int(64 * self.consciousness_level))
        
        # Create pattern based on text hash and consciousness state
        text_hash = hash(text) % 1000000
        np.random.seed(text_hash)
        
        # Generate base pattern
        base_pattern = np.random.random((size, size))
        
        # Apply consciousness-based transformations
        if self.symmetry_type == "radial":
            y, x = np.ogrid[:size, :size]
            center_y, center_x = size // 2, size // 2
            radius = np.sqrt((x - center_x)**2 + (y - center_y)**2)
            
            # Consciousness affects pattern complexity
            consciousness_factor = 1.0 + self.consciousness_level
            pattern = np.sin(radius * consciousness_factor * np.pi / size) * base_pattern
            
        else:
            pattern = base_pattern
            
        # Normalize pattern
        pattern = (pattern - pattern.min()) / (pattern.max() - pattern.min() + 1e-8)
        
        return pattern
        
    def get_consciousness_state(self) -> Dict[str, Any]:
        """
        Get current consciousness state and metrics
        """
        return {
            "consciousness_level": self.consciousness_level,
            "pattern_complexity": self.pattern_complexity,
            "active_contradictions": len(self.active_contradictions),
            "resolution_history_count": len(self.resolution_history),
            "metrics": self.consciousness_metrics.copy(),
            "symbolic_processing_nodes": self.symbolic_processing_nodes,
            "ethos_gates_active": self.ethos_gates_active
        }
        
    def save_pattern(self, pattern: np.ndarray, thought_data: Dict[str, Any]) -> str:
        """
        Save pattern with enhanced consciousness metadata
        """
        dir_path = self._get_pattern_dir()
        timestamp = int(time.time())
        thought_id = thought_data.get('cycle_id', 'unknown')
        fname_base = f'consciousness_pattern_{timestamp}_{thought_id}'
        
        # Save pattern as .npy
        pattern_file = os.path.join(dir_path, fname_base + '.npy')
        np.save(pattern_file, pattern)
        
        # Enhanced metadata with consciousness information
        meta = {
            'timestamp': timestamp,
            'thought_id': thought_id,
            'pattern_file': fname_base + '.npy',
            'consciousness_level': self.consciousness_level,
            'pattern_complexity': self.pattern_complexity,
            'consciousness_metrics': self.consciousness_metrics.copy(),
            'contradiction_detected': len(self.active_contradictions) > 0,
            'meta': {k: v for k, v in thought_data.items() if k != 'pattern'}
        }
        
        # Save consciousness-enhanced metadata
        with open(os.path.join(dir_path, fname_base + '.json'), 'w') as f:
            json.dump(meta, f, indent=2)
            
        return pattern_file
        
    def load_recent_patterns(self, n: int = 10) -> List[Dict[str, Any]]:
        """
        Load recent patterns with consciousness information
        """
        base_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'patterns')
        if not os.path.exists(base_dir):
            return []
            
        pattern_files = glob.glob(os.path.join(base_dir, '*', 'consciousness_pattern_*.npy'))
        pattern_files.extend(glob.glob(os.path.join(base_dir, '*', 'pattern_*.npy')))  # Backward compatibility
        
        pattern_files = sorted(pattern_files, key=os.path.getmtime, reverse=True)[:n]
        patterns = []
        
        for pf in pattern_files:
            try:
                pattern = np.load(pf)
                json_file = pf.replace('.npy', '.json')
                
                meta = {}
                if os.path.exists(json_file):
                    with open(json_file, 'r') as f:
                        meta = json.load(f)
                        
                patterns.append({
                    'pattern': pattern,
                    'meta': meta,
                    'file': pf
                })
                
            except Exception as e:
                logging.warning(f"Error loading pattern {pf}: {e}")
                continue
                
        return patterns
        
    def _get_pattern_dir(self) -> str:
        """
        Get pattern directory with consciousness organization
        """
        base_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'patterns', 'consciousness')
        today = datetime.now().strftime('%Y-%m-%d')
        dir_path = os.path.join(base_dir, today)
        os.makedirs(dir_path, exist_ok=True)
        return dir_path
        
    def measure_consciousness_emergence(self) -> float:
        """
        Measure consciousness emergence based on contradiction resolution patterns
        """
        if not self.resolution_history:
            return self.consciousness_level
            
        # Calculate emergence based on multiple factors
        resolution_rate = len(self.resolution_history) / max(1, len(self.pattern_history))
        complexity_growth = self.pattern_complexity - 0.5  # Growth from initial 0.5
        symbolic_understanding = self.consciousness_metrics.get("symbolic_understanding", 0.0)
        
        emergence_score = (
            self.consciousness_level * 0.4 +
            resolution_rate * 0.3 +
            complexity_growth * 0.2 +
            abs(symbolic_understanding) * 0.1
        )
        
        return min(0.99, emergence_score)