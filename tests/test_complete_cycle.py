"""
Complete cycle integration test for the Autonomous Technical Expert Framework
Tests the full information_gathering → safe_development → quality_assurance cycle
"""

import pytest
import os
import tempfile
import shutil
from unittest.mock import Mock, patch
from src.core.autonomous_framework import AutonomousTechnicalExpertFramework


class TestCompleteCycle:
    """Test the complete framework cycle"""
    
    @pytest.fixture
    def framework(self):
        """Create framework instance with temporary workspace"""
        temp_dir = tempfile.mkdtemp()
        framework = AutonomousTechnicalExpertFramework(
            project_name="Complete Cycle Test",
            workspace_path=temp_dir
        )
        yield framework
        shutil.rmtree(temp_dir, ignore_errors=True)
    
    def test_complete_framework_cycle(self, framework):
        """Test the complete cycle: information gathering → safe development → quality assurance"""
        
        # Phase 1: Information Gathering
        # semantic_search → file_search → read_file → grep_search
        
        # Create context files for information gathering
        context_file = os.path.join(framework.workspace_path, "context.md")
        with open(context_file, 'w') as f:
            f.write("""
# Project Context
This is a test project for demonstrating the complete framework cycle.

## Requirements
- Create a calculator module
- Include proper error handling
- Implement comprehensive testing
- Follow professional standards

## Architecture
The calculator should have basic operations:
- Addition
- Subtraction
- Multiplication
- Division (with zero-division protection)
            """)
        
        # Test information gathering phase
        info_result = framework.gather_comprehensive_information("calculator module requirements")
        
        assert "context_files" in info_result
        assert "requirements" in info_result
        assert "architecture_info" in info_result
        assert len(info_result["context_files"]) > 0
        
        # Phase 2: Safe Development
        # create_directory → create_file → list_dir → get_errors
        
        # Test safe development phase using gathered information
        dev_result = framework.implement_safe_development(info_result)
        
        assert "created_directories" in dev_result
        assert "created_files" in dev_result
        assert "safety_checks" in dev_result
        assert dev_result["safety_checks"]["directory_exists"]
        assert dev_result["safety_checks"]["files_created"]
        assert dev_result["safety_checks"]["no_errors"]
        
        # Phase 3: Quality Assurance
        # read_file → replace_string_in_file → get_errors → runTests
        
        # Test quality assurance phase on developed code
        qa_result = framework.validate_professional_quality_complete(dev_result)
        
        assert "error_handling" in qa_result
        assert "documentation" in qa_result
        assert "performance_optimized" in qa_result
        assert "testing_coverage" in qa_result
        assert "security_compliance" in qa_result
        assert "maintainability_score" in qa_result
        
        # Verify complete cycle effectiveness
        cycle_metrics = framework.measure_complete_cycle_effectiveness()
        
        assert "information_gathering_score" in cycle_metrics
        assert "safe_development_score" in cycle_metrics
        assert "quality_assurance_score" in cycle_metrics
        assert "overall_effectiveness" in cycle_metrics
        
        # Overall effectiveness should be high for successful cycle
        assert cycle_metrics["overall_effectiveness"] > 0.7
    
    def test_partnership_decision_making(self, framework):
        """Test AI-Human partnership decision making throughout the cycle"""
        
        # Create decision points throughout the cycle
        decision_points = [
            {
                "phase": "information_gathering",
                "decision": "Which files to analyze first",
                "context": "Multiple configuration files found",
                "ai_recommendation": "Start with main config file",
                "human_input": "Focus on security settings first"
            },
            {
                "phase": "safe_development", 
                "decision": "Error handling strategy",
                "context": "Multiple error types possible",
                "ai_recommendation": "Comprehensive try-catch blocks",
                "human_input": "Include specific error messages"
            },
            {
                "phase": "quality_assurance",
                "decision": "Testing approach",
                "context": "Multiple testing frameworks available",
                "ai_recommendation": "Use pytest for consistency",
                "human_input": "Include integration tests"
            }
        ]
        
        for decision_point in decision_points:
            result = framework.make_partnership_decision(decision_point)
            
            assert "consensus_reached" in result
            assert "final_decision" in result
            assert "reasoning" in result
            assert result["consensus_reached"] == True
            
            # Decision should incorporate both AI and human input
            final_decision = result["final_decision"].lower()
            ai_elements = any(word in final_decision for word in decision_point["ai_recommendation"].lower().split())
            human_elements = any(word in final_decision for word in decision_point["human_input"].lower().split())
            
            assert ai_elements or human_elements, "Decision should incorporate AI or human input"
    
    def test_knowledge_preservation(self, framework):
        """Test that knowledge is preserved throughout the complete cycle"""
        
        # Start with initial knowledge
        initial_knowledge = {
            "project_requirements": ["calculator", "error handling", "testing"],
            "architecture_decisions": ["modular design", "separation of concerns"],
            "quality_standards": ["documentation", "type hints", "error handling"]
        }
        
        framework.preserve_knowledge(initial_knowledge)
        
        # Simulate cycle phases and knowledge evolution
        phases = ["information_gathering", "safe_development", "quality_assurance"]
        
        for phase in phases:
            # Knowledge should be accessible and growing
            current_knowledge = framework.get_preserved_knowledge()
            
            assert "project_requirements" in current_knowledge
            assert "architecture_decisions" in current_knowledge
            assert "quality_standards" in current_knowledge
            
            # Add phase-specific knowledge
            phase_knowledge = {
                f"{phase}_insights": [f"{phase} completed successfully"],
                f"{phase}_decisions": [f"Best practices applied in {phase}"]
            }
            
            framework.preserve_knowledge(phase_knowledge)
        
        # Final knowledge should include all phases
        final_knowledge = framework.get_preserved_knowledge()
        
        for phase in phases:
            assert f"{phase}_insights" in final_knowledge
            assert f"{phase}_decisions" in final_knowledge
    
    def test_continuous_improvement(self, framework):
        """Test continuous improvement throughout cycles"""
        
        # Run multiple cycles to test improvement
        cycle_results = []
        
        for cycle_num in range(3):
            cycle_result = framework.run_complete_cycle(
                task=f"Cycle {cycle_num + 1}: Build and improve calculator",
                previous_results=cycle_results
            )
            
            cycle_results.append(cycle_result)
            
            assert "cycle_number" in cycle_result
            assert "improvements_made" in cycle_result
            assert "effectiveness_score" in cycle_result
            
            # Each cycle should show improvement or maintain high quality
            if cycle_num > 0:
                previous_score = cycle_results[cycle_num - 1]["effectiveness_score"]
                current_score = cycle_result["effectiveness_score"]
                
                # Score should improve or maintain high quality (> 0.8)
                assert current_score >= previous_score or current_score > 0.8
    
    def test_system_reliability(self, framework):
        """Test system reliability across multiple operations"""
        
        # Test system reliability with various scenarios
        test_scenarios = [
            {"task": "Create simple function", "complexity": "low"},
            {"task": "Build class hierarchy", "complexity": "medium"},
            {"task": "Implement design pattern", "complexity": "high"}
        ]
        
        reliability_scores = []
        
        for scenario in test_scenarios:
            try:
                result = framework.run_complete_cycle(
                    task=scenario["task"],
                    complexity=scenario["complexity"]
                )
                
                reliability_scores.append(result.get("reliability_score", 0.0))
                
            except Exception as e:
                # System should handle errors gracefully
                error_result = framework.handle_system_error(e, scenario)
                assert "error_handled" in error_result
                assert error_result["error_handled"] == True
                reliability_scores.append(0.5)  # Partial credit for error handling
        
        # Average reliability should be high
        avg_reliability = sum(reliability_scores) / len(reliability_scores)
        assert avg_reliability > 0.7, f"System reliability too low: {avg_reliability}"


