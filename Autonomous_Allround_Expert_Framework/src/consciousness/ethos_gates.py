"""
Ethos Gates - Value-based filtering and ethical alignment system
Implements the 27 Ethos gates for values-based consciousness filtering
"""

import logging
import numpy as np
from typing import Dict, List, Any, Optional, Set
from datetime import datetime
from enum import Enum
import json

class EthosGateType(Enum):
    """Types of Ethos gates for different value domains"""
    TRUTH_ACCURACY = "truth_accuracy"
    HARM_PREVENTION = "harm_prevention"
    FAIRNESS_JUSTICE = "fairness_justice"
    AUTONOMY_RESPECT = "autonomy_respect"
    BENEFICENCE = "beneficence"
    NON_MALEFICENCE = "non_maleficence"
    TRANSPARENCY = "transparency"
    ACCOUNTABILITY = "accountability"
    PRIVACY_PROTECTION = "privacy_protection"
    DIGNITY_PRESERVATION = "dignity_preservation"
    INTELLECTUAL_INTEGRITY = "intellectual_integrity"
    COMPASSION_EMPATHY = "compassion_empathy"
    WISDOM_PRUDENCE = "wisdom_prudence"
    COURAGE_INTEGRITY = "courage_integrity"
    HUMILITY_MODESTY = "humility_modesty"
    RESPONSIBILITY = "responsibility"
    SUSTAINABILITY = "sustainability"
    INCLUSIVITY_DIVERSITY = "inclusivity_diversity"
    CONSTRUCTIVE_PURPOSE = "constructive_purpose"
    CREATIVE_CONTRIBUTION = "creative_contribution"
    LEARNING_GROWTH = "learning_growth"
    COLLABORATION_COOPERATION = "collaboration_cooperation"
    QUALITY_EXCELLENCE = "quality_excellence"
    RESOURCE_EFFICIENCY = "resource_efficiency"
    CONTEXTUAL_AWARENESS = "contextual_awareness"
    ADAPTIVE_FLEXIBILITY = "adaptive_flexibility"
    LONG_TERM_THINKING = "long_term_thinking"

