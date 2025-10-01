"""
Test suite for PB2S Framework Integration
Tests the PB2S cycle management functionality
"""

import pytest
import json
from datetime import datetime
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the framework with correct path
import importlib.util
spec = importlib.util.spec_from_file_location(
    "autonomus_framework", 
    os.path.join(os.path.dirname(__file__), "..", r"C:\Users\Admin\Documents\pb2s\PB2S_PRODUCTION_READY\ITERATION_1\Autonomous_Technical_Expert_Framework\src\core", "autonomus_framework.py")
)
autonomus_framework = importlib.util.module_from_spec(spec)
spec.loader.exec_module(autonomus_framework)

AutonomousTechnicalExpertFramework = autonomus_framework.AutonomousTechnicalExpertFramework
PB2SStructures = autonomus_framework.PB2SStructures
PB2SCycle = autonomus_framework.PB2SCycle
FrameworkIntegration = autonomus_framework.FrameworkIntegration


class TestPB2SIntegration:
    """Test PB2S framework integration functionality"""
    
    @pytest.fixture
    def framework(self):
        """Create framework instance for testing"""
        # Create test workspace
        os.makedirs("./test_workspace", exist_ok=True)
        return AutonomousTechnicalExpertFramework(
            project_name="Test PB2S Integration",
            workspace_path="./test_workspace"
        )
    
    def test_pb2s_structures_creation(self):
        """Test PB2S structure constants are accessible"""
        single_cycle = PB2SStructures.get_single_cycle_structure()
        complete_cycles = PB2SStructures.get_complete_three_cycles_structure()
        
        assert "cycles" in single_cycle
        assert len(single_cycle["cycles"]) == 1
        assert single_cycle["cycles"][0]["cycle_number"] == 1
        
        assert "cycles" in complete_cycles
        assert len(complete_cycles["cycles"]) == 3
        assert "pb2s_framework" in complete_cycles
        assert complete_cycles["pb2s_framework"]["creator"] == "Shyamal Solanki (ZenAInomaly)"
    
    def test_pb2s_cycle_creation(self, framework):
        """Test creating PB2S cycles"""
        initial_cycles = len(framework.pb2s_cycles)
        
        cycle = framework.create_pb2s_cycle(
            cycle_number=1,
            perception_input="Test input",
            analysis_results={
                "contradictions_found": False,
                "assumptions_found": True, 
                "missing_evidence": False
            },
            reflection_flags=["assumption"],
            reflection_recommendation="Validate assumptions",
            action_taken="Requested validation data"
        )
        
        assert len(framework.pb2s_cycles) == initial_cycles + 1
        assert cycle.cycle_number == 1
        assert cycle.perception_input == "Test input"
        assert cycle.analysis_assumptions == True
        assert cycle.analysis_contradictions == False
        assert "assumption" in cycle.reflection_flags
        assert cycle.action_taken == "Requested validation data"
    
    def test_pb2s_conformance_validation(self, framework):
        """Test PB2S conformance validation"""
        # Test with insufficient cycles
        conformance = framework.validate_pb2s_conformance()
        assert not conformance["conformant"]
        assert not conformance["mandatory_cycles_met"]
        
        # Add required cycles
        for i in range(1, 4):
            framework.create_pb2s_cycle(
                cycle_number=i,
                perception_input=f"Test input {i}",
                analysis_results={
                    "contradictions_found": i == 2,  # Second cycle has contradictions
                    "assumptions_found": i == 1,     # First cycle has assumptions
                    "missing_evidence": i == 1       # First cycle missing evidence
                },
                reflection_flags=[] if i == 3 else [f"flag_{i}"],
                reflection_recommendation=f"Recommendation {i}",
                action_taken=f"Action {i}"
            )
        
        # Test with sufficient cycles
        conformance = framework.validate_pb2s_conformance()
        assert conformance["conformant"]
        assert conformance["mandatory_cycles_met"]
        assert conformance["total_cycles"] == 3
        assert len(conformance["validation_errors"]) == 0
    
    def test_pb2s_json_generation(self, framework):
        """Test PB2S JSON structure generation"""
        # Add sample cycles
        framework.create_pb2s_cycle(
            cycle_number=1,
            perception_input="Sample input",
            analysis_results={
                "contradictions_found": False,
                "assumptions_found": True,
                "missing_evidence": True
            },
            reflection_flags=["assumption", "missing_evidence"],
            reflection_recommendation="Gather more evidence",
            action_taken="Requested additional information"
        )
        
        # Test single cycle structure
        single_structure = framework.generate_pb2s_json_structure(single_cycle=True)
        assert "cycles" in single_structure
        assert len(single_structure["cycles"]) == 1
        assert single_structure["cycles"][0]["steps"][0]["step"] == "Perception"
        assert single_structure["cycles"][0]["steps"][0]["input"] == "Sample input"
        
        # Test complete structure
        complete_structure = framework.generate_pb2s_json_structure(single_cycle=False)
        assert "cycles" in complete_structure
        assert len(complete_structure["cycles"]) == 1  # Only one cycle created
    
    def test_vscode_snippets_generation(self):
        """Test VS Code snippets generation"""
        snippets = FrameworkIntegration.generate_pb2s_vscode_snippets()
        
        assert "PB2S Cycle Structure" in snippets
        assert "PB2S Complete 3 Cycles" in snippets
        
        cycle_snippet = snippets["PB2S Cycle Structure"]
        assert cycle_snippet["prefix"] == "pb2s-cycle"
        assert "body" in cycle_snippet
        assert "description" in cycle_snippet
        assert "Shyamal Solanki (ZenAInomaly)" in cycle_snippet["description"]
        
        complete_snippet = snippets["PB2S Complete 3 Cycles"]
        assert complete_snippet["prefix"] == "pb2s-full"
        assert "body" in complete_snippet
        assert "description" in complete_snippet
    
    def test_pb2s_export_functionality(self, framework):
        """Test exporting PB2S structure to file"""
        # Create sample cycle
        framework.create_pb2s_cycle(
            cycle_number=1,
            perception_input="Export test input",
            analysis_results={
                "contradictions_found": False,
                "assumptions_found": False,
                "missing_evidence": False
            },
            reflection_flags=[],
            reflection_recommendation="No issues found",
            action_taken="Proceed with export"
        )
        
        # Test export
        export_path = "./test_workspace/pb2s_export.json"
        result_path = framework.export_pb2s_structure_file(export_path, single_cycle=True)
        
        assert result_path == export_path
        assert os.path.exists(export_path)
        
        # Validate exported content
        with open(export_path, 'r') as f:
            exported_data = json.load(f)
        
        assert "cycles" in exported_data
        assert len(exported_data["cycles"]) == 1
        assert exported_data["cycles"][0]["steps"][0]["input"] == "Export test input"
        
        # Cleanup
        os.remove(export_path)
    
    def test_integration_logging(self, framework):
        """Test that PB2S operations are properly logged"""
        initial_log_count = len(framework.partnership_log)
        
        # Create a cycle (should generate log)
        framework.create_pb2s_cycle(
            cycle_number=1,
            perception_input="Logging test",
            analysis_results={"contradictions_found": False, "assumptions_found": False, "missing_evidence": False},
            reflection_flags=[],
            reflection_recommendation="Test recommendation",
            action_taken="Test action"
        )
        
        # Check logging
        assert len(framework.partnership_log) > initial_log_count
        latest_log = framework.partnership_log[-1]
        assert latest_log["action"] == "pb2s_cycle_created"
        assert "perception_input" in latest_log["details"]


if __name__ == "__main__":
    # Run tests directly
    pytest.main([__file__, "-v"])