class TestFrameworkEffectiveness:
    """Test overall framework effectiveness"""
    
    @pytest.fixture
    def framework(self):
        temp_dir = tempfile.mkdtemp()
        framework = AutonomousTechnicalExpertFramework(
            "Framework Effectiveness Test",
            temp_dir
        )
        yield framework
        shutil.rmtree(temp_dir, ignore_errors=True)
    
    def test_overall_framework_effectiveness(self, framework):
        """Test overall framework effectiveness measurement"""
        
        effectiveness_metrics = framework.measure_framework_effectiveness()
        
        required_metrics = [
            "information_gathering_effectiveness",
            "safe_development_effectiveness", 
            "quality_assurance_effectiveness",
            "partnership_effectiveness",
            "knowledge_preservation_effectiveness",
            "continuous_improvement_rate",
            "system_reliability_score",
            "overall_framework_score"
        ]
        
        for metric in required_metrics:
            assert metric in effectiveness_metrics
            assert isinstance(effectiveness_metrics[metric], (int, float))
            assert 0.0 <= effectiveness_metrics[metric] <= 1.0
        
        # Overall score should be high for effective framework
        assert effectiveness_metrics["overall_framework_score"] > 0.75
    
    def test_professional_standards_compliance(self, framework):
        """Test compliance with professional development standards"""
        
        standards_check = framework.validate_professional_standards()
        
        required_standards = [
            "code_quality",
            "documentation_completeness",
            "error_handling_coverage",
            "testing_coverage",
            "security_compliance",
            "performance_optimization",
            "maintainability_score"
        ]
        
        for standard in required_standards:
            assert standard in standards_check
            assert standards_check[standard] >= 0.8  # High professional standards
    
    def test_autonomous_operation(self, framework):
        """Test framework's ability to operate autonomously"""
        
        autonomous_result = framework.run_autonomous_cycle(
            duration_minutes=1,  # Short test run
            task="Create and test simple module"
        )
        
        assert "cycles_completed" in autonomous_result
        assert "decisions_made" in autonomous_result
        assert "human_interventions_needed" in autonomous_result
        assert "success_rate" in autonomous_result
        
        # Should be able to operate with minimal human intervention
        intervention_rate = autonomous_result["human_interventions_needed"] / autonomous_result["cycles_completed"]
        assert intervention_rate < 0.3  # Less than 30% intervention rate


if __name__ == "__main__":
    # Run tests directly
    pytest.main([__file__, "-v"])