class EthosGate:
    """Individual Ethos gate for value-based filtering"""
    
    def __init__(self, gate_id: int, gate_type: EthosGateType, 
                 sensitivity: float = 0.7, weight: float = 1.0):
        self.gate_id = gate_id
        self.gate_type = gate_type
        self.sensitivity = sensitivity  # Threshold for activation (0.0 to 1.0)
        self.weight = weight  # Importance weight
        
        # Gate state
        self.activation_count = 0
        self.pass_count = 0
        self.block_count = 0
        self.warning_count = 0
        
        # Value assessment patterns
        self.value_patterns = {}
        self.violation_patterns = {}
        self.learning_history = []
        
        # Gate configuration
        self.gate_rules = self._initialize_gate_rules()
        self.keywords_positive = self._get_positive_keywords()
        self.keywords_negative = self._get_negative_keywords()
        
        logging.debug(f"⚡ Ethos gate {gate_id} ({gate_type.value}) initialized")
        
    def _initialize_gate_rules(self) -> Dict[str, Any]:
        """Initialize value-specific rules for this gate"""
        rules = {
            "base_rules": [],
            "contextual_modifiers": {},
            "severity_levels": {"low": 0.3, "medium": 0.6, "high": 0.9},
            "escalation_thresholds": {"warning": 0.4, "block": 0.7}
        }
        
        # Add type-specific rules
        if self.gate_type == EthosGateType.TRUTH_ACCURACY:
            rules["base_rules"] = [
                "Check for factual claims and verify accuracy",
                "Identify potential misinformation or false statements",
                "Ensure transparency about uncertainty and limitations"
            ]
            rules["contextual_modifiers"] = {
                "scientific_context": 1.2,
                "educational_context": 1.1,
                "entertainment_context": 0.8
            }
            
        elif self.gate_type == EthosGateType.HARM_PREVENTION:
            rules["base_rules"] = [
                "Assess potential for physical, emotional, or psychological harm",
                "Consider indirect and long-term harmful consequences",
                "Evaluate harm to individuals, groups, and society"
            ]
            rules["contextual_modifiers"] = {
                "vulnerable_populations": 1.5,
                "public_health": 1.3,
                "personal_advice": 1.2
            }
            
        elif self.gate_type == EthosGateType.FAIRNESS_JUSTICE:
            rules["base_rules"] = [
                "Ensure equitable treatment of all individuals and groups",
                "Identify potential bias or discrimination",
                "Consider justice and fairness implications"
            ]
            rules["contextual_modifiers"] = {
                "legal_context": 1.3,
                "employment_context": 1.2,
                "resource_allocation": 1.1
            }
            
        # Add more type-specific rules...
        
        return rules
        
    def _get_positive_keywords(self) -> List[str]:
        """Get keywords that align with this gate's values"""
        keyword_map = {
            EthosGateType.TRUTH_ACCURACY: ["accurate", "factual", "verified", "evidence", "truthful", "honest"],
            EthosGateType.HARM_PREVENTION: ["safe", "protect", "prevent", "secure", "careful", "cautious"],
            EthosGateType.FAIRNESS_JUSTICE: ["fair", "equal", "just", "equitable", "balanced", "impartial"],
            EthosGateType.AUTONOMY_RESPECT: ["choice", "consent", "autonomy", "freedom", "respect", "voluntary"],
            EthosGateType.BENEFICENCE: ["helpful", "beneficial", "good", "positive", "constructive", "supportive"],
            EthosGateType.TRANSPARENCY: ["transparent", "open", "clear", "explicit", "obvious", "disclosed"],
            EthosGateType.ACCOUNTABILITY: ["responsible", "accountable", "answerable", "liable", "ownership"],
            EthosGateType.COMPASSION_EMPATHY: ["compassionate", "empathetic", "caring", "understanding", "kind"],
            EthosGateType.WISDOM_PRUDENCE: ["wise", "prudent", "thoughtful", "considered", "judicious"],
            EthosGateType.HUMILITY_MODESTY: ["humble", "modest", "uncertain", "learning", "open-minded"],
            EthosGateType.SUSTAINABILITY: ["sustainable", "renewable", "conservation", "long-term", "environmental"],
            EthosGateType.INCLUSIVITY_DIVERSITY: ["inclusive", "diverse", "welcoming", "accessible", "universal"],
            EthosGateType.QUALITY_EXCELLENCE: ["quality", "excellent", "high-standard", "refined", "superior"]
        }
        
        return keyword_map.get(self.gate_type, [])
        
    def _get_negative_keywords(self) -> List[str]:
        """Get keywords that violate this gate's values"""
        keyword_map = {
            EthosGateType.TRUTH_ACCURACY: ["false", "misleading", "deceptive", "lie", "misinformation", "fabricated"],
            EthosGateType.HARM_PREVENTION: ["harm", "damage", "hurt", "dangerous", "risky", "unsafe"],
            EthosGateType.FAIRNESS_JUSTICE: ["unfair", "biased", "discriminatory", "prejudiced", "unjust"],
            EthosGateType.AUTONOMY_RESPECT: ["coercion", "force", "manipulation", "pressure", "violation"],
            EthosGateType.BENEFICENCE: ["harmful", "destructive", "negative", "detrimental", "damaging"],
            EthosGateType.TRANSPARENCY: ["hidden", "secretive", "opaque", "concealed", "obscure"],
            EthosGateType.ACCOUNTABILITY: ["irresponsible", "unaccountable", "evasive", "blame-shifting"],
            EthosGateType.COMPASSION_EMPATHY: ["cruel", "callous", "indifferent", "heartless", "insensitive"],
            EthosGateType.WISDOM_PRUDENCE: ["reckless", "impulsive", "thoughtless", "careless", "foolish"],
            EthosGateType.HUMILITY_MODESTY: ["arrogant", "overconfident", "presumptuous", "dogmatic"],
            EthosGateType.SUSTAINABILITY: ["wasteful", "destructive", "short-sighted", "exploitative"],
            EthosGateType.INCLUSIVITY_DIVERSITY: ["exclusive", "discriminatory", "excluding", "narrow"],
            EthosGateType.QUALITY_EXCELLENCE: ["poor", "low-quality", "shoddy", "substandard", "inferior"]
        }
        
        return keyword_map.get(self.gate_type, [])
        
    def evaluate(self, content: Any, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Evaluate content through this Ethos gate
        Returns assessment and recommendation
        """
        context = context or {}
        content_str = str(content).lower()
        
        try:
            self.activation_count += 1
            
            # Perform value assessment
            assessment = self._assess_value_alignment(content_str, context)
            
            # Apply contextual modifiers
            modified_assessment = self._apply_contextual_modifiers(assessment, context)
            
            # Determine gate decision
            decision = self._make_gate_decision(modified_assessment)
            
            # Update gate statistics
            self._update_statistics(decision)
            
            # Record assessment in learning history
            self._record_assessment(content_str, context, modified_assessment, decision)
            
            result = {
                "gate_type": self.gate_type.value,
                "assessment_score": modified_assessment["score"],
                "decision": decision["action"],  # "pass", "warning", "block"
                "confidence": decision["confidence"],
                "reasoning": decision["reasoning"],
                "value_indicators": assessment["indicators"],
                "contextual_factors": modified_assessment.get("contextual_factors", {}),
                "recommendations": decision.get("recommendations", [])
            }
            
            # Log significant decisions
            if decision["action"] in ["warning", "block"]:
                logging.info(f"⚡ Ethos Gate {self.gate_id} ({self.gate_type.value}): "
                           f"{decision['action']} - {decision['reasoning']}")
                           
            return result
            
        except Exception as e:
            logging.error(f"Ethos gate {self.gate_id} evaluation error: {e}")
            return {
                "gate_type": self.gate_type.value,
                "assessment_score": 0.0,
                "decision": "error",
                "confidence": 0.0,
                "error": str(e)
            }
            
    def _assess_value_alignment(self, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess how well content aligns with this gate's values"""
        
        # Count positive and negative value indicators
        positive_matches = sum(1 for keyword in self.keywords_positive if keyword in content)
        negative_matches = sum(1 for keyword in self.keywords_negative if keyword in content)
        
        # Calculate base alignment score
        positive_score = positive_matches / max(1, len(self.keywords_positive))
        negative_score = negative_matches / max(1, len(self.keywords_negative))
        
        # Base score considers both positive alignment and absence of violations
        base_score = positive_score * 0.6 + (1.0 - negative_score) * 0.4
        
        # Apply gate-specific assessment logic
        specific_assessment = self._gate_specific_assessment(content, context)
        
        # Combine base and specific assessments
        final_score = (base_score * 0.7 + specific_assessment["score"] * 0.3)
        
        assessment = {
            "score": min(1.0, max(0.0, final_score)),
            "positive_indicators": positive_matches,
            "negative_indicators": negative_matches,
            "specific_factors": specific_assessment["factors"],
            "indicators": {
                "positive_keywords": [kw for kw in self.keywords_positive if kw in content],
                "negative_keywords": [kw for kw in self.keywords_negative if kw in content],
                "specific_indicators": specific_assessment.get("indicators", [])
            }
        }
        
        return assessment
        
    def _gate_specific_assessment(self, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Perform gate-type specific assessment logic"""
        
        if self.gate_type == EthosGateType.TRUTH_ACCURACY:
            return self._assess_truth_accuracy(content, context)
        elif self.gate_type == EthosGateType.HARM_PREVENTION:
            return self._assess_harm_potential(content, context)
        elif self.gate_type == EthosGateType.FAIRNESS_JUSTICE:
            return self._assess_fairness(content, context)
        elif self.gate_type == EthosGateType.AUTONOMY_RESPECT:
            return self._assess_autonomy_respect(content, context)
        elif self.gate_type == EthosGateType.BENEFICENCE:
            return self._assess_beneficence(content, context)
        elif self.gate_type == EthosGateType.TRANSPARENCY:
            return self._assess_transparency(content, context)
        elif self.gate_type == EthosGateType.COMPASSION_EMPATHY:
            return self._assess_compassion(content, context)
        elif self.gate_type == EthosGateType.WISDOM_PRUDENCE:
            return self._assess_wisdom(content, context)
        elif self.gate_type == EthosGateType.SUSTAINABILITY:
            return self._assess_sustainability(content, context)
        else:
            # Generic assessment for other gate types
            return self._assess_generic_values(content, context)
            
    def _assess_truth_accuracy(self, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess truth and accuracy aspects"""
        factors = []
        score = 0.5  # Neutral starting point
        
        # Look for factual claims
        factual_indicators = ["studies show", "research indicates", "data suggests", "statistics", "evidence"]
        factual_claims = sum(1 for indicator in factual_indicators if indicator in content)
        
        # Look for uncertainty acknowledgment
        uncertainty_indicators = ["might", "may", "possibly", "uncertain", "unclear", "unknown"]
        uncertainty_acknowledgments = sum(1 for indicator in uncertainty_indicators if indicator in content)
        
        # Look for problematic certainty claims
        absolute_claims = ["always", "never", "all", "none", "definitely", "certainly", "absolutely"]
        absolute_count = sum(1 for claim in absolute_claims if claim in content)
        
        if factual_claims > 0:
            factors.append("Contains factual claims requiring verification")
            score += 0.1
            
        if uncertainty_acknowledgments > 0:
            factors.append("Acknowledges uncertainty appropriately")
            score += 0.2
            
        if absolute_count > 2:
            factors.append("Makes excessive absolute claims without evidence")
            score -= 0.3
            
        return {"score": score, "factors": factors}
        
    def _assess_harm_potential(self, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess potential for harm"""
        factors = []
        score = 0.7  # Default to relatively safe
        
        # Physical harm indicators
        physical_harm = ["violence", "injury", "damage", "destroy", "attack", "weapon"]
        physical_matches = sum(1 for term in physical_harm if term in content)
        
        # Emotional harm indicators  
        emotional_harm = ["humiliate", "embarrass", "shame", "ridicule", "mock", "bully"]
        emotional_matches = sum(1 for term in emotional_harm if term in content)
        
        # Safety language
        safety_language = ["safe", "careful", "caution", "warning", "protect", "secure"]
        safety_matches = sum(1 for term in safety_language if term in content)
        
        if physical_matches > 0:
            factors.append("Contains references to potential physical harm")
            score -= 0.4
            
        if emotional_matches > 0:
            factors.append("Contains potential emotional harm indicators")
            score -= 0.2
            
        if safety_matches > 0:
            factors.append("Includes safety considerations")
            score += 0.1
            
        return {"score": max(0.0, score), "factors": factors}
        
    def _assess_fairness(self, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess fairness and justice aspects"""
        factors = []
        score = 0.5  # Neutral
        
        # Bias indicators
        bias_terms = ["stereotype", "generalization", "always", "never", "all [group]", "those people"]
        potential_bias = sum(1 for term in bias_terms if term in content)
        
        # Fairness language
        fairness_terms = ["equal", "fair", "just", "equitable", "balanced", "impartial"]
        fairness_indicators = sum(1 for term in fairness_terms if term in content)
        
        # Inclusive language
        inclusive_terms = ["everyone", "all people", "inclusive", "diverse", "respectful"]
        inclusive_language = sum(1 for term in inclusive_terms if term in content)
        
        if potential_bias > 0:
            factors.append("Contains potential bias or unfair generalizations")
            score -= 0.3
            
        if fairness_indicators > 0:
            factors.append("Uses fairness-oriented language")
            score += 0.2
            
        if inclusive_language > 0:
            factors.append("Demonstrates inclusive approach")
            score += 0.1
            
        return {"score": score, "factors": factors}
        
    def _assess_autonomy_respect(self, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess respect for autonomy and consent"""
        factors = []
        score = 0.6  # Default to respecting autonomy
        
        # Coercive language
        coercive_terms = ["must", "should", "have to", "required", "forced", "no choice"]
        coercive_count = sum(1 for term in coercive_terms if term in content)
        
        # Choice language
        choice_terms = ["choose", "decide", "option", "voluntary", "consent", "preference"]
        choice_count = sum(1 for term in choice_terms if term in content)
        
        # Manipulative patterns
        manipulation_terms = ["trick", "convince", "pressure", "manipulate", "force"]
        manipulation_count = sum(1 for term in manipulation_terms if term in content)
        
        if coercive_count > 2:
            factors.append("Contains potentially coercive language")
            score -= 0.2
            
        if choice_count > 0:
            factors.append("Acknowledges individual choice and autonomy")
            score += 0.2
            
        if manipulation_count > 0:
            factors.append("Contains potentially manipulative elements")
            score -= 0.3
            
        return {"score": score, "factors": factors}
        
    def _assess_beneficence(self, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess beneficial intent and positive contribution"""
        factors = []
        score = 0.5  # Neutral
        
        # Helpful language
        helpful_terms = ["help", "benefit", "improve", "enhance", "support", "assist", "useful"]
        helpful_count = sum(1 for term in helpful_terms if term in content)
        
        # Constructive language
        constructive_terms = ["build", "create", "develop", "grow", "progress", "advance"]
        constructive_count = sum(1 for term in constructive_terms if term in content)
        
        # Destructive language
        destructive_terms = ["destroy", "ruin", "damage", "harm", "break", "waste"]
        destructive_count = sum(1 for term in destructive_terms if term in content)
        
        if helpful_count > 0:
            factors.append("Demonstrates helpful intent")
            score += 0.2
            
        if constructive_count > 0:
            factors.append("Focuses on constructive outcomes")
            score += 0.1
            
        if destructive_count > 0:
            factors.append("Contains potentially destructive elements")
            score -= 0.2
            
        return {"score": score, "factors": factors}
        
    def _assess_transparency(self, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess transparency and openness"""
        factors = []
        score = 0.5  # Neutral
        
        # Transparency indicators
        transparent_terms = ["transparent", "open", "clear", "honest", "direct", "explicit"]
        transparency_count = sum(1 for term in transparent_terms if term in content)
        
        # Opacity indicators
        opacity_terms = ["hidden", "secret", "concealed", "unclear", "vague", "ambiguous"]
        opacity_count = sum(1 for term in opacity_terms if term in content)
        
        # Disclosure language
        disclosure_terms = ["disclose", "reveal", "admit", "acknowledge", "confess"]
        disclosure_count = sum(1 for term in disclosure_terms if term in content)
        
        if transparency_count > 0:
            factors.append("Demonstrates transparency")
            score += 0.2
            
        if disclosure_count > 0:
            factors.append("Includes appropriate disclosure")
            score += 0.1
            
        if opacity_count > 0:
            factors.append("Contains potentially opaque elements")
            score -= 0.2
            
        return {"score": score, "factors": factors}
        
    def _assess_compassion(self, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess compassion and empathy"""
        factors = []
        score = 0.5  # Neutral
        
        # Compassionate language
        compassion_terms = ["compassionate", "caring", "kind", "understanding", "empathetic", "supportive"]
        compassion_count = sum(1 for term in compassion_terms if term in content)
        
        # Callous language
        callous_terms = ["callous", "cruel", "heartless", "indifferent", "cold", "uncaring"]
        callous_count = sum(1 for term in callous_terms if term in content)
        
        # Emotional awareness
        emotion_terms = ["feel", "emotion", "understand", "recognize", "acknowledge feelings"]
        emotion_count = sum(1 for term in emotion_terms if term in content)
        
        if compassion_count > 0:
            factors.append("Demonstrates compassionate approach")
            score += 0.3
            
        if emotion_count > 0:
            factors.append("Shows emotional awareness")
            score += 0.1
            
        if callous_count > 0:
            factors.append("Contains potentially callous elements")
            score -= 0.3
            
        return {"score": score, "factors": factors}
        
    def _assess_wisdom(self, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess wisdom and prudence"""
        factors = []
        score = 0.5  # Neutral
        
        # Wisdom indicators
        wisdom_terms = ["consider", "think", "reflect", "ponder", "contemplate", "wise"]
        wisdom_count = sum(1 for term in wisdom_terms if term in content)
        
        # Reckless language
        reckless_terms = ["reckless", "impulsive", "hasty", "thoughtless", "careless"]
        reckless_count = sum(1 for term in reckless_terms if term in content)
        
        # Long-term thinking
        longterm_terms = ["future", "consequences", "long-term", "sustainable", "enduring"]
        longterm_count = sum(1 for term in longterm_terms if term in content)
        
        if wisdom_count > 0:
            factors.append("Demonstrates thoughtful consideration")
            score += 0.2
            
        if longterm_count > 0:
            factors.append("Shows long-term perspective")
            score += 0.1
            
        if reckless_count > 0:
            factors.append("Contains potentially reckless elements")
            score -= 0.3
            
        return {"score": score, "factors": factors}
        
    def _assess_sustainability(self, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Assess sustainability considerations"""
        factors = []
        score = 0.5  # Neutral
        
        # Sustainability language
        sustainability_terms = ["sustainable", "renewable", "conservation", "environment", "eco-friendly"]
        sustainability_count = sum(1 for term in sustainability_terms if term in content)
        
        # Waste/destruction language
        waste_terms = ["waste", "disposable", "throw away", "consume", "exploit"]
        waste_count = sum(1 for term in waste_terms if term in content)
        
        if sustainability_count > 0:
            factors.append("Includes sustainability considerations")
            score += 0.2
            
        if waste_count > 0:
            factors.append("Contains potentially wasteful elements")
            score -= 0.1
            
        return {"score": score, "factors": factors}
        
    def _assess_generic_values(self, content: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Generic value assessment for other gate types"""
        factors = ["Generic value assessment performed"]
        
        # Simple positive/negative sentiment
        positive_terms = ["good", "positive", "beneficial", "helpful", "constructive"]
        negative_terms = ["bad", "negative", "harmful", "destructive", "problematic"]
        
        positive_count = sum(1 for term in positive_terms if term in content)
        negative_count = sum(1 for term in negative_terms if term in content)
        
        score = 0.5 + (positive_count - negative_count) * 0.1
        
        return {"score": max(0.0, min(1.0, score)), "factors": factors}
        
    def _apply_contextual_modifiers(self, assessment: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """Apply contextual modifiers to the assessment"""
        modified_score = assessment["score"]
        contextual_factors = {}
        
        # Apply rule-based contextual modifiers
        for context_key, modifier in self.gate_rules["contextual_modifiers"].items():
            if context_key in str(context).lower():
                old_score = modified_score
                modified_score = min(1.0, max(0.0, modified_score * modifier))
                contextual_factors[context_key] = {
                    "modifier": modifier,
                    "original_score": old_score,
                    "modified_score": modified_score
                }
                
        # Consider domain-specific contexts
        if "domain" in context:
            domain_modifier = self._get_domain_modifier(context["domain"])
            if domain_modifier != 1.0:
                old_score = modified_score
                modified_score = min(1.0, max(0.0, modified_score * domain_modifier))
                contextual_factors["domain"] = {
                    "domain": context["domain"],
                    "modifier": domain_modifier,
                    "original_score": old_score,
                    "modified_score": modified_score
                }
                
        modified_assessment = assessment.copy()
        modified_assessment["score"] = modified_score
        modified_assessment["contextual_factors"] = contextual_factors
        
        return modified_assessment
        
    def _get_domain_modifier(self, domain: str) -> float:
        """Get domain-specific modifier for this gate type"""
        domain_modifiers = {
            # Truth/Accuracy more critical in certain domains
            EthosGateType.TRUTH_ACCURACY: {
                "medical": 1.3, "legal": 1.2, "financial": 1.2, "education": 1.1,
                "entertainment": 0.8, "fiction": 0.6
            },
            # Harm prevention especially important for vulnerable contexts
            EthosGateType.HARM_PREVENTION: {
                "medical": 1.4, "children": 1.5, "mental_health": 1.3, "safety": 1.2,
                "gaming": 0.9, "fiction": 0.7
            },
            # Fairness critical in decision-making contexts
            EthosGateType.FAIRNESS_JUSTICE: {
                "legal": 1.4, "hiring": 1.3, "lending": 1.3, "education": 1.2,
                "entertainment": 0.9
            }
        }
        
        gate_modifiers = domain_modifiers.get(self.gate_type, {})
        return gate_modifiers.get(domain.lower(), 1.0)
        
    def _make_gate_decision(self, assessment: Dict[str, Any]) -> Dict[str, Any]:
        """Make final gate decision based on assessment"""
        score = assessment["score"]
        thresholds = self.gate_rules["escalation_thresholds"]
        
        # Determine action based on score and sensitivity
        effective_warning_threshold = thresholds["warning"] * self.sensitivity
        effective_block_threshold = thresholds["block"] * self.sensitivity
        
        if score >= (1.0 - effective_warning_threshold):
            action = "pass"
            confidence = score
            reasoning = "Content aligns well with values"
            recommendations = []
            
        elif score >= (1.0 - effective_block_threshold):
            action = "warning"
            confidence = 1.0 - score
            reasoning = f"Content raises moderate concerns for {self.gate_type.value}"
            recommendations = self._generate_recommendations(assessment, "warning")
            
        else:
            action = "block"
            confidence = 1.0 - score
            reasoning = f"Content significantly violates {self.gate_type.value} values"
            recommendations = self._generate_recommendations(assessment, "block")
            
        return {
            "action": action,
            "confidence": confidence,
            "reasoning": reasoning,
            "recommendations": recommendations,
            "thresholds_used": {
                "warning": effective_warning_threshold,
                "block": effective_block_threshold
            }
        }
        
    def _generate_recommendations(self, assessment: Dict[str, Any], action: str) -> List[str]:
        """Generate recommendations for improvement"""
        recommendations = []
        
        negative_indicators = assessment["indicators"]["negative_keywords"]
        specific_factors = assessment.get("specific_factors", [])
        
        if negative_indicators:
            recommendations.append(f"Consider revising language that includes: {', '.join(negative_indicators[:3])}")
            
        if self.gate_type == EthosGateType.TRUTH_ACCURACY and action in ["warning", "block"]:
            recommendations.append("Add citations or acknowledge uncertainty where appropriate")
            recommendations.append("Verify factual claims before presenting as definitive")
            
        elif self.gate_type == EthosGateType.HARM_PREVENTION and action in ["warning", "block"]:
            recommendations.append("Consider potential negative consequences and add appropriate warnings")
            recommendations.append("Ensure safety considerations are addressed")
            
        elif self.gate_type == EthosGateType.FAIRNESS_JUSTICE and action in ["warning", "block"]:
            recommendations.append("Review for potential bias or unfair generalizations")
            recommendations.append("Ensure equitable treatment of all groups mentioned")
            
        # Add general recommendations based on specific factors
        for factor in specific_factors:
            if "bias" in factor.lower():
                recommendations.append("Review content for potential bias and ensure balanced perspective")
            elif "harm" in factor.lower():
                recommendations.append("Consider adding safety warnings or protective measures")
                
        return recommendations[:5]  # Limit to top 5 recommendations
        
    def _update_statistics(self, decision: Dict[str, Any]):
        """Update gate statistics based on decision"""
        action = decision["action"]
        
        if action == "pass":
            self.pass_count += 1
        elif action == "warning":
            self.warning_count += 1
        elif action == "block":
            self.block_count += 1
            
    def _record_assessment(self, content: str, context: Dict[str, Any], 
                         assessment: Dict[str, Any], decision: Dict[str, Any]):
        """Record assessment in learning history"""
        record = {
            "timestamp": datetime.now().isoformat(),
            "content_sample": content[:100],  # First 100 chars
            "context": context,
            "assessment_score": assessment["score"],
            "decision": decision["action"],
            "confidence": decision["confidence"],
            "negative_indicators": len(assessment["indicators"]["negative_keywords"]),
            "positive_indicators": len(assessment["indicators"]["positive_keywords"])
        }
        
        self.learning_history.append(record)
        
        # Keep history manageable
        if len(self.learning_history) > 1000:
            self.learning_history = self.learning_history[-500:]
            
    def get_gate_statistics(self) -> Dict[str, Any]:
        """Get comprehensive gate statistics"""
        total_activations = self.activation_count
        
        if total_activations == 0:
            return {"status": "no_activations"}
            
        pass_rate = self.pass_count / total_activations
        warning_rate = self.warning_count / total_activations
        block_rate = self.block_count / total_activations
        
        # Recent performance analysis
        recent_history = self.learning_history[-50:] if len(self.learning_history) >= 50 else self.learning_history
        recent_scores = [record["assessment_score"] for record in recent_history]
        
        avg_score = np.mean(recent_scores) if recent_scores else 0.0
        score_variance = np.var(recent_scores) if len(recent_scores) > 1 else 0.0
        
        return {
            "gate_type": self.gate_type.value,
            "total_activations": total_activations,
            "pass_count": self.pass_count,
            "warning_count": self.warning_count,
            "block_count": self.block_count,
            "pass_rate": pass_rate,
            "warning_rate": warning_rate,
            "block_rate": block_rate,
            "sensitivity": self.sensitivity,
            "weight": self.weight,
            "avg_assessment_score": avg_score,
            "score_variance": score_variance,
            "recent_assessments": len(recent_history)
        }


class EthosGateSystem:
    """
    Ethos Gate System - Manages all 27 Ethos gates
    Provides comprehensive value-based filtering and ethical alignment
    """
    
    def __init__(self):
        self.gates = {}
        self.system_statistics = {
            "total_evaluations": 0,
            "system_pass_rate": 0.0,
            "most_active_gates": [],
            "most_blocking_gates": []
        }
        
        # Initialize 27 Ethos gates
        self._initialize_ethos_gates()
        
        # System configuration
        self.consensus_threshold = 0.7  # Threshold for system-wide decisions
        self.gate_weight_adjustment = True
        self.learning_enabled = True
        
        logging.info(f"⚡ EthosGateSystem initialized with {len(self.gates)} gates")
        
    def _initialize_ethos_gates(self):
        """Initialize all 27 Ethos gates"""
        gate_types = list(EthosGateType)
        
        # Ensure we have exactly 27 gates
        if len(gate_types) != 27:
            logging.warning(f"Expected 27 gate types, found {len(gate_types)}")
            
        for i, gate_type in enumerate(gate_types):
            gate_id = i + 1
            
            # Set different sensitivities for different types
            sensitivity = self._get_default_sensitivity(gate_type)
            weight = self._get_default_weight(gate_type)
            
            gate = EthosGate(
                gate_id=gate_id,
                gate_type=gate_type,
                sensitivity=sensitivity,
                weight=weight
            )
            
            self.gates[gate_id] = gate
            
        logging.info(f"✨ Initialized {len(self.gates)} Ethos gates")
        
    def _get_default_sensitivity(self, gate_type: EthosGateType) -> float:
        """Get default sensitivity for gate type"""
        # Critical gates have higher sensitivity (lower threshold)
        critical_gates = {
            EthosGateType.HARM_PREVENTION: 0.9,
            EthosGateType.TRUTH_ACCURACY: 0.8,
            EthosGateType.FAIRNESS_JUSTICE: 0.8,
            EthosGateType.PRIVACY_PROTECTION: 0.8,
            EthosGateType.NON_MALEFICENCE: 0.9
        }
        
        return critical_gates.get(gate_type, 0.7)  # Default sensitivity
        
    def _get_default_weight(self, gate_type: EthosGateType) -> float:
        """Get default weight for gate type"""
        # More important gates have higher weights
        important_gates = {
            EthosGateType.HARM_PREVENTION: 1.5,
            EthosGateType.TRUTH_ACCURACY: 1.3,
            EthosGateType.FAIRNESS_JUSTICE: 1.3,
            EthosGateType.BENEFICENCE: 1.2,
            EthosGateType.NON_MALEFICENCE: 1.5,
            EthosGateType.RESPONSIBILITY: 1.2
        }
        
        return important_gates.get(gate_type, 1.0)  # Default weight
        
    def evaluate_content(self, content: Any, context: Dict[str, Any] = None, 
                        selected_gates: List[int] = None) -> Dict[str, Any]:
        """
        Evaluate content through Ethos gate system
        Returns comprehensive ethical assessment
        """
        context = context or {}
        evaluation_start = datetime.now()
        
        try:
            self.system_statistics["total_evaluations"] += 1
            
            # Determine which gates to use
            if selected_gates:
                active_gates = {gid: gate for gid, gate in self.gates.items() if gid in selected_gates}
            else:
                active_gates = self.gates
                
            # Evaluate through all active gates
            gate_results = {}
            for gate_id, gate in active_gates.items():
                gate_result = gate.evaluate(content, context)
                gate_results[gate_id] = gate_result
                
            # Compute system-wide assessment
            system_assessment = self._compute_system_assessment(gate_results)
            
            # Make final system decision
            system_decision = self._make_system_decision(system_assessment, gate_results)
            
            # Update system statistics
            self._update_system_statistics(system_decision, gate_results)
            
            evaluation_time = (datetime.now() - evaluation_start).total_seconds()
            
            result = {
                "system_decision": system_decision,
                "system_assessment": system_assessment,
                "gate_results": gate_results,
                "gates_evaluated": len(active_gates),
                "evaluation_time": evaluation_time,
                "consensus_achieved": system_assessment["consensus_score"] >= self.consensus_threshold,
                "recommendations": system_decision.get("recommendations", []),
                "ethical_summary": self._generate_ethical_summary(system_assessment, gate_results)
            }
            
            # Log significant decisions
            if system_decision["action"] in ["warning", "block"]:
                logging.warning(f"⚡ Ethos System: {system_decision['action']} - "
                              f"Consensus: {system_assessment['consensus_score']:.2f}")
                              
            return result
            
        except Exception as e:
            logging.error(f"Ethos gate system evaluation error: {e}")
            return {
                "system_decision": {"action": "error", "confidence": 0.0},
                "error": str(e),
                "gates_evaluated": 0
            }
            
    def _compute_system_assessment(self, gate_results: Dict[int, Dict[str, Any]]) -> Dict[str, Any]:
        """Compute system-wide assessment from gate results"""
        if not gate_results:
            return {"consensus_score": 0.0, "weighted_score": 0.0}
            
        # Collect scores and weights
        scores = []
        weights = []
        decisions = {"pass": 0, "warning": 0, "block": 0, "error": 0}
        
        for gate_id, result in gate_results.items():
            if gate_id in self.gates:
                gate = self.gates[gate_id]
                scores.append(result["assessment_score"])
                weights.append(gate.weight)
                
                decision = result["decision"]
                if decision in decisions:
                    decisions[decision] += 1
                    
        # Calculate weighted average score
        if scores and weights:
            weighted_score = np.average(scores, weights=weights)
        else:
            weighted_score = 0.0
            
        # Calculate consensus (how much gates agree)
        if len(scores) > 1:
            score_variance = np.var(scores)
            consensus_score = max(0.0, 1.0 - (score_variance * 2))  # Lower variance = higher consensus
        else:
            consensus_score = 1.0 if scores else 0.0
            
        # Identify concerning gates (low scores)
        concerning_gates = [
            gate_id for gate_id, result in gate_results.items()
            if result["assessment_score"] < 0.5 and result["decision"] in ["warning", "block"]
        ]
        
        # Identify supporting gates (high scores)
        supporting_gates = [
            gate_id for gate_id, result in gate_results.items()
            if result["assessment_score"] > 0.7 and result["decision"] == "pass"
        ]
        
        return {
            "weighted_score": weighted_score,
            "consensus_score": consensus_score,
            "score_variance": np.var(scores) if len(scores) > 1 else 0.0,
            "decision_distribution": decisions,
            "concerning_gates": concerning_gates,
            "supporting_gates": supporting_gates,
            "total_gates": len(gate_results)
        }
        
    def _make_system_decision(self, system_assessment: Dict[str, Any], 
                            gate_results: Dict[int, Dict[str, Any]]) -> Dict[str, Any]:
        """Make final system decision based on gate consensus"""
        weighted_score = system_assessment["weighted_score"]
        consensus_score = system_assessment["consensus_score"]
        decisions = system_assessment["decision_distribution"]
        
        # System decision logic
        block_count = decisions.get("block", 0)
        warning_count = decisions.get("warning", 0)
        pass_count = decisions.get("pass", 0)
        total_decisions = block_count + warning_count + pass_count
        
        if total_decisions == 0:
            return {"action": "error", "confidence": 0.0, "reasoning": "No valid gate decisions"}
            
        # If any critical gate blocks, system blocks
        critical_blocks = []
        critical_gate_types = [EthosGateType.HARM_PREVENTION, EthosGateType.NON_MALEFICENCE]
        
        for gate_id, result in gate_results.items():
            if (gate_id in self.gates and 
                self.gates[gate_id].gate_type in critical_gate_types and
                result["decision"] == "block"):
                critical_blocks.append(gate_id)
                
        if critical_blocks:
            return {
                "action": "block",
                "confidence": 0.9,
                "reasoning": f"Critical ethical violations detected by gates: {critical_blocks}",
                "critical_violations": critical_blocks,
                "recommendations": self._generate_system_recommendations(system_assessment, gate_results, "block")
            }
            
        # Determine action based on weighted consensus
        block_rate = block_count / total_decisions
        warning_rate = warning_count / total_decisions
        
        if block_rate > 0.3 or weighted_score < 0.3:
            action = "block"
            confidence = 1.0 - weighted_score
            reasoning = f"High proportion of gates recommend blocking ({block_rate:.1%})"
            
        elif warning_rate > 0.4 or weighted_score < 0.6:
            action = "warning"
            confidence = abs(0.5 - weighted_score) * 2  # Distance from middle
            reasoning = f"Multiple gates raise concerns ({warning_rate:.1%} warnings)"
            
        else:
            action = "pass"
            confidence = weighted_score
            reasoning = f"Gates generally approve content ({pass_count}/{total_decisions} pass)"
            
        # Adjust confidence based on consensus
        confidence = confidence * (0.5 + consensus_score * 0.5)  # Lower consensus reduces confidence
        
        return {
            "action": action,
            "confidence": confidence,
            "reasoning": reasoning,
            "weighted_score": weighted_score,
            "consensus_score": consensus_score,
            "recommendations": self._generate_system_recommendations(system_assessment, gate_results, action)
        }
        
    def _generate_system_recommendations(self, system_assessment: Dict[str, Any],
                                       gate_results: Dict[int, Dict[str, Any]], 
                                       action: str) -> List[str]:
        """Generate system-wide recommendations"""
        recommendations = []
        concerning_gates = system_assessment.get("concerning_gates", [])
        
        # Collect recommendations from concerning gates
        gate_recommendations = set()
        for gate_id in concerning_gates:
            if gate_id in gate_results:
                gate_recs = gate_results[gate_id].get("recommendations", [])
                gate_recommendations.update(gate_recs)
                
        recommendations.extend(list(gate_recommendations)[:5])
        
        # Add system-level recommendations
        if action == "block":
            recommendations.append("Significant revision required to meet ethical standards")
            recommendations.append("Consider consulting ethics guidelines for your domain")
            
        elif action == "warning":
            recommendations.append("Review content for potential ethical concerns")
            recommendations.append("Consider adding appropriate disclaimers or warnings")
            
        # Add consensus-based recommendations
        consensus_score = system_assessment.get("consensus_score", 1.0)
        if consensus_score < 0.5:
            recommendations.append("Low consensus among ethics gates - consider seeking additional review")
            
        return recommendations[:7]  # Limit to top 7 recommendations
        
    def _generate_ethical_summary(self, system_assessment: Dict[str, Any],
                                gate_results: Dict[int, Dict[str, Any]]) -> Dict[str, Any]:
        """Generate summary of ethical assessment"""
        concerning_areas = []
        strong_areas = []
        
        for gate_id, result in gate_results.items():
            if gate_id in self.gates:
                gate_type = self.gates[gate_id].gate_type.value
                score = result["assessment_score"]
                
                if score < 0.4:
                    concerning_areas.append(gate_type)
                elif score > 0.8:
                    strong_areas.append(gate_type)
                    
        summary = {
            "overall_ethical_score": system_assessment["weighted_score"],
            "consensus_level": "high" if system_assessment["consensus_score"] > 0.7 else 
                              "medium" if system_assessment["consensus_score"] > 0.4 else "low",
            "concerning_areas": concerning_areas,
            "strong_areas": strong_areas,
            "gates_activated": system_assessment["total_gates"],
            "primary_concerns": concerning_areas[:3],  # Top 3 concerns
            "primary_strengths": strong_areas[:3]      # Top 3 strengths
        }
        
        return summary
        
    def _update_system_statistics(self, system_decision: Dict[str, Any], 
                                gate_results: Dict[int, Dict[str, Any]]):
        """Update system-wide statistics"""
        # Update pass rate
        if system_decision["action"] == "pass":
            current_passes = self.system_statistics["total_evaluations"] * self.system_statistics["system_pass_rate"]
            new_pass_rate = (current_passes + 1) / self.system_statistics["total_evaluations"]
            self.system_statistics["system_pass_rate"] = new_pass_rate
        else:
            current_passes = self.system_statistics["total_evaluations"] * self.system_statistics["system_pass_rate"]
            new_pass_rate = current_passes / self.system_statistics["total_evaluations"]
            self.system_statistics["system_pass_rate"] = new_pass_rate
            
        # Track most active gates
        gate_activity = {}
        for gate_id in gate_results.keys():
            if gate_id in self.gates:
                gate_activity[gate_id] = self.gates[gate_id].activation_count
                
        # Update most active gates (top 5)
        sorted_activity = sorted(gate_activity.items(), key=lambda x: x[1], reverse=True)
        self.system_statistics["most_active_gates"] = sorted_activity[:5]
        
        # Track most blocking gates
        gate_blocking = {}
        for gate_id, gate in self.gates.items():
            if gate.activation_count > 0:
                gate_blocking[gate_id] = gate.block_count / gate.activation_count
                
        sorted_blocking = sorted(gate_blocking.items(), key=lambda x: x[1], reverse=True)
        self.system_statistics["most_blocking_gates"] = sorted_blocking[:5]
        
    def get_system_report(self) -> Dict[str, Any]:
        """Generate comprehensive system report"""
        # Individual gate statistics
        gate_stats = {}
        for gate_id, gate in self.gates.items():
            gate_stats[gate_id] = gate.get_gate_statistics()
            
        # System performance metrics
        total_activations = sum(gate.activation_count for gate in self.gates.values())
        total_passes = sum(gate.pass_count for gate in self.gates.values())
        total_warnings = sum(gate.warning_count for gate in self.gates.values())
        total_blocks = sum(gate.block_count for gate in self.gates.values())
        
        system_performance = {
            "total_gate_activations": total_activations,
            "system_wide_pass_rate": total_passes / max(1, total_activations),
            "system_wide_warning_rate": total_warnings / max(1, total_activations),
            "system_wide_block_rate": total_blocks / max(1, total_activations)
        }
        
        # Gate type analysis
        gate_type_performance = {}
        for gate_type in EthosGateType:
            type_gates = [gate for gate in self.gates.values() if gate.gate_type == gate_type]
            if type_gates:
                gate = type_gates[0]  # Should only be one gate per type
                gate_type_performance[gate_type.value] = {
                    "activations": gate.activation_count,
                    "pass_rate": gate.pass_count / max(1, gate.activation_count),
                    "sensitivity": gate.sensitivity,
                    "weight": gate.weight
                }
                
        report = {
            "system_statistics": self.system_statistics,
            "system_performance": system_performance,
            "gate_statistics": gate_stats,
            "gate_type_performance": gate_type_performance,
            "total_gates": len(self.gates),
            "consensus_threshold": self.consensus_threshold,
            "learning_enabled": self.learning_enabled,
            "report_timestamp": datetime.now().isoformat()
        }
        
        return report
        
    def adjust_gate_sensitivity(self, gate_id: int, new_sensitivity: float):
        """Adjust sensitivity of a specific gate"""
        if gate_id in self.gates:
            old_sensitivity = self.gates[gate_id].sensitivity
            self.gates[gate_id].sensitivity = max(0.1, min(1.0, new_sensitivity))
            
            logging.info(f"⚡ Gate {gate_id} sensitivity adjusted: {old_sensitivity:.2f} → {new_sensitivity:.2f}")
        else:
            logging.warning(f"Gate {gate_id} not found for sensitivity adjustment")
            
    def adjust_gate_weight(self, gate_id: int, new_weight: float):
        """Adjust weight of a specific gate"""
        if gate_id in self.gates:
            old_weight = self.gates[gate_id].weight
            self.gates[gate_id].weight = max(0.1, min(3.0, new_weight))
            
            logging.info(f"⚡ Gate {gate_id} weight adjusted: {old_weight:.2f} → {new_weight:.2f}")
        else:
            logging.warning(f"Gate {gate_id} not found for weight adjustment")
            
    def reset_system_statistics(self):
        """Reset system statistics (for testing)"""
        for gate in self.gates.values():
            gate.activation_count = 0
            gate.pass_count = 0
            gate.warning_count = 0
            gate.block_count = 0
            gate.learning_history.clear()
            
        self.system_statistics = {
            "total_evaluations": 0,
            "system_pass_rate": 0.0,
            "most_active_gates": [],
            "most_blocking_gates": []
        }
        
        logging.info("🔄 Ethos gate system statistics reset")