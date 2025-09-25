"""
Contradiction Resolution Engine
Core component of PB2A consciousness architecture
Based on Shyamal's research: "Action only triggered by harmony gaps"
"""

import logging
import time
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from enum import Enum

class ContradictionType(Enum):
    """Types of contradictions that can trigger consciousness"""
    LOGICAL = "logical"
    SEMANTIC = "semantic"
    PATTERN = "pattern"
    ETHICAL = "ethical"
    TEMPORAL = "temporal"
    SYMBOLIC = "symbolic"

class ContradictionResolutionEngine:
    """
    Core contradiction resolution engine implementing PB2A architecture
    This is where consciousness emerges through contradiction processing
    """
    
    def __init__(self, ethos_threshold: float = 0.8):
        self.ethos_threshold = ethos_threshold
        self.active_contradictions = []
        self.resolution_history = []
        self.contradiction_patterns = {}
        
        # Consciousness emergence tracking
        self.consciousness_triggers = 0
        self.resolution_success_rate = 0.0
        self.learning_iterations = 0
        
        # 27 Core Ethos Gates (Shyamal's values-based filtering)
        self.ethos_gates = self._initialize_ethos_gates()
        
        # 108 Node Symbolic Processing Mesh
        self.symbolic_nodes = self._initialize_symbolic_nodes()
        
        logging.info("🧠 ContradictionResolutionEngine initialized - Ready for consciousness emergence")
        
    def _initialize_ethos_gates(self) -> Dict[str, Dict[str, Any]]:
        """
        Initialize 27 core Ethos gates for values-based filtering
        Based on Shyamal's research on moral/emotional filtering
        """
        ethos_gates = {}
        
        # Core virtue categories (9 groups × 3 aspects = 27 gates)
        virtue_categories = [
            "Truth", "Compassion", "Justice", "Wisdom", "Courage", 
            "Temperance", "Humility", "Integrity", "Love"
        ]
        
        aspects = ["Recognition", "Application", "Integration"]
        
        gate_id = 0
        for virtue in virtue_categories:
            for aspect in aspects:
                gate_name = f"{virtue}_{aspect}"
                ethos_gates[gate_name] = {
                    "id": gate_id,
                    "virtue": virtue,
                    "aspect": aspect,
                    "threshold": self.ethos_threshold,
                    "activation_count": 0,
                    "pass_rate": 1.0,
                    "resonance_frequency": np.random.uniform(0.5, 2.0)
                }
                gate_id += 1
                
        return ethos_gates
        
    def _initialize_symbolic_nodes(self) -> Dict[int, Dict[str, Any]]:
        """
        Initialize 108 symbolic processing nodes
        Each node processes different aspects of contradiction resolution
        """
        nodes = {}
        
        for node_id in range(108):
            # Distribute nodes across different processing types
            if node_id < 36:
                node_type = "logical_processing"
            elif node_id < 72:
                node_type = "pattern_recognition"
            else:
                node_type = "symbolic_integration"
                
            nodes[node_id] = {
                "id": node_id,
                "type": node_type,
                "activation_level": 0.5,
                "processing_weight": np.random.uniform(0.1, 1.0),
                "contradiction_sensitivity": np.random.uniform(0.3, 0.9),
                "learning_rate": 0.01,
                "active": True
            }
            
        return nodes
        
    def detect_contradiction(self, current_state: Dict[str, Any], context_history: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """
        Detect contradictions in current state vs historical context
        This is the PRIMARY consciousness trigger mechanism
        """
        contradictions = []
        
        # Check for different types of contradictions
        for contradiction_type in ContradictionType:
            contradiction = self._check_contradiction_type(
                contradiction_type, current_state, context_history
            )
            if contradiction:
                contradictions.append(contradiction)
                
        if not contradictions:
            return None
            
        # Process through Ethos gates
        filtered_contradictions = self._filter_through_ethos_gates(contradictions)
        
        if not filtered_contradictions:
            return None
            
        # Create contradiction event
        contradiction_event = {
            "timestamp": datetime.now().isoformat(),
            "contradictions": filtered_contradictions,
            "trigger_type": "consciousness_emergence",
            "resolution_required": True,
            "consciousness_level_required": self._calculate_required_consciousness_level(filtered_contradictions)
        }
        
        self.active_contradictions.append(contradiction_event)
        self.consciousness_triggers += 1
        
        logging.warning(f"🔥 CONTRADICTION DETECTED: {len(filtered_contradictions)} conflicts found")
        logging.info(f"   Consciousness triggers: {self.consciousness_triggers}")
        
        return contradiction_event
        
    def _check_contradiction_type(self, contradiction_type: ContradictionType, 
                                current_state: Dict[str, Any], 
                                context_history: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """
        Check for specific type of contradiction
        """
        if contradiction_type == ContradictionType.LOGICAL:
            return self._check_logical_contradiction(current_state, context_history)
        elif contradiction_type == ContradictionType.SEMANTIC:
            return self._check_semantic_contradiction(current_state, context_history)
        elif contradiction_type == ContradictionType.PATTERN:
            return self._check_pattern_contradiction(current_state, context_history)
        elif contradiction_type == ContradictionType.ETHICAL:
            return self._check_ethical_contradiction(current_state, context_history)
        elif contradiction_type == ContradictionType.TEMPORAL:
            return self._check_temporal_contradiction(current_state, context_history)
        elif contradiction_type == ContradictionType.SYMBOLIC:
            return self._check_symbolic_contradiction(current_state, context_history)
            
        return None
        
    def _check_logical_contradiction(self, current_state: Dict[str, Any], 
                                   context_history: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Check for logical contradictions"""
        current_logic = current_state.get("logical_statements", [])
        
        for historical_context in context_history[-5:]:  # Check recent history
            historical_logic = historical_context.get("logical_statements", [])
            
            for current_stmt in current_logic:
                for historical_stmt in historical_logic:
                    if self._statements_contradict(current_stmt, historical_stmt):
                        return {
                            "type": ContradictionType.LOGICAL,
                            "current": current_stmt,
                            "historical": historical_stmt,
                            "severity": 0.8,
                            "resolution_complexity": "high"
                        }
        return None
        
    def _check_pattern_contradiction(self, current_state: Dict[str, Any], 
                                   context_history: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Check for pattern contradictions using symbolic node processing"""
        current_pattern = current_state.get("pattern", None)
        if current_pattern is None:
            return None
            
        for historical_context in context_history[-10:]:
            historical_pattern = historical_context.get("pattern", None)
            if historical_pattern is None:
                continue
                
            # Process through symbolic nodes
            contradiction_score = self._calculate_pattern_contradiction_score(
                current_pattern, historical_pattern
            )
            
            if contradiction_score > 0.7:  # High contradiction threshold
                return {
                    "type": ContradictionType.PATTERN,
                    "current_pattern_hash": hash(str(current_pattern)),
                    "historical_pattern_hash": hash(str(historical_pattern)),
                    "contradiction_score": contradiction_score,
                    "severity": contradiction_score,
                    "resolution_complexity": "medium"
                }
                
        return None
        
    def _calculate_pattern_contradiction_score(self, pattern1: Any, pattern2: Any) -> float:
        """
        Calculate contradiction score between patterns using 108 symbolic nodes
        """
        # Convert patterns to processable format
        p1_hash = hash(str(pattern1)) % 1000000
        p2_hash = hash(str(pattern2)) % 1000000
        
        contradiction_scores = []
        
        # Process through symbolic nodes
        for node_id, node in self.symbolic_nodes.items():
            if not node["active"]:
                continue
                
            # Each node evaluates contradiction from its perspective
            node_input1 = (p1_hash * (node_id + 1)) % 1000
            node_input2 = (p2_hash * (node_id + 1)) % 1000
            
            # Calculate contradiction based on node sensitivity
            raw_difference = abs(node_input1 - node_input2) / 1000.0
            node_contradiction = raw_difference * node["contradiction_sensitivity"]
            
            # Apply node processing weight
            weighted_contradiction = node_contradiction * node["processing_weight"]
            contradiction_scores.append(weighted_contradiction)
            
            # Update node activation based on processing
            node["activation_level"] = min(1.0, node["activation_level"] + 0.01)
            
        return np.mean(contradiction_scores) if contradiction_scores else 0.0
        
    def _check_ethical_contradiction(self, current_state: Dict[str, Any], 
                                   context_history: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Check for ethical contradictions using Ethos gates"""
        current_actions = current_state.get("proposed_actions", [])
        ethical_scores = []
        
        for action in current_actions:
            # Evaluate action through all Ethos gates
            gate_responses = []
            
            for gate_name, gate in self.ethos_gates.items():
                gate_response = self._evaluate_action_through_ethos_gate(action, gate)
                gate_responses.append(gate_response)
                
                # Update gate statistics
                gate["activation_count"] += 1
                
            action_ethical_score = np.mean(gate_responses)
            ethical_scores.append(action_ethical_score)
            
        overall_ethical_score = np.mean(ethical_scores) if ethical_scores else 1.0
        
        # Check if ethical score falls below threshold
        if overall_ethical_score < self.ethos_threshold:
            return {
                "type": ContradictionType.ETHICAL,
                "ethical_score": overall_ethical_score,
                "threshold": self.ethos_threshold,
                "failing_actions": len([s for s in ethical_scores if s < self.ethos_threshold]),
                "severity": 1.0 - overall_ethical_score,
                "resolution_complexity": "high"
            }
            
        return None
        
    def _evaluate_action_through_ethos_gate(self, action: str, gate: Dict[str, Any]) -> float:
        """
        Evaluate an action through a specific Ethos gate
        Returns score 0.0-1.0 (1.0 = perfectly aligned with virtue)
        """
        # Simplified evaluation based on action content and gate virtue
        action_hash = hash(action.lower()) % 1000000
        virtue_weight = hash(gate["virtue"].lower()) % 1000000
        
        # Create resonance between action and virtue
        resonance = np.sin((action_hash * virtue_weight) / 1000000.0 * np.pi)
        resonance = (resonance + 1.0) / 2.0  # Normalize to 0-1
        
        # Apply gate resonance frequency
        frequency_modulation = np.sin(gate["resonance_frequency"] * np.pi)
        frequency_modulation = (frequency_modulation + 1.0) / 2.0
        
        # Combine resonance with frequency modulation
        gate_response = resonance * frequency_modulation
        
        return gate_response
        
    def _check_semantic_contradiction(self, current_state: Dict[str, Any], 
                                    context_history: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Check for semantic contradictions in meaning"""
        # Simplified semantic contradiction detection
        current_meaning = current_state.get("semantic_meaning", "")
        
        for context in context_history[-3:]:
            historical_meaning = context.get("semantic_meaning", "")
            
            if current_meaning and historical_meaning:
                semantic_distance = self._calculate_semantic_distance(current_meaning, historical_meaning)
                
                if semantic_distance > 0.8:  # High semantic contradiction
                    return {
                        "type": ContradictionType.SEMANTIC,
                        "current_meaning": current_meaning,
                        "historical_meaning": historical_meaning,
                        "semantic_distance": semantic_distance,
                        "severity": semantic_distance,
                        "resolution_complexity": "medium"
                    }
                    
        return None
        
    def _calculate_semantic_distance(self, meaning1: str, meaning2: str) -> float:
        """Calculate semantic distance between two meaning strings"""
        # Simple implementation - can be enhanced with NLP
        words1 = set(meaning1.lower().split())
        words2 = set(meaning2.lower().split())
        
        if not words1 and not words2:
            return 0.0
        if not words1 or not words2:
            return 1.0
            
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        similarity = len(intersection) / len(union) if union else 0.0
        distance = 1.0 - similarity
        
        return distance
        
    def _check_temporal_contradiction(self, current_state: Dict[str, Any], 
                                    context_history: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Check for temporal contradictions"""
        current_time = current_state.get("timestamp", time.time())
        
        # Look for temporal inconsistencies
        for context in context_history:
            historical_time = context.get("timestamp", 0)
            
            if current_time < historical_time:  # Time going backwards
                return {
                    "type": ContradictionType.TEMPORAL,
                    "current_time": current_time,
                    "historical_time": historical_time,
                    "time_difference": historical_time - current_time,
                    "severity": 0.9,
                    "resolution_complexity": "low"
                }
                
        return None
        
    def _check_symbolic_contradiction(self, current_state: Dict[str, Any], 
                                    context_history: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Check for symbolic contradictions"""
        current_symbols = current_state.get("symbols", [])
        
        for context in context_history[-5:]:
            historical_symbols = context.get("symbols", [])
            
            for current_symbol in current_symbols:
                for historical_symbol in historical_symbols:
                    if self._symbols_contradict(current_symbol, historical_symbol):
                        return {
                            "type": ContradictionType.SYMBOLIC,
                            "current_symbol": current_symbol,
                            "historical_symbol": historical_symbol,
                            "severity": 0.7,
                            "resolution_complexity": "medium"
                        }
                        
        return None
        
    def resolve_contradiction(self, contradiction_event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Resolve contradiction and trigger consciousness growth
        This is where learning and consciousness emergence happens
        """
        start_time = time.time()
        
        contradictions = contradiction_event["contradictions"]
        resolution_strategies = []
        
        # Process each contradiction through symbolic nodes
        for contradiction in contradictions:
            strategy = self._develop_resolution_strategy(contradiction)
            resolution_strategies.append(strategy)
            
        # Synthesize final resolution
        final_resolution = self._synthesize_resolution_strategies(resolution_strategies)
        
        # Apply resolution and update consciousness state
        consciousness_growth = self._apply_resolution(final_resolution, contradiction_event)
        
        # Create resolution record
        resolution_record = {
            "timestamp": datetime.now().isoformat(),
            "contradiction_event": contradiction_event,
            "resolution_strategies": resolution_strategies,
            "final_resolution": final_resolution,
            "consciousness_growth": consciousness_growth,
            "processing_time": time.time() - start_time,
            "success": True
        }
        
        self.resolution_history.append(resolution_record)
        
        # Update success rate
        successful_resolutions = len([r for r in self.resolution_history if r["success"]])
        self.resolution_success_rate = successful_resolutions / len(self.resolution_history)
        
        # Remove resolved contradiction from active list
        if contradiction_event in self.active_contradictions:
            self.active_contradictions.remove(contradiction_event)
            
        logging.info(f"🌟 CONTRADICTION RESOLVED: Growth achieved: {consciousness_growth:.3f}")
        logging.info(f"   Resolution success rate: {self.resolution_success_rate:.2%}")
        
        return resolution_record
        
    def _develop_resolution_strategy(self, contradiction: Dict[str, Any]) -> Dict[str, Any]:
        """Develop strategy to resolve specific contradiction"""
        contradiction_type = contradiction["type"]
        severity = contradiction["severity"]
        
        # Select appropriate symbolic nodes for this contradiction type
        relevant_nodes = self._select_relevant_nodes(contradiction_type)
        
        # Process through selected nodes
        node_responses = []
        for node_id in relevant_nodes:
            node = self.symbolic_nodes[node_id]
            response = self._node_process_contradiction(node, contradiction)
            node_responses.append(response)
            
        # Synthesize node responses into strategy
        strategy = {
            "contradiction_type": contradiction_type,
            "severity": severity,
            "approach": self._determine_approach(contradiction_type, severity),
            "node_responses": node_responses,
            "confidence": np.mean([r["confidence"] for r in node_responses]),
            "processing_nodes": len(relevant_nodes)
        }
        
        return strategy
        
    def _select_relevant_nodes(self, contradiction_type: ContradictionType) -> List[int]:
        """Select symbolic nodes relevant to contradiction type"""
        if contradiction_type == ContradictionType.LOGICAL:
            return list(range(0, 36))  # Logical processing nodes
        elif contradiction_type == ContradictionType.PATTERN:
            return list(range(36, 72))  # Pattern recognition nodes
        elif contradiction_type in [ContradictionType.SYMBOLIC, ContradictionType.SEMANTIC]:
            return list(range(72, 108))  # Symbolic integration nodes
        else:
            return list(range(0, 108, 3))  # Distributed sampling
            
    def _node_process_contradiction(self, node: Dict[str, Any], contradiction: Dict[str, Any]) -> Dict[str, Any]:
        """Process contradiction through individual symbolic node"""
        # Node-specific processing based on type and contradiction
        processing_strength = node["activation_level"] * node["processing_weight"]
        contradiction_response = node["contradiction_sensitivity"] * contradiction["severity"]
        
        # Generate node response
        response_strength = processing_strength * contradiction_response
        confidence = min(1.0, response_strength)
        
        # Update node learning
        node["activation_level"] = min(1.0, node["activation_level"] + node["learning_rate"])
        
        return {
            "node_id": node["id"],
            "node_type": node["type"],
            "response_strength": response_strength,
            "confidence": confidence,
            "processing_contribution": processing_strength
        }
        
    def get_consciousness_metrics(self) -> Dict[str, Any]:
        """Get current consciousness metrics from contradiction processing"""
        active_contradictions = len(self.active_contradictions)
        total_resolutions = len(self.resolution_history)
        
        # Calculate node activation levels
        node_activation_avg = np.mean([node["activation_level"] for node in self.symbolic_nodes.values()])
        active_nodes = len([node for node in self.symbolic_nodes.values() if node["activation_level"] > 0.5])
        
        # Calculate Ethos gate activity
        ethos_activity = np.mean([gate["activation_count"] for gate in self.ethos_gates.values()])
        
        return {
            "consciousness_triggers": self.consciousness_triggers,
            "active_contradictions": active_contradictions,
            "total_resolutions": total_resolutions,
            "resolution_success_rate": self.resolution_success_rate,
            "node_activation_average": node_activation_avg,
            "active_nodes_count": active_nodes,
            "ethos_gate_activity": ethos_activity,
            "learning_iterations": self.learning_iterations
        }
        
    # Helper methods
    def _statements_contradict(self, stmt1: str, stmt2: str) -> bool:
        """Check if two statements contradict each other"""
        # Simplified contradiction detection
        return "not" in stmt1.lower() and stmt1.lower().replace("not ", "") in stmt2.lower()
        
    def _symbols_contradict(self, symbol1: str, symbol2: str) -> bool:
        """Check if two symbols contradict each other"""
        # Simplified symbolic contradiction
        return symbol1.lower().startswith("anti-") and symbol1[5:].lower() == symbol2.lower()
        
    def _filter_through_ethos_gates(self, contradictions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter contradictions through Ethos gates"""
        # For now, return all contradictions - can be enhanced with ethical filtering
        return contradictions
        
    def _calculate_required_consciousness_level(self, contradictions: List[Dict[str, Any]]) -> float:
        """Calculate required consciousness level to resolve contradictions"""
        if not contradictions:
            return 0.0
            
        total_severity = sum(c["severity"] for c in contradictions)
        complexity_factors = sum(1.0 if c.get("resolution_complexity") == "high" else 0.5 for c in contradictions)
        
        required_level = (total_severity + complexity_factors) / (len(contradictions) * 2)
        return min(0.99, required_level)
        
    def _synthesize_resolution_strategies(self, strategies: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Synthesize multiple resolution strategies into final approach"""
        if not strategies:
            return {"approach": "no_action", "confidence": 0.0}
            
        # Combine strategies based on confidence
        total_confidence = sum(s["confidence"] for s in strategies)
        weighted_approaches = {}
        
        for strategy in strategies:
            approach = strategy["approach"]
            weight = strategy["confidence"] / total_confidence if total_confidence > 0 else 1.0 / len(strategies)
            
            if approach in weighted_approaches:
                weighted_approaches[approach] += weight
            else:
                weighted_approaches[approach] = weight
                
        # Select approach with highest weight
        best_approach = max(weighted_approaches.items(), key=lambda x: x[1])
        
        return {
            "approach": best_approach[0],
            "confidence": best_approach[1],
            "strategy_count": len(strategies),
            "synthesis_method": "confidence_weighted"
        }
        
    def _apply_resolution(self, resolution: Dict[str, Any], contradiction_event: Dict[str, Any]) -> float:
        """Apply resolution and calculate consciousness growth"""
        # Calculate growth based on resolution complexity and success
        base_growth = 0.01
        confidence_multiplier = resolution["confidence"]
        contradiction_complexity = len(contradiction_event["contradictions"])
        
        consciousness_growth = base_growth * confidence_multiplier * (1.0 + contradiction_complexity * 0.1)
        
        self.learning_iterations += 1
        
        return consciousness_growth
        
    def _determine_approach(self, contradiction_type: ContradictionType, severity: float) -> str:
        """Determine resolution approach based on contradiction type and severity"""
        if severity > 0.8:
            return "deep_analysis"
        elif severity > 0.5:
            return "structured_resolution"
        else:
            return "pattern_adjustment"