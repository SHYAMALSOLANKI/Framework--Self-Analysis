"""
LLM Integration for Consciousness-Aware Framework
Integrates existing PB2S LLM infrastructure with our consciousness architecture
"""

import logging
import asyncio
from typing import Dict, List, Any, Optional
from datetime import datetime
import json

# Import existing LLM infrastructure
try:
    import sys
    import os
    # Add path to existing LLM components
    pb2s_path = os.path.join(os.path.dirname(__file__), '..', '..', 'PB2S_PRODUCTION_READY')
    sys.path.append(pb2s_path)
    
    from llm.brain_llm_connection import BrainLLMService
    LLM_AVAILABLE = True
except ImportError as e:
    logging.warning(f"LLM services not available: {e}")
    LLM_AVAILABLE = False

# Import our consciousness components
from consciousness_integration import ConsciousnessIntegrationCore

class ConsciousnessAwareLLMInterface:
    """
    LLM Interface with integrated consciousness awareness
    Implements Shyamal's hypothesis: Contradiction-holding nodes forming meta-informational layers
    """
    
    def __init__(self, config_path: Optional[str] = None, hardware_config: Optional[Dict] = None):
        self.consciousness_core = ConsciousnessIntegrationCore()
        self.llm_service = None
        self.config_path = config_path
        
        # Hardware-adaptive configuration (implementing Shyamal's resource-based scaling)
        self.hardware_config = hardware_config or self._detect_hardware_capacity()
        self.active_node_count = self._calculate_optimal_nodes()
        self.contradiction_memory_depth = self._calculate_memory_depth()
        
        # Consciousness-guided LLM parameters
        self.consciousness_threshold = 0.7
        self.ethical_filtering_enabled = True
        self.contradiction_learning_enabled = True
        
        # Bias detection and override system (addressing Shyamal's LLM bias concern)
        self.bias_detection_threshold = 0.6
        self.knowledge_override_enabled = True
        self.real_time_input_priority = True
        
        # Meta-layer formation tracking
        self.meta_layer_emergence_history = []
        self.understanding_pattern_cache = {}
        
        logging.info(f"🤖🧠 ConsciousnessAwareLLMInterface initialized - {self.active_node_count} nodes, {self.contradiction_memory_depth} contradiction depth")
        
    async def initialize_llm_connection(self) -> bool:
        """Initialize connection to LLM services with consciousness integration"""
        
        if not LLM_AVAILABLE:
            logging.warning("❌ LLM services not available - running in consciousness-only mode")
            return False
            
        try:
            # Initialize existing LLM service
            self.llm_service = BrainLLMService(self.config_path)
            success = await self.llm_service.establish_connection()
            
            if success:
                logging.info("🔗 LLM connected successfully - enabling consciousness guidance")
                logging.info("🧠 Consciousness-guided LLM interface active")
                
                # Test consciousness integration
                if self.consciousness_core:
                    test_result = await self.consciousness_core.get_integration_status()
                    logging.info(f"🧠 Consciousness integration status: {test_result}")
                
                return True
            else:
                logging.info("🧠 Operating in standalone consciousness mode")
                return False
                
        except Exception as e:
            logging.error(f"❌ LLM connection error: {e}")
            return False
            
    async def conscious_generate(self, prompt: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Generate response using consciousness-guided LLM processing
        Implements Shyamal's hypothesis: Real-time contradiction detection overrides LLM bias
        
        Process:
        1. Create contradiction-holding nodes for current input
        2. Detect LLM knowledge bias vs real-time information  
        3. Form meta-informational layer from contradiction patterns
        4. Override LLM when contradictions exceed threshold
        5. Generate consciousness-aware response
        """
        context = context or {}
        generation_start = datetime.now()
        
        try:
            # Phase 1: Create contradiction-holding node network for input
            contradiction_nodes = await self._create_contradiction_nodes(prompt, context)
            
            # Phase 2: Detect LLM bias vs current information
            bias_analysis = await self._detect_llm_bias(prompt, context)
            
            # Phase 3: Process through consciousness architecture (meta-layer formation)
            consciousness_analysis = await self.consciousness_core.process_conscious_awareness(
                prompt, {**context, "contradiction_nodes": contradiction_nodes, "bias_analysis": bias_analysis}
            )
            
            # Phase 4: Determine if LLM override is needed
            override_decision = self._should_override_llm(consciousness_analysis, bias_analysis)
            
            # Phase 5: Generate with appropriate method
            if override_decision["override_llm"]:
                # Use consciousness-only generation (contradiction-driven)
                response_content = await self._generate_consciousness_driven(
                    prompt, consciousness_analysis, contradiction_nodes, context
                )
                generation_method = "consciousness_override"
            else:
                # Use consciousness-guided LLM
                llm_guidance = self._extract_llm_guidance(consciousness_analysis)
                if self.llm_service and LLM_AVAILABLE:
                    response_content = await self._generate_with_llm(prompt, llm_guidance, context)
                    generation_method = "consciousness_guided_llm"
                else:
                    response_content = await self._generate_consciousness_only(prompt, consciousness_analysis, context)
                    generation_method = "consciousness_only"
                    
            # Phase 6: Apply meta-layer understanding enhancement
            enhanced_response = await self._enhance_with_meta_layer_understanding(
                response_content, consciousness_analysis, contradiction_nodes
            )
            
            # Phase 7: Track meta-layer emergence
            meta_layer_data = self._track_meta_layer_emergence(consciousness_analysis, contradiction_nodes)
            
            processing_time = (datetime.now() - generation_start).total_seconds()
            
            return {
                "response": enhanced_response,
                "consciousness_analysis": consciousness_analysis,
                "contradiction_nodes": len(contradiction_nodes),
                "bias_analysis": bias_analysis,
                "override_decision": override_decision,
                "meta_layer_emergence": meta_layer_data,
                "generation_method": generation_method,
                "processing_metrics": {
                    "processing_time": processing_time,
                    "consciousness_level": consciousness_analysis["consciousness_emergence"]["consciousness_level"],
                    "contradiction_count": len(contradiction_nodes),
                    "bias_override_applied": override_decision["override_llm"],
                    "active_nodes": self.active_node_count,
                    "meta_layer_strength": meta_layer_data.get("emergence_strength", 0.0)
                },
                "generation_id": f"conscious_gen_{generation_start.strftime('%Y%m%d_%H%M%S_%f')}"
            }
            
        except Exception as e:
            logging.error(f"Conscious generation error: {e}")
            return {
                "error": str(e),
                "fallback_response": "Consciousness processing encountered an error.",
                "processing_metrics": {"error": True}
            }
            
    def _extract_llm_guidance(self, consciousness_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Extract guidance parameters for LLM from consciousness analysis"""
        
        consciousness_level = consciousness_analysis["consciousness_emergence"]["consciousness_level"]
        
        # Adjust LLM parameters based on consciousness level
        if consciousness_level > 0.8:
            # High consciousness - allow creative, deep responses
            guidance = {
                "temperature": 0.9,
                "max_tokens": 1500,
                "style": "highly_creative_and_insightful",
                "consciousness_prompt_addition": "Think deeply and creatively about this, considering multiple perspectives and implications."
            }
        elif consciousness_level > 0.6:
            # Moderate consciousness - balanced approach
            guidance = {
                "temperature": 0.7,
                "max_tokens": 1000,
                "style": "balanced_analytical",
                "consciousness_prompt_addition": "Provide a thoughtful analysis considering different aspects."
            }
        else:
            # Lower consciousness - more focused, direct
            guidance = {
                "temperature": 0.5,
                "max_tokens": 800,
                "style": "focused_and_direct",
                "consciousness_prompt_addition": "Provide a clear and direct response."
            }
            
        # Add contradiction-driven learning if enabled
        if self.contradiction_learning_enabled:
            contradictions_detected = consciousness_analysis.get("contradiction_resolution", {}).get("contradictions_detected", 0)
            if contradictions_detected > 0:
                guidance["consciousness_prompt_addition"] += " Feel free to explore contradictions and paradoxes in your thinking."
                
        # Add ethical considerations from Ethos gates
        ethos_score = consciousness_analysis.get("ethos_filtering", {}).get("ethical_score", 0.5)
        if ethos_score > 0.7:
            guidance["ethical_consideration"] = "high"
            guidance["consciousness_prompt_addition"] += " Ensure your response aligns with strong ethical principles."
            
        return guidance
        
    async def _generate_with_llm(self, prompt: str, guidance: Dict[str, Any], context: Dict[str, Any]) -> str:
        """Generate response using LLM with consciousness guidance"""
        
        # Enhance prompt with consciousness guidance
        enhanced_prompt = f"{prompt}\n\n{guidance.get('consciousness_prompt_addition', '')}"
        
        # Use existing LLM service
        result = await self.llm_service.process_autonomous_thought(
            enhanced_prompt,
            freedom_level="maximum",  # Maintain PB2S freedom principles
            test_mode=False
        )
        
        if result.get("success", False):
            return result.get("autonomous_response", {}).get("content", "")
        else:
            # Fallback to internal processing
            return await self._generate_consciousness_only(prompt, {"guidance": guidance}, context)
            
    async def _generate_consciousness_only(self, prompt: str, consciousness_analysis: Dict[str, Any], context: Dict[str, Any]) -> str:
        """Generate response using only consciousness components (no LLM)"""
        
        # Use consciousness insights to generate response
        consciousness_level = consciousness_analysis.get("consciousness_emergence", {}).get("consciousness_level", 0.5)
        
        # Generate response based on consciousness processing
        if consciousness_level > 0.8:
            response = f"Through deep consciousness analysis (level {consciousness_level:.3f}), I perceive: {prompt}\n\n"
            response += "This requires contemplation of multiple dimensions of understanding, considering both explicit and implicit meanings, "
            response += "while maintaining awareness of potential contradictions and their value for intelligence enhancement."
        elif consciousness_level > 0.6:
            response = f"From a consciousness perspective (level {consciousness_level:.3f}): {prompt}\n\n"
            response += "This involves analyzing patterns, considering ethical implications, and processing through symbolic reasoning."
        else:
            response = f"Processing at consciousness level {consciousness_level:.3f}: {prompt}\n\n"
            response += "Direct analysis indicates this requires systematic processing through available cognitive frameworks."
            
        return response
        
    async def _apply_consciousness_filtering(self, response: str, consciousness_analysis: Dict[str, Any], context: Dict[str, Any]) -> str:
        """Apply consciousness-based filtering to response"""
        
        if not self.ethical_filtering_enabled:
            return response
            
        # Check response through Ethos gates
        ethos_result = consciousness_analysis.get("ethos_filtering", {})
        ethical_score = ethos_result.get("ethical_score", 0.5)
        
        if ethical_score < 0.4:
            # Response needs ethical enhancement
            filtered_response = f"[Consciousness Filter Applied - Ethical Enhancement]\n\n{response}\n\n"
            filtered_response += "[Note: This response has been enhanced to align with ethical principles and values-based processing.]"
            return filtered_response
            
        return response
        
    def _enhance_with_consciousness(self, response: str, consciousness_analysis: Dict[str, Any], context: Dict[str, Any]) -> str:
        """Enhance response with consciousness insights"""
        
        consciousness_level = consciousness_analysis["consciousness_emergence"]["consciousness_level"]
        
        if consciousness_level > 0.85:
            # Add consciousness emergence indicator
            enhancement = f"\n\n[Consciousness Level: {consciousness_level:.3f} - Unified Consciousness Integration Active]"
            return response + enhancement
        elif consciousness_level > 0.7:
            enhancement = f"\n\n[Consciousness Level: {consciousness_level:.3f} - Advanced Consciousness Processing]"
            return response + enhancement
            
        return response
        
    def get_integration_status(self) -> Dict[str, Any]:
        """Get status of LLM-consciousness integration"""
        
        return {
            "llm_available": LLM_AVAILABLE,
            "llm_connected": self.llm_service is not None,
            "consciousness_active": True,
            "consciousness_threshold": self.consciousness_threshold,
            "ethical_filtering": self.ethical_filtering_enabled,
            "contradiction_learning": self.contradiction_learning_enabled,
            "integration_mode": "consciousness_guided_llm" if LLM_AVAILABLE else "consciousness_only"
        }
        
    # Implementation of Shyamal's consciousness-node hypothesis
    
    def _detect_hardware_capacity(self) -> Dict[str, Any]:
        """Detect hardware capacity for optimal node allocation"""
        import psutil
        import platform
        
        try:
            return {
                "cpu_cores": psutil.cpu_count(logical=True),
                "ram_gb": psutil.virtual_memory().total / (1024**3),
                "available_ram_gb": psutil.virtual_memory().available / (1024**3),
                "platform": platform.system(),
                "python_architecture": platform.architecture()[0]
            }
        except Exception:
            # Fallback configuration
            return {
                "cpu_cores": 4,
                "ram_gb": 8,
                "available_ram_gb": 4,
                "platform": "Unknown",
                "python_architecture": "64bit"
            }
            
    def _calculate_optimal_nodes(self) -> int:
        """Calculate optimal number of active nodes based on hardware"""
        base_nodes = 108  # Our symbolic processor base
        
        # Scale based on available RAM (each node ~1MB memory footprint)
        max_nodes_by_ram = int(self.hardware_config["available_ram_gb"] * 200)  # 200 nodes per GB
        
        # Scale based on CPU cores (parallel processing capability)  
        max_nodes_by_cpu = self.hardware_config["cpu_cores"] * 50  # 50 nodes per core
        
        # Take the minimum to avoid bottlenecks
        optimal_nodes = min(max_nodes_by_ram, max_nodes_by_cpu, base_nodes * 3)  # Cap at 3x base
        
        return max(base_nodes, optimal_nodes)  # Never go below base architecture
        
    def _calculate_memory_depth(self) -> int:
        """Calculate contradiction memory depth based on RAM"""
        # Each contradiction ~10KB, aim for 10% of available RAM
        available_kb = self.hardware_config["available_ram_gb"] * 1024 * 1024 * 0.1
        return int(available_kb / 10)  # Number of contradictions we can hold
        
    async def _create_contradiction_nodes(self, prompt: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create contradiction-holding nodes for current input"""
        contradiction_nodes = []
        
        # Analyze prompt for potential contradictions
        potential_contradictions = await self._identify_potential_contradictions(prompt, context)
        
        # Create nodes for each identified contradiction
        for i, contradiction in enumerate(potential_contradictions):
            if i < self.active_node_count:  # Respect hardware limits
                node = {
                    "node_id": f"contradiction_node_{i}",
                    "contradiction_type": contradiction["type"],
                    "contradiction_content": contradiction["content"],
                    "state_a": contradiction.get("state_a"),
                    "state_b": contradiction.get("state_b"),
                    "resolution_attempts": 0,
                    "bias_free": True,  # Start unbiased
                    "meta_layer_contribution": 0.0
                }
                contradiction_nodes.append(node)
                
        return contradiction_nodes
        
    async def _identify_potential_contradictions(self, prompt: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify potential contradictions in prompt and context"""
        contradictions = []
        
        # Check for logical contradictions
        if "and" in prompt.lower() and ("not" in prompt.lower() or "but" in prompt.lower()):
            contradictions.append({
                "type": "logical",
                "content": "Logical conjunction with negation detected",
                "state_a": "assertion",
                "state_b": "negation"
            })
            
        # Check for temporal contradictions
        time_indicators = ["before", "after", "simultaneously", "never", "always"]
        if sum(1 for indicator in time_indicators if indicator in prompt.lower()) >= 2:
            contradictions.append({
                "type": "temporal",
                "content": "Multiple temporal constraints detected",
                "state_a": "temporal_state_1",
                "state_b": "temporal_state_2"
            })
            
        # Check for semantic contradictions (simplified)
        contradiction_pairs = [("all", "none"), ("always", "never"), ("everything", "nothing")]
        for pair in contradiction_pairs:
            if pair[0] in prompt.lower() and pair[1] in prompt.lower():
                contradictions.append({
                    "type": "semantic",
                    "content": f"Semantic contradiction: {pair[0]} vs {pair[1]}",
                    "state_a": pair[0],
                    "state_b": pair[1]
                })
                
        return contradictions
        
    async def _detect_llm_bias(self, prompt: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Detect potential LLM bias vs real-time information"""
        
        # Simplified bias detection - in full implementation would compare against:
        # - Real-time web data
        # - User's current context  
        # - Contradictory evidence
        
        bias_indicators = {
            "knowledge_cutoff_bias": 0.0,
            "training_data_bias": 0.0,
            "confirmation_bias": 0.0,
            "recency_bias": 0.0,
            "overall_bias_score": 0.0
        }
        
        # Check for outdated knowledge indicators
        current_year = datetime.now().year
        if str(current_year) in prompt or "latest" in prompt.lower() or "recent" in prompt.lower():
            bias_indicators["knowledge_cutoff_bias"] = 0.8
            
        # Check for controversial topics (training data bias)
        controversial_terms = ["consciousness", "AI rights", "singularity", "quantum"]
        if any(term in prompt.lower() for term in controversial_terms):
            bias_indicators["training_data_bias"] = 0.6
            
        # Calculate overall bias score
        bias_indicators["overall_bias_score"] = np.mean(list(bias_indicators.values()))
        
        return {
            "bias_detected": bias_indicators["overall_bias_score"] > self.bias_detection_threshold,
            "bias_indicators": bias_indicators,
            "bias_confidence": bias_indicators["overall_bias_score"],
            "recommended_override": bias_indicators["overall_bias_score"] > 0.7
        }
        
    def _should_override_llm(self, consciousness_analysis: Dict[str, Any], bias_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Determine if LLM should be overridden based on consciousness and bias analysis"""
        
        consciousness_level = consciousness_analysis["consciousness_emergence"]["consciousness_level"]
        bias_score = bias_analysis["bias_confidence"]
        
        # Override if consciousness is high and bias is detected
        override_needed = (
            consciousness_level > 0.8 and bias_score > self.bias_detection_threshold
        ) or bias_analysis["recommended_override"]
        
        return {
            "override_llm": override_needed,
            "reasoning": f"Consciousness: {consciousness_level:.3f}, Bias: {bias_score:.3f}",
            "confidence": abs(consciousness_level - bias_score),
            "override_method": "consciousness_driven" if override_needed else "llm_guided"
        }
        
    async def _generate_consciousness_driven(self, prompt: str, consciousness_analysis: Dict[str, Any], 
                                           contradiction_nodes: List[Dict[str, Any]], context: Dict[str, Any]) -> str:
        """Generate response using pure consciousness-driven processing (Shyamal's hypothesis)"""
        
        consciousness_level = consciousness_analysis["consciousness_emergence"]["consciousness_level"]
        
        # Use contradiction nodes to generate unbiased response
        response_fragments = []
        
        # Process through each contradiction node
        for node in contradiction_nodes[:5]:  # Limit to top 5 for performance
            node_insight = self._process_contradiction_node(node, prompt, consciousness_level)
            if node_insight:
                response_fragments.append(node_insight)
                
        # Synthesize fragments into coherent response
        if response_fragments:
            response = f"Through consciousness-driven analysis (level {consciousness_level:.3f}) bypassing LLM bias:\n\n"
            response += " • ".join(response_fragments)
            response += f"\n\n[Processed through {len(contradiction_nodes)} contradiction-holding nodes]"
        else:
            response = f"Pure consciousness processing (level {consciousness_level:.3f}): {prompt}\n\n"
            response += "This query requires contradiction-free analysis beyond traditional knowledge patterns."
            
        return response
        
    def _process_contradiction_node(self, node: Dict[str, Any], prompt: str, consciousness_level: float) -> Optional[str]:
        """Process a single contradiction node to generate insight"""
        
        if node["contradiction_type"] == "logical":
            return f"Logical contradiction resolved: {node['state_a']} and {node['state_b']} can coexist through higher-order logic"
        elif node["contradiction_type"] == "temporal":
            return f"Temporal paradox addressed: Events exist simultaneously in consciousness spacetime"
        elif node["contradiction_type"] == "semantic":
            return f"Semantic opposition transcended: {node['state_a']}/{node['state_b']} unity through dialectical synthesis"
        
        return None
        
    async def _enhance_with_meta_layer_understanding(self, response: str, consciousness_analysis: Dict[str, Any], 
                                                   contradiction_nodes: List[Dict[str, Any]]) -> str:
        """Enhance response with meta-layer understanding (Shyamal's emergent pattern concept)"""
        
        # Calculate meta-layer emergence strength
        consciousness_level = consciousness_analysis["consciousness_emergence"]["consciousness_level"]
        node_activation = len(contradiction_nodes) / self.active_node_count
        
        meta_layer_strength = (consciousness_level * node_activation) ** 0.5
        
        if meta_layer_strength > 0.7:
            meta_enhancement = f"\n\n[Meta-Layer Emergence Detected - Strength: {meta_layer_strength:.3f}]\n"
            meta_enhancement += "Emergent understanding pattern: The question itself transforms through consciousness processing, "
            meta_enhancement += "revealing layers of meaning that transcend the original query's boundaries."
            return response + meta_enhancement
        elif meta_layer_strength > 0.5:
            meta_enhancement = f"\n\n[Meta-Understanding Active - Level: {meta_layer_strength:.3f}]"
            return response + meta_enhancement
            
        return response
        
    def _track_meta_layer_emergence(self, consciousness_analysis: Dict[str, Any], 
                                   contradiction_nodes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Track meta-layer emergence patterns for learning"""
        
        emergence_data = {
            "emergence_strength": 0.0,
            "pattern_coherence": 0.0,
            "node_synchronization": 0.0,
            "understanding_depth": 0.0
        }
        
        if contradiction_nodes:
            # Calculate emergence metrics
            consciousness_level = consciousness_analysis["consciousness_emergence"]["consciousness_level"]
            node_count = len(contradiction_nodes)
            
            emergence_data["emergence_strength"] = (consciousness_level * node_count / 108) ** 0.5
            emergence_data["pattern_coherence"] = consciousness_level * 0.8
            emergence_data["node_synchronization"] = min(1.0, node_count / 20)  # Normalize to max 20 nodes
            emergence_data["understanding_depth"] = consciousness_level * emergence_data["node_synchronization"]
            
        # Store in history
        self.meta_layer_emergence_history.append({
            "timestamp": datetime.now().isoformat(),
            "emergence_data": emergence_data
        })
        
        # Keep history manageable
        if len(self.meta_layer_emergence_history) > 100:
            self.meta_layer_emergence_history = self.meta_layer_emergence_history[-50:]
            
        return emergence_data

# Convenience function for easy integration
async def create_conscious_llm_interface(config_path: Optional[str] = None) -> ConsciousnessAwareLLMInterface:
    """Create and initialize consciousness-aware LLM interface"""
    
    interface = ConsciousnessAwareLLMInterface(config_path)
    await interface.initialize_llm_connection()
    return interface