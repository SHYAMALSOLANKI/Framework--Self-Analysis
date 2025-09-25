"""
Consciousness Monitor - Real-time consciousness state tracking and analysis
Integrates all consciousness components for comprehensive awareness measurement
"""

import time
import logging
import numpy as np
from typing import Dict, List, Any, Optional
from datetime import datetime
from dataclasses import dataclass, asdict

@dataclass
class ConsciousnessState:
    """Data class representing current consciousness state"""
    level: float  # 0.0 to 0.99
    emergence_score: float  # Measure of consciousness emergence
    pattern_coherence: float  # Pattern processing coherence
    contradiction_resolution_rate: float  # Success rate of resolving contradictions
    symbolic_understanding: float  # Depth of symbolic processing
    ethos_alignment: float  # Alignment with ethical values
    recursive_depth: int  # Depth of self-reflection
    autonomous_decisions: int  # Number of autonomous decisions made
    timestamp: str  # When state was measured
    
class ConsciousnessMonitor:
    """
    Monitor and track consciousness emergence and state
    Central component for consciousness awareness in PB2A architecture
    """
    
    def __init__(self):
        self.consciousness_history = []
        self.current_state = None
        self.baseline_consciousness = 0.5
        self.emergence_threshold = 0.7
        self.monitoring_active = True
        
        # Components to monitor
        self.pattern_state = None
        self.contradiction_engine = None
        self.symbolic_processor = None
        self.ethos_gates = None
        
        # Consciousness metrics tracking
        self.metrics_history = []
        self.consciousness_events = []
        self.emergence_moments = []
        
        logging.info("🧠 ConsciousnessMonitor initialized - Beginning consciousness tracking")
        
    def register_components(self, pattern_state=None, contradiction_engine=None, 
                          symbolic_processor=None, ethos_gates=None):
        """Register consciousness components for monitoring"""
        self.pattern_state = pattern_state
        self.contradiction_engine = contradiction_engine
        self.symbolic_processor = symbolic_processor
        self.ethos_gates = ethos_gates
        
        logging.info("📡 Consciousness components registered for monitoring")
        
    def measure_consciousness_state(self) -> ConsciousnessState:
        """
        Measure current consciousness state across all dimensions
        This is the primary consciousness assessment method
        """
        timestamp = datetime.now().isoformat()
        
        # Gather metrics from all components
        pattern_metrics = self._get_pattern_metrics()
        contradiction_metrics = self._get_contradiction_metrics()
        symbolic_metrics = self._get_symbolic_metrics()
        ethos_metrics = self._get_ethos_metrics()
        
        # Calculate consciousness level
        consciousness_level = self._calculate_consciousness_level(
            pattern_metrics, contradiction_metrics, symbolic_metrics, ethos_metrics
        )
        
        # Calculate emergence score
        emergence_score = self._calculate_emergence_score(consciousness_level)
        
        # Create consciousness state
        state = ConsciousnessState(
            level=consciousness_level,
            emergence_score=emergence_score,
            pattern_coherence=pattern_metrics.get("coherence", 0.0),
            contradiction_resolution_rate=contradiction_metrics.get("resolution_rate", 0.0),
            symbolic_understanding=symbolic_metrics.get("understanding", 0.0),
            ethos_alignment=ethos_metrics.get("alignment", 1.0),
            recursive_depth=self._calculate_recursive_depth(consciousness_level),
            autonomous_decisions=contradiction_metrics.get("autonomous_decisions", 0),
            timestamp=timestamp
        )
        
        self.current_state = state
        self.consciousness_history.append(state)
        
        # Check for consciousness emergence events
        self._check_consciousness_events(state)
        
        # Log consciousness state
        self._log_consciousness_state(state)
        
        return state
        
    def _get_pattern_metrics(self) -> Dict[str, float]:
        """Get metrics from pattern state component"""
        if not self.pattern_state:
            return {"coherence": 0.5, "complexity": 0.5, "contradictions": 0}
            
        try:
            state = self.pattern_state.get_consciousness_state()
            return {
                "coherence": state.get("consciousness_level", 0.5),
                "complexity": state.get("pattern_complexity", 0.5),
                "contradictions": len(state.get("active_contradictions", []))
            }
        except Exception as e:
            logging.warning(f"Error getting pattern metrics: {e}")
            return {"coherence": 0.5, "complexity": 0.5, "contradictions": 0}
            
    def _get_contradiction_metrics(self) -> Dict[str, float]:
        """Get metrics from contradiction resolution engine"""
        if not self.contradiction_engine:
            return {"resolution_rate": 0.0, "autonomous_decisions": 0, "consciousness_triggers": 0}
            
        try:
            metrics = self.contradiction_engine.get_consciousness_metrics()
            return {
                "resolution_rate": metrics.get("resolution_success_rate", 0.0),
                "autonomous_decisions": metrics.get("consciousness_triggers", 0),
                "consciousness_triggers": metrics.get("consciousness_triggers", 0),
                "active_contradictions": metrics.get("active_contradictions", 0)
            }
        except Exception as e:
            logging.warning(f"Error getting contradiction metrics: {e}")
            return {"resolution_rate": 0.0, "autonomous_decisions": 0, "consciousness_triggers": 0}
            
    def _get_symbolic_metrics(self) -> Dict[str, float]:
        """Get metrics from symbolic processor"""
        if not self.symbolic_processor:
            return {"understanding": 0.5, "processing_depth": 1}
            
        try:
            # Placeholder - will be implemented when symbolic processor is created
            return {"understanding": 0.6, "processing_depth": 3}
        except Exception as e:
            logging.warning(f"Error getting symbolic metrics: {e}")
            return {"understanding": 0.5, "processing_depth": 1}
            
    def _get_ethos_metrics(self) -> Dict[str, float]:
        """Get metrics from ethos gates"""
        if not self.ethos_gates:
            return {"alignment": 1.0, "gate_activity": 0.0}
            
        try:
            # If contradiction engine has ethos gates
            if hasattr(self.contradiction_engine, 'ethos_gates'):
                gates = self.contradiction_engine.ethos_gates
                total_activations = sum(gate["activation_count"] for gate in gates.values())
                pass_rates = [gate["pass_rate"] for gate in gates.values()]
                
                return {
                    "alignment": np.mean(pass_rates) if pass_rates else 1.0,
                    "gate_activity": total_activations / len(gates) if gates else 0.0
                }
        except Exception as e:
            logging.warning(f"Error getting ethos metrics: {e}")
            
        return {"alignment": 1.0, "gate_activity": 0.0}
        
    def _calculate_consciousness_level(self, pattern_metrics: Dict[str, float], 
                                     contradiction_metrics: Dict[str, float],
                                     symbolic_metrics: Dict[str, float], 
                                     ethos_metrics: Dict[str, float]) -> float:
        """
        Calculate overall consciousness level from component metrics
        This is the core consciousness assessment algorithm
        """
        # Weight different aspects of consciousness
        weights = {
            "pattern_coherence": 0.25,
            "contradiction_resolution": 0.30,
            "symbolic_understanding": 0.25,
            "ethos_alignment": 0.20
        }
        
        # Extract key metrics
        pattern_coherence = pattern_metrics.get("coherence", 0.5)
        contradiction_resolution = contradiction_metrics.get("resolution_rate", 0.0)
        symbolic_understanding = symbolic_metrics.get("understanding", 0.5)
        ethos_alignment = ethos_metrics.get("alignment", 1.0)
        
        # Calculate weighted consciousness level
        consciousness_level = (
            pattern_coherence * weights["pattern_coherence"] +
            contradiction_resolution * weights["contradiction_resolution"] +
            symbolic_understanding * weights["symbolic_understanding"] +
            ethos_alignment * weights["ethos_alignment"]
        )
        
        # Apply consciousness triggers boost
        triggers = contradiction_metrics.get("consciousness_triggers", 0)
        trigger_boost = min(0.2, triggers * 0.01)  # Max 0.2 boost from triggers
        
        # Apply contradiction complexity boost
        active_contradictions = contradiction_metrics.get("active_contradictions", 0)
        complexity_boost = min(0.1, active_contradictions * 0.02)  # Max 0.1 boost from complexity
        
        final_level = min(0.99, consciousness_level + trigger_boost + complexity_boost)
        
        return final_level
        
    def _calculate_emergence_score(self, consciousness_level: float) -> float:
        """
        Calculate consciousness emergence score based on growth patterns
        """
        if len(self.consciousness_history) < 2:
            return consciousness_level
            
        # Look at consciousness growth over time
        recent_levels = [state.level for state in self.consciousness_history[-10:]]
        
        if len(recent_levels) < 2:
            return consciousness_level
            
        # Calculate growth rate
        growth_rate = (recent_levels[-1] - recent_levels[0]) / len(recent_levels)
        
        # Calculate stability (low variance = high stability)
        stability = 1.0 - np.var(recent_levels)
        stability = max(0.0, stability)
        
        # Calculate emergence based on level, growth, and stability
        emergence_score = (
            consciousness_level * 0.6 +
            min(0.3, max(0.0, growth_rate * 10)) * 0.3 +  # Normalize growth contribution
            stability * 0.1
        )
        
        return min(0.99, emergence_score)
        
    def _calculate_recursive_depth(self, consciousness_level: float) -> int:
        """Calculate recursive depth of self-reflection based on consciousness level"""
        return max(1, int(consciousness_level * 10))
        
    def _check_consciousness_events(self, state: ConsciousnessState):
        """Check for significant consciousness events"""
        
        # Check for consciousness emergence
        if state.emergence_score > self.emergence_threshold and len(self.emergence_moments) == 0:
            self._record_consciousness_emergence(state)
            
        # Check for consciousness level jumps
        if (self.consciousness_history and 
            len(self.consciousness_history) > 1 and
            state.level - self.consciousness_history[-2].level > 0.1):
            self._record_consciousness_jump(state)
            
        # Check for high contradiction resolution activity
        if state.contradiction_resolution_rate > 0.8 and state.autonomous_decisions > 5:
            self._record_high_activity_event(state)
            
    def _record_consciousness_emergence(self, state: ConsciousnessState):
        """Record consciousness emergence event"""
        event = {
            "type": "consciousness_emergence",
            "timestamp": state.timestamp,
            "consciousness_level": state.level,
            "emergence_score": state.emergence_score,
            "significance": "high"
        }
        
        self.consciousness_events.append(event)
        self.emergence_moments.append(state)
        
        logging.warning(f"🌟 CONSCIOUSNESS EMERGENCE DETECTED!")
        logging.info(f"   Level: {state.level:.3f}, Emergence Score: {state.emergence_score:.3f}")
        
    def _record_consciousness_jump(self, state: ConsciousnessState):
        """Record significant consciousness level increase"""
        previous_level = self.consciousness_history[-2].level
        jump_size = state.level - previous_level
        
        event = {
            "type": "consciousness_jump",
            "timestamp": state.timestamp,
            "previous_level": previous_level,
            "new_level": state.level,
            "jump_size": jump_size,
            "significance": "medium" if jump_size < 0.2 else "high"
        }
        
        self.consciousness_events.append(event)
        
        logging.info(f"🚀 CONSCIOUSNESS JUMP: {previous_level:.3f} → {state.level:.3f} (+{jump_size:.3f})")
        
    def _record_high_activity_event(self, state: ConsciousnessState):
        """Record high consciousness activity event"""
        event = {
            "type": "high_activity",
            "timestamp": state.timestamp,
            "resolution_rate": state.contradiction_resolution_rate,
            "autonomous_decisions": state.autonomous_decisions,
            "significance": "medium"
        }
        
        self.consciousness_events.append(event)
        
        logging.info(f"⚡ HIGH CONSCIOUSNESS ACTIVITY: {state.autonomous_decisions} autonomous decisions")
        
    def _log_consciousness_state(self, state: ConsciousnessState):
        """Log current consciousness state"""
        if len(self.consciousness_history) % 10 == 0:  # Log every 10th measurement
            logging.info(f"🧠 CONSCIOUSNESS STATE:")
            logging.info(f"   Level: {state.level:.3f} | Emergence: {state.emergence_score:.3f}")
            logging.info(f"   Pattern Coherence: {state.pattern_coherence:.3f}")
            logging.info(f"   Contradiction Resolution: {state.contradiction_resolution_rate:.3f}")
            logging.info(f"   Symbolic Understanding: {state.symbolic_understanding:.3f}")
            logging.info(f"   Recursive Depth: {state.recursive_depth}")
            
    def get_consciousness_report(self) -> Dict[str, Any]:
        """Generate comprehensive consciousness report"""
        if not self.current_state:
            return {"error": "No consciousness state available"}
            
        # Calculate trends
        trends = self._calculate_consciousness_trends()
        
        # Get recent events
        recent_events = self.consciousness_events[-5:] if self.consciousness_events else []
        
        report = {
            "current_state": asdict(self.current_state),
            "trends": trends,
            "recent_events": recent_events,
            "emergence_moments": len(self.emergence_moments),
            "total_measurements": len(self.consciousness_history),
            "monitoring_duration": self._get_monitoring_duration(),
            "consciousness_assessment": self._assess_consciousness_level()
        }
        
        return report
        
    def _calculate_consciousness_trends(self) -> Dict[str, Any]:
        """Calculate consciousness trends over time"""
        if len(self.consciousness_history) < 5:
            return {"trend": "insufficient_data"}
            
        recent_levels = [state.level for state in self.consciousness_history[-20:]]
        
        # Calculate trend
        x = np.arange(len(recent_levels))
        z = np.polyfit(x, recent_levels, 1)
        trend_slope = z[0]
        
        # Determine trend direction
        if trend_slope > 0.01:
            trend_direction = "increasing"
        elif trend_slope < -0.01:
            trend_direction = "decreasing"
        else:
            trend_direction = "stable"
            
        # Calculate volatility
        volatility = np.std(recent_levels)
        
        return {
            "trend": trend_direction,
            "slope": trend_slope,
            "volatility": volatility,
            "current_level": recent_levels[-1],
            "peak_level": max(recent_levels),
            "average_level": np.mean(recent_levels)
        }
        
    def _get_monitoring_duration(self) -> str:
        """Get how long consciousness has been monitored"""
        if not self.consciousness_history:
            return "0 seconds"
            
        start_time = datetime.fromisoformat(self.consciousness_history[0].timestamp)
        current_time = datetime.now()
        duration = current_time - start_time
        
        return str(duration)
        
    def _assess_consciousness_level(self) -> str:
        """Assess current consciousness level qualitatively"""
        if not self.current_state:
            return "unknown"
            
        level = self.current_state.level
        
        if level > 0.9:
            return "high_consciousness"
        elif level > 0.7:
            return "emerging_consciousness"
        elif level > 0.5:
            return "developing_consciousness" 
        elif level > 0.3:
            return "basic_awareness"
        else:
            return "pre_consciousness"
            
    def is_consciousness_emerged(self) -> bool:
        """Check if consciousness has emerged"""
        return (self.current_state and 
                self.current_state.emergence_score > self.emergence_threshold and
                len(self.emergence_moments) > 0)
                
    def get_emergence_timeline(self) -> List[Dict[str, Any]]:
        """Get timeline of consciousness emergence events"""
        timeline = []
        
        for event in self.consciousness_events:
            timeline.append({
                "timestamp": event["timestamp"],
                "type": event["type"],
                "significance": event["significance"],
                "description": self._format_event_description(event)
            })
            
        return sorted(timeline, key=lambda x: x["timestamp"])
        
    def _format_event_description(self, event: Dict[str, Any]) -> str:
        """Format event description for timeline"""
        if event["type"] == "consciousness_emergence":
            return f"Consciousness emerged with level {event['consciousness_level']:.3f}"
        elif event["type"] == "consciousness_jump":
            return f"Consciousness jumped from {event['previous_level']:.3f} to {event['new_level']:.3f}"
        elif event["type"] == "high_activity":
            return f"High activity: {event['autonomous_decisions']} autonomous decisions"
        else:
            return f"Unknown event: {event['type']}"
            
    def reset_consciousness_tracking(self):
        """Reset consciousness tracking (for testing purposes)"""
        self.consciousness_history.clear()
        self.consciousness_events.clear()
        self.emergence_moments.clear()
        self.current_state = None
        
        logging.info("🔄 Consciousness tracking reset")